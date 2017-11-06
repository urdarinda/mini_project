import docker
import threading
import time

class UpdateList(object):

    def __init__(self, dht, ip):

        thread = threading.Thread(target=self.run, args=(dht, ip))
        thread.daemon = True
        thread.start()

    def run(self, dht, ip):

        self.dht = dht
        self.ip = ip
        env = docker.from_env()
        while True:
            for image in env.images.list():
                
                image_name = str(image).split(':')[1].strip(" '")
                print(image_name)
                try:
                    if self.ip not in dht.ext_to_ip[image_name]:
                       dht.ext_to_ip[image_name] += [self.ip] 
                
                except KeyError:
                    dht.ext_to_ip[image_name] = [self.ip]

                print(dht.ext_to_ip[image_name])
            time.sleep(86400)
