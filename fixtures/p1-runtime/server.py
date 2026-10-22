from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from pathlib import Path
VERSION = Path('/release.txt').read_text().strip()
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        status = 200 if self.path in ('/ready', '/business', '/wrong') else 404
        value = dict(ready=True, version=VERSION, value=0 if self.path == '/wrong' else 42)
        raw = json.dumps(value).encode()
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)
    def log_message(self, *args):
        pass
HTTPServer(('0.0.0.0', 8080), Handler).serve_forever()
