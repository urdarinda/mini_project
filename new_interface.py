'''Interface for the system
This file provides a way to get information about the DHT.
a)The cpu usage of a particular node in DHT
b)The list of nodes having a particular image in DHT
c)list all the peers
'''
from imagedht import ImageDHT
import sys

'''
four arguments are your ip, your port, the ip of the node you are connecting to and its port.
'''

class UIHandler:

    def __init__(self,argv1,argv2,argv3,argv4):
        self.dht_object = ImageDHT(argv1, int(argv2),( argv3, int(argv4)))
        print ('s')

    def extract_info(self,number,query):
        number = int(number)

        if number == 1:
            # enter the ip as key to get its cpu usage in the DHT
            return self.dht_object.get_iptocpu(query)

        elif number == 2:
            # enter the name of the image as the key to get the list of the nodes having the particular image in DHT
            return self.dht_object.get_exttoip(query)

        elif number == 3:  # this prints the list of the peers present in the DHT
            return self.dht_object.get_peers()

        '''
        elif query == 4:  # get all the nodes in the ip_to_cpu DHT
            dht_object.get_all_iptocpu()

        elif query == 5:  # get all the nodes in the ext_to_ip DHT
            dht_object.get_all_exttoip()
        '''
