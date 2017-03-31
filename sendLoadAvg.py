import socket 
import time
import sys
import ipaddress
import os

if(len(sys.argv)!=3):
	print("usage: "+sys.argv[0]+" %ip %port[>1024]")
	sys.exit(2)

try:
	ipaddress.ip_address(sys.argv[1])
	host=sys.argv[1]
	if(1024 <= int(sys.argv[2]) <= 65535):
		port = int(sys.argv[2])
	else:
		  raise Exception('Bad port')

except:
	print("usage: "+sys.argv[0]+" %ip %port[>1024]")
	sys.exit(2)

	
#BUFFER_SIZE = 10 
tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientA.connect((host, port))
 
while True: 
	cpuAvg = os.getloadavg()[0]
	#print(MESSAGE)
	tcpClientA.sendall(str(cpuAvg).encode())
	time.sleep(5)     
 
tcpClientA.close() 