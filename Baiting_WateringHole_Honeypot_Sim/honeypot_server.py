import datetime
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

LOG = []


class HoneyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        entry = {
            "time": str(datetime.datetime.now()),
            "ip": self.client_address[0],
            "path": self.path,
            "agent": self.headers.get("User-Agent", "?"),
        }
        LOG.append(entry)
        print(json.dumps(entry))
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Thanks for visiting!")

    def log_message(self, *args):
        pass  # suppress default logs


print("Honeypot on http://localhost:8080")
HTTPServer(("", 8080), HoneyHandler).serve_forever()
