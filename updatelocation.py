import docker
import threading
import time


class UpdateLocation(object):

    def __init__(self, dht, ip):
        self.dht = dht
        self.ip = ip
        file = open("loc.txt")
        while True:
            x = file.readline()
            if x:
                self.dht.loc_to_ip[x.split()[0]] = x.split()[1:]
            else:
                break  
