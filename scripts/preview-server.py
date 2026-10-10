from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os
os.chdir(Path(__file__).resolve().parents[1] / "_site")
class Handler(SimpleHTTPRequestHandler):
    def log_message(self, fmt, *args):
        if args and str(args[1]) != "200":
            super().log_message(fmt, *args)
print("Preview: http://127.0.0.1:4000/", flush=True)
ThreadingHTTPServer(("127.0.0.1", 4000), Handler).serve_forever()
