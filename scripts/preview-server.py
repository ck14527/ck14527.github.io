from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlsplit
import os
os.chdir(Path(__file__).resolve().parents[1] / "_site")
class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/kangchen.github.io"):
            self.path = self.path[len("/kangchen.github.io"):] or "/"
        super().do_GET()
    def log_message(self, fmt, *args):
        if args and str(args[1]) != "200":
            super().log_message(fmt, *args)
print("Preview: http://127.0.0.1:4000/kangchen.github.io/", flush=True)
ThreadingHTTPServer(("127.0.0.1", 4000), Handler).serve_forever()
