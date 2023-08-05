// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module roboweb-extension
 */
import { IThemeManager, ICommandPalette } from '@jupyterlab/apputils';
import { ITranslator } from '@jupyterlab/translation';
import { NotebookActions, INotebookTracker } from '@jupyterlab/notebook';
import { Widget } from '@lumino/widgets';
const { Terminal } = require('@jupyterlab/terminal');
import { Kernel, KernelMessage} from '@jupyterlab/services';
import { JupyterFrontEnd, JupyterFrontEndPlugin } from '@jupyterlab/application';

class AssistantSidebar extends Widget {
  constructor() {
    super();
    this.id = 'assistant-panel';
    this.addClass('assistant-panel');
    this.title.caption = 'Assistant';
    this.title.iconClass = 'fa fa-robot';
  }
}

class NotebookAPI {
  constructor(manager, notebook) {
    this.manager = manager; 
    this.notebook = notebook;
    this.enableThemeSync = true;
  }
  isJupyter() {
    console.log("isJupyter");
    return true;
  }
  currentWindowType() {
    console.log("currentWindowType");

    return "notebook";
  }
  getCurrentJupyterTheme() {
    console.log("getCurrentJupyterTheme");

    return this.manager.theme;
  }
  changeThemeJupyter(theme) {

    console.log("changeThemeJupyter");
    manager.setTheme(theme);
    this.enableThemeSync = false;
  }
  run(index) {
    console.log("run");

    const notebook = this.notebook;
    if (notebook) {
      const notebookName = notebook.title.label;
      notebook.content.activeCellIndex = index;
      NotebookActions.runAllBelow(notebook.content, notebook.sessionContext);
    } else { 
      console.log("No notebook is active");
    }
  }
  runAll() {
    console.log("runAll");


    const notebook = this.notebook;
    if (notebook) {
      const notebookName = notebook.title.label;
      NotebookActions.runAll(notebook.content, notebook.sessionContext);
    } else { 
      console.log("No notebook is active");
    }
  }
  insertCellAt(code, index, replace) {
    console.log("insertCellAt");

    code = code.trim();
    if (index >= this.notebook.content.model.cells.length) {
      const cell = this.notebook.content.model.contentFactory.createCodeCell({});
      cell.value.text = code;
      this.notebook.content.model.cells.push(cell);
    } else { 
      if (replace) {
        const cell = this.notebook.content.model.cells.get(index);
        cell.value.text = code;
     } else {
        const cell = this.notebook.content.model.contentFactory.createCodeCell({});
        cell.value.text = code;
        this.notebook.content.model.cells.insert(index, cell);
      }
    }
  }

  getNotebookContext() {
    const notebook = this.notebook;
    if (!notebook) {
      return;
    }
    const cells = [];    
    for (var i = 0; i < notebook.model.cells.length; i++) {
      const cell = notebook.model.cells.get(i).toJSON();
      var outputText = "";
      if (cell.outputs.length > 0) {
        const traceback = cell.outputs[0].traceback;
        if (traceback != null) {
          for (var j = 0; j < traceback.length; j++) {
            const plainTextString = removeAnsiCodes(traceback[j]);
            outputText += plainTextString + "\n";
          }
        } else {
          outputText = removeAnsiCodes(cell.outputs[0].text);
        }
      }
      cells.push({"input": cell.source, "output": outputText});
    }
    const insertCellIndex = notebook.content.activeCellIndex;
    const context = {"cells": cells, "insertCellIndex": insertCellIndex};
    return context; 
  } 
}

