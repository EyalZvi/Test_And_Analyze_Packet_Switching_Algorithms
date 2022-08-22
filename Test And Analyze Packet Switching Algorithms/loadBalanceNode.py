import http.server
import socketserver
import sys
import random

# choose server using Round Robin algorithm:
def RR(c, arr):
    n = c % 3
    return arr[n]

# Choose Random server:
def Random(arr):
    n = random.randint(0, 2)
    return arr[n]

# Choose server using WFQ algorithm:
def WFQ(arr):
    n = c % 6
    a=0
    if n < 3:
        a = 0

    elif n < 5:
        a = 1

    else:
        a = 2

    return arr[a]

# Class to handle requests:
class MyHandler(http.server.SimpleHTTPRequestHandler):
    arr = ["http://10.0.0.7:8080", "http://10.0.0.8:8080","http://10.0.0.9:8080"]

    def do_GET(self):
        global c
        self.send_response(301)
        add=""
        # Pick server for each request according to chosen algorithm:
        if (sys.argv[1] == "bal-RR"):
            add = RR(c, self.arr)
        elif (sys.argv[1] == "bal-RANDOM"):
            add = Random(self.arr)
        elif (sys.argv[1] == "bal-WFQ"):
            add = WFQ(self.arr)
        else:
            add = self.arr[0]
        c = c + 1
        # Send header to the chosen server:
        self.send_header('Location', add)
        self.end_headers()


c = 0

pywebserver = socketserver.TCPServer(("", 9090), MyHandler)

pywebserver.serve_forever()
