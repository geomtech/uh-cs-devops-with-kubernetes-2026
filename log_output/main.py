
import uuid
import time
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from datetime import datetime, timezone

random_id = str(uuid.uuid4())


def get_status():
    timestamp = datetime.now(timezone.utc).isoformat()
    return f"{timestamp}: {random_id}"


def log_status():
    while True:
        print(get_status(), flush=True)
        time.sleep(5)


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/":
            self.send_error(404)
            return

        response = get_status().encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)


threading.Thread(target=log_status, daemon=True).start()

server = ThreadingHTTPServer(("0.0.0.0", 3000), RequestHandler)
server.serve_forever()