async function executeSilentCode(kernel, code) {
  return new Promise(async (resolve, reject) => {
    try {
      console.log("Executing code silently:" + code);
      const executeFuture = kernel.requestExecute({ code, silent: false }); // set silent to false to receive IOPub messages
      let streamOutput = ''; // Variable to capture the stream output
      // Listen for IOPub messages
      executeFuture.onIOPub = (msg) => {
        // Check if the message is an execute result
        if (msg.header.msg_type === 'execute_result') {
          const resultData = msg.content.data;
          const resultText = resultData['text/plain'];
        }
        // Check if the message is a stream output (stdout or stderr)
        if (msg.header.msg_type === 'stream') {
          const resultText = msg.content.text;
          streamOutput += resultText; // Append the stream output to the variable
        }
      };
      // Wait for the execution to complete
      await executeFuture.done;
      // Resolve the Promise with the captured stream output
      resolve(streamOutput);
    } catch (error) {
      reject(error); // Reject the Promise with the error
    }
  });
}
function waitForNonNullVariable(reader, callback) {
  var variable = reader(); 
  if (variable !== null) {
    callback(variable);
  } else {
    setTimeout(function() {
      waitForNonNullVariable(reader, callback);
    }, 100); // Wait 1 second before checking again
  }
}

// This is a hack until we can figure out how to get jest tests working
function parsePath(pathName) {
  // N.B. Is this for JupyterHub?
  if (pathName.startsWith('/user/')) {
    const username = pathName.split('/')[2];
    if (username != null) {
      return `/user/${username}/roboweb-server-extension`;
    }
  }
  // Split the path
  const pathParts = pathName.split('/');
  // Get all parts of the path up to "lab"
  const labIndex = pathParts.indexOf('lab');
  console.log("labIndex: " + labIndex +"\n");
  const pathPartsToLab = pathParts.slice(0, labIndex);

  if (labIndex == -1) {
    // Since we didn't find lab path assuming its rooted at the base of the path
    return "/roboweb-server-extension";
  }

  // Add the extension path
  pathPartsToLab.push('roboweb-server-extension');
  // Rejoin the path
  return pathPartsToLab.join('/');  
}

function buildBaseUrl() {
  // N.B. the point of the indirection is to make it easy to inject values for windows.location.pathname
  // in the test.
  return parsePath(window.location.pathname)
}

function loadFlutterApp() {
  //detect if we are in jupyterhub 
  var baseUrl = buildBaseUrl();
  window.isJupyter = true;
  window.serviceWorkerVersion = "124778936";
  const flutter_script = document.createElement('script');
  const flutter_src = `${baseUrl}/flutter.js`;
  flutter_script.src = flutter_src;
  document.head.appendChild(flutter_script);
  
  flutter_script.onload = function() {
    _flutter.loader.loadEntrypoint({
      serviceWorker: {
        serviceWorkerVersion: serviceWorkerVersion,
      }
    }).then(function(engineInitializer) {
      waitForNonNullVariable(function() {return document.getElementById("assistant-panel")}, function (target) {
        engineInitializer.initializeEngine({
          hostElement: target,
        }).then(function(appRunner) {
          return appRunner.runApp();
        })
      }); 
      //if target is null sleep for 100 ms 
    });
  };
}

async function startDebugger(kernel) {
  const absoluteUrl = new URL(window.location.href);
  const url = absoluteUrl.origin + "/roboweb-server-extension/debugger.py";
  const response = await fetch(url);
  const debugger_code = await response.text();
  const execution_response = await executeSilentCode(kernel, debugger_code);
  console.log(execution_response);
}


function registerCommTarget(kernel) {
  kernel.registerCommTarget('debugger_comm_target', (comm, msg) => {
    console.log("Registered debugger_comm_target");
    comm.onMsg = (msg) => {
      // Handle the received message, execute your JavaScript function
      console.log('Message received from Python:', msg);
      logException(msg);
    };
  });
}

// Execute your JavaScript function
function logException(msg) {
  console.log('Executing JavaScript function with message:', msg);
  // Your JavaScript function implementation goes here
  window.lastMSG = msg; 
  window.lastContext = msg.content.data; 
}

function removeAnsiCodes(str) {
  return str.replace(/\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])/g, '');
}  

