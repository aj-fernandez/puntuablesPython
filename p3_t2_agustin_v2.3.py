# @author: ajfernandez
# @last_edited: 29/01/19
# @repo: https://github.com/aj-fernandez/

import socket
import os

os.system("clear")

listClosed = [] # store closed ports

remoteNode = input("Set a valid target [domain or ip]: ")
startPort = int(input("Set a valid start port: "))
endPort = int(input("Set a valid end port: "))+1
target = socket.gethostbyname(remoteNode)
print ("\n")

for port in range(startPort,endPort):  
    sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sc.settimeout(0.2)
    conn = sc.connect_ex((remoteNode, port))
    if conn == 0:
        print ("[+] Port {}: OPEN".format(port))
        sc.close()
    else:
        listClosed.append(port)
print ("\n")

pPort = min(listClosed) # previous port (answer the question: is consecutive?)
rangeClosed = [] # store -ranges- of consecutive ports

for port in listClosed:
    if port != pPort+1:
        rangeClosed.append([port])
    elif len(rangeClosed[-1]) > 1:
        rangeClosed[-1][-1] = port
    else:
        rangeClosed[-1].append(port)
    pPort = port

for portCluster in rangeClosed:
    if len(portCluster) == 1:
        print("[-] {}: CLOSED PORT".format(portCluster))
    else:
        print("[-] {}: CLOSED RANGE".format(portCluster))