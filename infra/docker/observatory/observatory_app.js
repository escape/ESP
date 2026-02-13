/**
 * Minimal observatory service skeleton.
 * Dashboard + API for search/analysis/download.
 * To be developed: full dashboard UI and comprehensive API.
 */

const http = require('http');

const hostname = '0.0.0.0';
const port = 5173;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'application/json');
  
  if (req.url === '/health') {
    res.end(JSON.stringify({
      status: 'healthy',
      service: 'observatory'
    }));
  } else if (req.url === '/api/v1/') {
    res.end(JSON.stringify({
      message: 'Observatory API running',
      status: 'skeleton',
      version: '0.1.0',
      paths: ['/health', '/api/v1/search', '/api/v1/analysis', '/api/v1/download'],
      info: 'Dashboard + API for political influence data'
    }));
  } else {
    res.end(JSON.stringify({
      message: 'Observatory dashboard service',
      status: 'skeleton',
      version: '0.1.0',
      info: 'Access /health or /api/v1/ for endpoints'
    }));
  }
});

server.listen(port, hostname, () => {
  console.log(`Observatory service listening at http://${hostname}:${port}/`);
});
