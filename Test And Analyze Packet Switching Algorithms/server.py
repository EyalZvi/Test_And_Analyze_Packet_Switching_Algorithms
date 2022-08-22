import http.server
import socketserver
import sys
import time

# set delay from command-line argument:
delay = float(sys.argv[1])

# class for serving requests:
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def handle_one_request(self):
        time.sleep(delay)
        return http.server.SimpleHTTPRequestHandler.handle_one_request(self)


print("Serving local directory")
httpd = socketserver.TCPServer(("", 8080), MyHandler)

# serve forever:
while True:
    httpd.handle_request()
