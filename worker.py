import socket
import threading
import docker
import json


class Worker(threading.Thread):

    def __init__(self, connection, masterAddress):

        threading.Thread.__init__(self)
        self.conn = connection
        self.masterAddress = masterAddress

    def run(self):

        (ipOfMaster, port) = self.masterAddress
        data = self.conn.recv(200)
        decoded_data = json.loads(data.decode())
        print("Working for ", ipOfMaster, "with data ", data)
        image_name = decoded_data["type"]
        data_value = decoded_data["value"]
        docker_worker = docker.from_env(version="auto")
        data_arg = "python /src/hello.py " + str(data_value)
        ans = docker_worker.containers.run(image_name, data_arg, remove=True)
        # print(ans)
        self.conn.sendall(ans)


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
workerAddress = ('', 10002)
sock.bind(workerAddress)
sock.listen(10)

while True:
    # print("Waiting for Connections")
    connection, masterAddress = sock.accept()
    thread = Worker(connection, masterAddress)
    thread.start()
