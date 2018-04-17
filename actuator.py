import socket
import threading
import docker
import json
import time


class Actuator(threading.Thread):

    def __init__(self, connection, masterAddress):

        threading.Thread.__init__(self)
        self.conn = connection
        self.masterAddress = masterAddress

    def run(self):

        (ipOfMaster, port) = self.masterAddress
        data = self.conn.recv(200)
        decoded_data = json.loads(data.decode())
        #print("Working for ", ipOfMaster, "with data ", data)
        value = decoded_data["value"]
        timestamp = (float)(decoded_data["timestamp"])
        print(value)
        current_time = time.time()
        print(current_time)
        #if type(timestamp) == 'str':
        #    print("x") 
        #    #current_time = (float)current_time
        turn_around_time = current_time - timestamp
        print(turn_around_time)


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ActuatorAddress = ('', 10008)
sock.bind(ActuatorAddress)
sock.listen(10)

while True:
    # print("Waiting for Connections")
    connection, masterAddress = sock.accept()
    thread = Actuator(connection, masterAddress)
    thread.start()
