const functions = require('firebase-functions');
const { onRequest } = require('firebase-functions/v2/https');

// Replace with your deployed Cloud Run URL
const flaskAppUrl = 'https://YOUR_CLOUD_RUN_URL';

exports.app = onRequest((req, res) => {
  const proxy = require('http-proxy-middleware');
  return proxy({ target: flaskAppUrl, changeOrigin: true })(req, res);
});
