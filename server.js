'use strict';

const http = require('http');
const fs = require('fs');
const path = require('path');

const root = __dirname;
const port = Number(process.env.PORT) || 8080;
const cleanRoutes = {
  '/blog/construction-and-infrastructure-development-lubumbashi': 'congo-prime-construction-and-infrastructure-development-lubumbashi.html',
  '/blog/emerging-housing-design-trends-kolwezi': 'congo-prime-emerging-housing-design-trends-kolwezi.html',
  '/blog/10-points-designing-home-interior': 'congo-prime-10-points-designing-home-interior.html',
  '/blog/building-solid-ground-land-acquisition-permits-haut-katanga': 'congo-prime-building-solid-ground-land-acquisition-permits-haut-katanga.html',
  '/blog/engineering-katanga-homes-defeat-wet-season': 'congo-prime-engineering-katanga-homes-defeat-wet-season.html'
};
const legacyRoutes = {
  '/10-points-blog.html': '/blog/10-points-designing-home-interior',
  '/congo-prime-infrastructure-blog-updated.html': '/blog/construction-and-infrastructure-development-lubumbashi',
  '/congo-prime-kolwezi-housing-blog-updated.html': '/blog/emerging-housing-design-trends-kolwezi',
  '/land-acquisition-and-construction-permits-haut-katanga.html': '/blog/building-solid-ground-land-acquisition-permits-haut-katanga',
  '/residential-structural-engineering-greater-katanga.html': '/blog/engineering-katanga-homes-defeat-wet-season'
};
const contentTypes = {
  '.css': 'text/css; charset=utf-8',
  '.html': 'text/html; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.svg': 'image/svg+xml',
  '.webp': 'image/webp',
  '.woff': 'font/woff',
  '.woff2': 'font/woff2',
  '.ttf': 'font/ttf',
  '.xml': 'application/xml; charset=utf-8'
};

function sendFile(response, relativePath) {
  const filePath = path.resolve(root, relativePath);
  if (!filePath.startsWith(root + path.sep) && filePath !== root) {
    response.writeHead(403);
    response.end('Forbidden');
    return;
  }

  fs.stat(filePath, (error, stats) => {
    if (error || !stats.isFile()) {
      response.writeHead(404);
      response.end('Not found');
      return;
    }

    response.writeHead(200, {
      'Content-Type': contentTypes[path.extname(filePath).toLowerCase()] || 'application/octet-stream'
    });
    fs.createReadStream(filePath).pipe(response);
  });
}

http.createServer((request, response) => {
  const pathname = decodeURIComponent(new URL(request.url, `http://${request.headers.host}`).pathname);

  if (legacyRoutes[pathname]) {
    response.writeHead(301, { Location: legacyRoutes[pathname] });
    response.end();
    return;
  }

  if (cleanRoutes[pathname]) {
    sendFile(response, cleanRoutes[pathname]);
    return;
  }

  sendFile(response, pathname === '/' ? 'index.html' : pathname.replace(/^\/+/, ''));
}).listen(port, () => {
  console.log(`Congo Prime local server: http://127.0.0.1:${port}`);
});
