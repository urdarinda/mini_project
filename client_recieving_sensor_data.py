import socket
import threading
import docker

new_dict = {}

class Worker(threading.Thread):
	lock = threading.Lock()

	def __init__(self,connection,masterAddress):
		threading.Thread.__init__(self)
		self.conn = connection
		self.masterAddress = masterAddress

	def run(self):
		(ipOfMaster,port) = self.masterAddress

		# while True:
			# filename = open("iplist.txt","w")
		data = self.conn.recv(10)
		data = str(data)
		data= data[2:-1]
		print(data)
		dockerWorker=docker.from_env(version="auto");
		data="python /src/hello.py " + data
		#dockerClient.containers.run("bash","ls /tmp",volumes={'/home/urdarinda/':{'bind':'/tmp','mode':'ro'}})
		ans = dockerWorker.containers.run(image="lol",command=data)
		print(ans)
		self.conn.send(ans)


sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
workerAddress=('',20001)
sock.bind(workerAddress)
sock.listen(10)

while True:
	print("Waiting for Connections")
	connection,masterAddress = sock.accept()
	thread = Worker(connection,masterAddress)
	thread.start()