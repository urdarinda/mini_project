import socket
import time
import sys
import ipaddress
import os

if(len(sys.argv)!=2):
	print("usage: "+sys.argv[0]+" %ip")
	sys.exit(2)

try:
	ipaddress.ip_address(sys.argv[1])
	host=sys.argv[1]
	port=10001

except:
	print("usage: "+sys.argv[0]+" %ip")
	sys.exit(2)

tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClient.connect((host, port))

while True:
	cpuAvg = str(os.getloadavg()[0])
	tcpClient.sendall(cpuAvg.encode())
	time.sleep(5)

tcpClient.close()
