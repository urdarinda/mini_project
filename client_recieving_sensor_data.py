import socket
import operator
import threading
import docker

new_dict = {}

class Client(threading.Thread):
	lock = threading.Lock()

	def __init__(self,connection,clientAddress):
		threading.Thread.__init__(self)
		self.conn = connection
		self.clientAddress = clientAddress

	def run(self):
		(ipOfClient,port) = self.clientAddress

		# while True:
			# filename = open("iplist.txt","w")
		data = self.conn.recv(10)
		data = str(data)
		data= data[2:-1]
		print(data)
		dockerClient=docker.from_env(version="auto");
		data="python /src/hello.py " + data
		#dockerClient.containers.run("bash","ls /tmp",volumes={'/home/urdarinda/':{'bind':'/tmp','mode':'ro'}})
		ans = dockerClient.containers.run(image="lol",command=data)
		print(ans)
		self.conn.send(ans)


sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverAddress=('',10027)
sock.bind(serverAddress)
sock.listen(10)
a=10
while a:
	a=a-1
	print("Waiting for Connections")
	connection,clientAddress = sock.accept()
	thread = Client(connection,clientAddress)
	thread.start()