import csv
import matplotlib.pyplot as plt
import numpy as np

# Fucntion gets data array for a given test, opens the
# relevant log files, and adds data to array:
def calculate_data(topo_name,topo_type,num_clients,exp_name,data_array):
    for i in range(1, num_clients+1):
        fload = open(f"./log/{topo_name}/{topo_type}/log-c"+str(i)+f"-{exp_name}.txt")
        j = 0
        for row in csv.reader(fload):
            data_array[j] += float(row[0])*1000
            j = j + 1
    return data_array
# Function gets experiment information, calculates 
# data and average for each response and plots it.
def plot_test(topo_name,topo_type,num_clients,num_req,title):
    # Initialize data:
    data = []
    max_load = [0] * num_req
    bal_RR = [0] * num_req
    bal_RAND = [0] * num_req
    bal_WFQ = [0] * num_req
    # Calculate data:
    max_load = calculate_data(topo_name,topo_type,num_clients,"max-load",max_load)
    bal_RR = calculate_data(topo_name,topo_type,num_clients,"bal-RR",bal_RR)
    bal_RAND = calculate_data(topo_name,topo_type,num_clients,"bal-RANDOM",bal_RAND)
    bal_WFQ = calculate_data(topo_name,topo_type,num_clients,"bal-WFQ",bal_WFQ)
    # Calculate average for each client:
    for i in range(0, num_req):
        max_load[i] = max_load[i]/num_clients
        bal_RR[i] = bal_RR[i]/num_clients
        bal_RAND[i] = bal_RAND[i]/num_clients
        bal_WFQ[i] = bal_WFQ[i]/num_clients

    data.append(max_load)
    data.append(bal_RR)
    data.append(bal_RAND)
    data.append(bal_WFQ)


    # plotting graph
    x = np.linspace(0, len(data[0]), len(data[0]))
    a = plt.figure()
    for i in data:
        plt.plot(x, i)

    plt.legend([f'Max-Load - Avg: {round(sum(max_load)/num_req,2)}', f'Round Robin - Avg: {round(sum(bal_RR)/num_req,2)}',
                f'Random - Avg: {round(sum(bal_RAND)/num_req,2)}',f'WFQ - Avg: {round(sum(bal_WFQ)/num_req,2)}'],loc='upper right', prop={'size': 6})
    plt.xlabel("Number of Requests")
    plt.ylabel("Average Response Time (ms)")
    a.suptitle(title)
    a.savefig(f"./results/{topo_name}_{topo_type}.png")

if __name__ == '__main__':
    plot_test("Topo1","equal",3,50,"Topology 1 - 3 clients vs 3 equal servers")
    plot_test("Topo1","unequal",3,50,"Topology 1 - 3 clients vs 3 unequal servers")
    plot_test("Topo2","equal",6,50,"Topology 2 - 6 clients vs 3 equal servers")
    plot_test("Topo2","unequal",3,50,"Topology 2 - 6 clients vs 3 unequal servers")

