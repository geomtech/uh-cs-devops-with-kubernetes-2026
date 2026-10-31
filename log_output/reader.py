
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path

output_file = Path("/data/output.txt")


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/":
            self.send_error(404)
            return

        try:
            content = output_file.read_bytes()
        except FileNotFoundError:
            self.send_error(503, "Waiting for writer")
            return

        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)


server = HTTPServer(("0.0.0.0", 3000), Handler)
server.serve_forever()
