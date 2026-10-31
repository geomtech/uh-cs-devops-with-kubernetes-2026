
from http.server import HTTPServer, BaseHTTPRequestHandler

counter = 0


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        global counter

        if self.path != "/pingpong":
            self.send_error(404)
            return

        response = f"pong {counter}"
        counter += 1

        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(response.encode("utf-8"))


server = HTTPServer(("0.0.0.0", 3000), Handler)
server.serve_forever()
