import time
import socket
import sys
import psutil
import random

# Create a gTCP/IP socket


# Connect the socket to the port where the server is listening
server_address = ("172.31.132.89", 10003)
#print >> sys.stderr, 'connecting to %s port %s' % server_address


try:
	while(True):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect(server_address)
		message = random.randint(0,99)
		message = str(message)
		print(message)
		sock.sendall(message.encode())
		time.sleep(1)
		sock.close()

finally:
    #print >> sys.stderr, 'closing socket'
    sock.close()
