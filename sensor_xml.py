#ip and port by command line inputs
import time
import socket
import sys
import ipaddress
import os
import json
import random
from lxml import etree

# Connect the socket to the port where the server is listening
if(len(sys.argv)!=3):
	print("usage: "+sys.argv[0]+" %ip ,type ")
	sys.exit(2)

# Create a TCP/IP socket
try:	
	ipaddress.ip_address(sys.argv[1])
	host=sys.argv[1]
	port=10005###hard coded port of connection to master @ 9997

except:
	print("usage: "+sys.argv[0]+" %ip")
	sys.exit(2)

try:
	#while(True):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect((host,port))
			
		root = 	etree.Element('root')
		value = etree.Element('value')
		value.text = str(random.randint(0,99))
		data_type = etree.Element('type')
		data_type.text = 'temp'
		root.append(data_type)
		root.append(value)

		#message = {}
		#message["type"] = sys.argv[2]
		#message["value"] = random.randint(0,99)
		#encoded_data = json.dumps(message)

		encoded_data = etree.tostring(root,pretty_print=True)
		#print(encoded_data.decode())
		#print(type(encoded_data.decode()))

		#abc = etree.fromstring(encoded_data.decode())
		#print(abc[0].text)
		#print(abc[1].text)

		sock.sendall(encoded_data)
		time.sleep(1)
		sock.close()

finally:
	#print(1)
    print >> sys.stderr, 'closing socket'
    sock.close()
