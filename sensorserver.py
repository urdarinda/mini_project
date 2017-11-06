"""Sensor servers

The sensors are connected to this node. It will collect data and send them
to the appropriate node for processing.
"""

import socket
import threading
import sys
import time
import os
import json
from imagedht import ImageDHT
from exttoip import ExtToIP


class SensorServer(threading.Thread):
    lock = threading.Lock()

    def __init__(self, connection, sensorAddress):
        threading.Thread.__init__(self)
        self.conn = connection
        self.sensorAddress = sensorAddress

    def run(self):
        (ipOfSensor, port) = self.sensorAddress

        # while True:
        print("Received data from sensor ")
        data = self.conn.recv(50)
        # print(port,ipOfSensor)
        data = json.loads(data.decode())
        print((data), data["type"], data["value"])
        ipOfWorker = ExtToIP(dht, data).getbest()
        print(ipOfWorker)
        # portOfWorker = 10002
        # workerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # workerAddress = (ipOfWorker, portOfWorker)
        # workerSock.connect(workerAddress)
        # workerSock.send(data)
        # retanswer = workerSock.recv(10)
        # print("hello")
        # print(retanswer)


class Updateload():

    def __init__(self):
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    @staticmethod
    def run():
        while True:
            cpu_avg = os.getloadavg()[0]
            dht.ip_to_cpu[sys.argv[1]] = cpu_avg
            time.sleep(5)


if __name__ == "__main__":

    if(len(sys.argv) < 2):
        print("usage: " + sys.argv[0] + " %ip [port] [seedip seedport]")
        sys.exit(2)

    ipaddress = sys.argv[1]
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 12550
    seeed = tuple([sys.argv[3], sys.argv[4]]) if len(sys.argv) > 4 else ()
    dht = ImageDHT(ipaddress, port, seeed)
    dht.ip_to_cpu['aa'] = 5
    print(dht.ip_to_cpu['aa'])
    dht.ext_to_ip["temp"] = ['172.31.80.240', '172.31.81.241']
    dht.ext_to_ip["hum"] = ['172.31.80.240']
    dht.ip_to_cpu['172.31.81.241'] = 5
    updateload = Updateload()

    #while True:
     #   print (dht.ip_to_cpu[sys.argv[1]])
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('', 10004)
    sock.bind(server_address)
    sock.listen(10)

    while True:
        print("Waiting for Sensor Data")
        connection, sensorAddress = sock.accept()
        thread = SensorServer(connection, sensorAddress)
        thread.start()
