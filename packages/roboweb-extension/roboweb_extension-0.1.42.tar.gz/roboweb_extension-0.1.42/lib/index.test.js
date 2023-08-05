
/**
 * @packageDocumentation
 * @module roboweb-extension
 */

// TODO(jeremy): The test is currently broken because the imports don't work.
// Not sure how to fix that. During development I commented it out and copied the code 
// for parsePath from index.js to index.test.js
const { parsePath } = require('./index'); 

test('myFunction returns the expected value', () => {
  expect(parsePath("/lab/tree/git_roboweb/kaas/setup.ipynb")).toBe("/roboweb-server-extension");
  expect(parsePath("/notebook/kubeflow-user/jlewi/lab")).toBe("/notebook/kubeflow-user/jlewi/roboweb-server-extension");
  expect(parsePath("/notebook/kubeflow-user/jlewi/lab/workspaces/auto-L/tree/Untitled1.ipynb")).toBe("/notebook/kubeflow-user/jlewi/roboweb-server-extension");
  expect(parsePath("/some/other/path")).toBe("/roboweb-server-extension");
});
