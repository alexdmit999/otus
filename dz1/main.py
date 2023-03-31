from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
from urllib.parse import urlparse


class HttpGetHandler(BaseHTTPRequestHandler):
    """Обработчик с реализованным методом do_GET."""

    def do_GET(self):
        parsed = urlparse(self.path).path
        if parsed in ['/health', '/health/']:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.send_header("status", "OK")
            self.end_headers()
            self.wfile.write('{"status": "OK"}'.encode())
        else:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write('Hello, world!'.encode())


def run(server_class=HTTPServer, handler_class=HttpGetHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()


if __name__ == '__main__':
    run()
