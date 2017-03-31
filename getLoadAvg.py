import time
import socket
import sys
import os
import operator
import threading

new_dict = {}

class Client(threading.Thread):
	lock = threading.Lock()

	def __init__(self,connection,client_address): 
		threading.Thread.__init__(self) 
		self.conn = connection
		self.clientaddress = client_address
 
	def run(self): 
		(ipofclient,port) = self.clientaddress
		
		while True:
			filename = open("/home/jarvis/Documents/Docker/out.txt","w")
			data = self.conn.recv(10)
			if str(data) == "b''":
				data = "100"
				new_dict[ipofclient] = data
				Client.lock.acquire()
				print(len(new_dict))
				sorted_dict = sorted(new_dict.items(), key=operator.itemgetter(1))
				for key,value in sorted_dict:
					filename.write(key + " " + value + "\n")
				Client.lock.release()
				break

			data = str(data)
			data = data[2:-1]
			print(ipofclient + " " + data)
			
			new_dict[ipofclient]=data

			Client.lock.acquire()
			print(len(new_dict))
			sorted_dict = sorted(new_dict.items(), key=operator.itemgetter(1))
			for key,value in sorted_dict:
				filename.write(key + " " + value + "\n")
			Client.lock.release()	
		
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address=("172.31.132.88",9994)
sock.bind(server_address)
sock.listen(10)

while True:
	print("Waiting for Connections")
	connection,client_address = sock.accept()
	thread = Client(connection,client_address)		
	thread.start()
	
