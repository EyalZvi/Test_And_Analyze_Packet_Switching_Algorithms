import requests
import sys


i = 50 # set num of requests

# open log file:
f = open(f"../log/{str(sys.argv[2])}/log-" + sys.argv[1] + ".txt", "a")

# send requests and write response time to log file:
while i > 0:
    x = requests.get('http://10.0.0.10:9090')
    print(x)
    f.write(str(x.elapsed.total_seconds())+"\n")
    i = i - 1
