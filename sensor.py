#ip and port by command line inputs
import time
import socket
import sys
import ipaddress
import os
import random

# Connect the socket to the port where the server is listening
if(len(sys.argv)!=2):
	print("usage: "+sys.argv[0]+" %ip ")
	sys.exit(2)

# Create a TCP/IP socket
try:	
	ipaddress.ip_address(sys.argv[1])
	host=sys.argv[1]
	port=10003###hard coded port of connection to master @ 9997

except:
	print("usage: "+sys.argv[0]+" %ip")
	sys.exit(2)

try:
	while(True):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect((host,port))
		message = random.randint(0,99)
		message = str(message)
		print(message)
		sock.sendall(message.encode())
		time.sleep(1)
		sock.close()

finally:
    #print >> sys.stderr, 'closing socket'
    sock.close()