function getCellContent(cell) {
  var outputText = "";
  var cellJson = cell.model.toJSON();
  if (cellJson.outputs.length > 0) {
    outputText = removeAnsiCodes(cellJson.outputs[0].text);
  }
  // const outputJSON = cell.outputArea.model.toJSON();
  // if (outputJSON.length > 0) {
  //   const traceback = outputJSON[0].traceback;
  //   if (traceback != null) {
  //     for (var i = 0; i < traceback.length; i++) {
  //       const plainTextString = removeAnsiCodes(traceback[i]);
  //       outputText += plainTextString + "\n";
  //     }
  //   } else {
  //     if (outputJSON[0].text != null)
  //       outputText = removeAnsiCodes(outputJSON[0].text);
  //     else 
  //       console.log("NULL output: " + cell.model.value.text);
  //   }
  // }
  return {
    "input": cell.model.value.text,
    "output": outputText
  }
}

const plugin = {
    id: 'roboweb-extension',
    requires: [INotebookTracker, ICommandPalette, IThemeManager],
    activate: (app, tracker, palette, manager) => {
      console.log(
        'Roboweb extension activated v0.1'
      );
      window.notebookAPI = new NotebookAPI(manager, null);

      // track executions 
      NotebookActions.executed.connect(async (_, args) => {
        const { cell, notebook, success, error } = args;
        const { input, output}  = getCellContent(cell); 
        const cellIndex = notebook.widgets.indexOf(cell);
        if (!success && error.errorName != null && error.errorValue != null) {
          const {context , type} = window.lastContext; 
          const displayName = error.errorName+": "+error.errorValue; 
          console.log("Error: " + displayName);
          console.log("Context: " + context);
          console.log("Input: " + input);
          console.log("Output: " + output);
          if (input == null || output == null || context == null) {
            console.log("Null value detected");
          } else {
            window.autoPrompt(displayName, type, context, input, output.length < 2000 ? output : displayName, cellIndex);              
          }
        }  
      });


      manager.themeChanged.connect((_, args) => {
        if (window.enableThemeSync) {
          if (window.changeThemeFlutter != null)
            window.changeThemeFlutter(args.newValue);
        } else {
          window.enableThemeSync = true;
        }
      });
      tracker.widgetAdded.connect((sender, notebookPanel) => {
        console.log('A new notebook has been created:', notebookPanel);
        if (window.newChat != null)
          window.newChat();
      });
      app.shell.currentChanged.connect(function (_, args) {
          const oldWidget = args.oldValue;
          const newWidget = args.newValue;
          if (newWidget == null)
            return;
          window.newWidget = newWidget;
          if (newWidget.constructor.name == 'fe') {
            const notebook = newWidget;
            //expose API for the flutter app
            window.notebookAPI = new NotebookAPI(manager, notebook);
            window.notebook = notebook; 
            const sessionContext = notebook.sessionContext;
            if (sessionContext) {
                sessionContext.kernelChanged.connect((kernelArgs) => {                  
                    const kernel = sessionContext.session?.kernel;
                    if (kernel) {
                      console.log("starting debugger"); 
                      startDebugger(kernel);
                      registerCommTarget(kernel);
                    }
                });
            }
            notebook.content.activeCellChanged.connect(async (sender, cell) => {
              if (cell == null)
                return;
              const cellIndex = notebook.content.widgets.indexOf(cell);
              if (window.reloadNotebookContext != null)
                window.reloadNotebookContext();
            });
          } 
      });

      const widget = new AssistantSidebar();
      widget.node.style.minWidth = "450px";
      app.shell.add(widget, 'right', { rank: 0 });
    




      window.addEventListener('click', function(event) {
        const assistantPanelDiv = document.querySelector('#assistant-panel');
        if (!assistantPanelDiv.contains(event.target)) {
          if (window.removeFocus != null)
            window.removeFocus();
        }
      }, { passive: true });
            
      //embed flutter app 
      loadFlutterApp();
    },
    autoStart: true
};
export default plugin;

