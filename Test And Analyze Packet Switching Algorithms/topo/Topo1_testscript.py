import os
import time

if __name__ == '__main__':
    os.system("sudo mn -c")
    os.system("sudo python3 Topo1.py bal-RR uneq")
    os.system("sudo mn -c")
    os.system("sudo python3 Topo1.py bal-WFQ uneq")
    os.system("sudo mn -c")
    os.system("sudo python3 Topo1.py bal-RAND uneq")
    os.system("sudo mn -c")
    os.system("sudo python3 Topo1.py max-load uneq")
    os.system("sudo mn -c")
    os.system("sudo python3 Topo1.py bal-RR eq")
    os.system("sudo mn -c")
    os.system("sudo python3 Topo1.py bal-WFQ eq")
    os.system("sudo mn -c")
    os.system("sudo python3 Topo1.py bal-RAND eq")
    os.system("sudo mn -c")
    os.system("sudo python3 Topo1.py max-load eq")
    os.system("sudo mn -c")
