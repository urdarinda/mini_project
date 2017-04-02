import socket
import threading

new_dict = {}

class Master(threading.Thread):
	lock = threading.Lock()

	def __init__(self,connection,sensorAddress):
		threading.Thread.__init__(self)
		self.conn = connection
		self.sensorAddress = sensorAddress

	def run(self):
		(ipOfSensor,port) = self.sensorAddress

		while True:
			print("Received data from sensor ")
			data = self.conn.recv(10)
			print(str(data))
			filename = open("iplist.txt","r")
			line = filename.readline()
			line = line.split()

			if len(line) > 0:
				ipOfWorker = line[0]
				print(ipOfWorker)
				#iptosend = "172.31.84.177"
				portOfWorker = 20001
				workerSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
				workerAddress = (ipOfWorker,portOfWorker)
				workerSock.connect(workerAddress)
				workerSock.send(data)
				retanswer=workerSock.recv(10)
				print("hello")
				print(retanswer)

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address=('',9997)
sock.bind(server_address)
sock.listen(10)

while True:
	print("Waiting for Sensor Data")
	connection,sensorAddress = sock.accept()
	thread = Master(connection,sensorAddress)
	thread.start()