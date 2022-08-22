import time


def testload(net, costs):
    serv1 = net.get("serv1")

    if costs == "eq":
        delays = 0.1
        dest_log = "Topo2/equal"
    else:
        delays = 0.3
        dest_log = "Topo2/unequal"
    print("--> Starting load with six clients - for testing performance under extensive load")
    # Starting Server:
    serv1.sendCmd(f'python3 ../server.py {delays} &')
    # Starting Load-Balancer:
    net.get("lb").sendCmd("python3 ../loadBalanceNode.py n &")
    # Starting Clients:
    net.get("c1").sendCmd(f"python3 ../client.py c1-max-load {dest_log} &")
    net.get("c2").sendCmd(f"python3 ../client.py c2-max-load {dest_log} &")
    net.get("c3").sendCmd(f"python3 ../client.py c3-max-load {dest_log} &")
    net.get("c4").sendCmd(f"python3 ../client.py c4-max-load {dest_log} &")
    net.get("c5").sendCmd(f"python3 ../client.py c5-max-load {dest_log} &")
    net.get("c6").sendCmd(f"python3 ../client.py c6-max-load {dest_log}")

    time.sleep(120)

    net.get("c1").monitor()
    net.get("c2").monitor()
    net.get("c3").monitor()
    net.get("c4").monitor()
    net.get("c5").monitor()
    net.get("c6").monitor()
    net.get("lb").monitor()

    print("--->Done")
    return


def testloadbal(net,algo,costs):
    serv1 = net.get("serv1")
    serv2 = net.get("serv2")
    serv3 = net.get("serv3")
    delays =[]
    if costs == "eq":
        delays = [0.1,0.1,0.1]
        dest_log = "Topo2/equal"
    else:
        delays = [0.1,0.2,0.3]
        dest_log = "Topo2/unequal"
    print(f"--Testing {algo} load balancing for six clients--")
    # Starting Servers:
    serv1.sendCmd(f'python3 ../server.py {delays[0]} &')
    serv2.sendCmd(f'python3 ../server.py {delays[1]} &')
    serv3.sendCmd(f'python3 ../server.py {delays[2]} &')
    # Starting Load-Balancer:
    net.get("lb").sendCmd(f"python3 ../loadBalanceNode.py bal-{algo} &")
    # Starting Clients:
    net.get("c1").sendCmd(f"python3 ../client.py c1-bal-{algo} {dest_log} &")
    net.get("c2").sendCmd(f"python3 ../client.py c2-bal-{algo} {dest_log} &")
    net.get("c3").sendCmd(f"python3 ../client.py c3-bal-{algo} {dest_log} &")
    net.get("c4").sendCmd(f"python3 ../client.py c4-bal-{algo} {dest_log} &")
    net.get("c5").sendCmd(f"python3 ../client.py c5-bal-{algo} {dest_log} &")
    net.get("c6").sendCmd(f"python3 ../client.py c6-bal-{algo} {dest_log}")

    time.sleep(45)

    net.get("c1").monitor()
    net.get("c2").monitor()
    net.get("c3").monitor()
    net.get("c4").monitor()
    net.get("c5").monitor()
    net.get("c6").monitor()
    net.get("lb").monitor()

    print("--->Done")
    return
