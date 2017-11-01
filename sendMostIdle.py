import socket
import operator
import threading

new_dict = {}

class Client(threading.Thread):
	lock = threading.Lock()

	def __init__(self,connection,clientAddress):
		threading.Thread.__init__(self)
		self.conn = connection
		self.clientAddress = clientAddress

	def run(self):
		(ipOfClient,port) = self.clientAddress

		filename = open("iplist.txt","r")
		line= filename.readline().split()
		print(line[0])
		
		self.conn.send(line[0].encode())
		self.conn.close()


sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverAddress=('',10010)
sock.bind(serverAddress)
sock.listen(10)

while True:
	print("Waiting for Connections")
	connection,clientAddress = sock.accept()
	thread = Client(connection,clientAddress)
	thread.start()