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
dht_object = ImageDHT(sys.argv[1], int(sys.argv[2]),
                      (sys.argv[3], int(sys.argv[4])))

while True:
	
	query = input("Enter your query\n")
	print("1 for getting cpu usage of a node\n 2 for getting nodes having a particular image \n 3 to get all peers \n 6 to exit\n")
	query = int(query)

    query = int(input("Enter your query :"))

    if query == 1:
        key = input("Enter your key :") #enter the ip as key to get its cpu usage in the DHT
        dht_object.get_iptocpu(key)

    elif query == 2:
        key = input("Enter your key :") #enter the name of the image as the key to get the list of the nodes having the particular image in DHT
        dht_object.get_exttoip(key)

    elif query == 3: #this prints the list of the peers present in the DHT
        dht_object.get_peers()

    elif query == 4: #get all the nodes in the ip_to_cpu DHT
        dht_object.get_all_iptocpu()

    elif query == 5: #get all the nodes in the ext_to_ip DHT
        dht_object.get_all_exttoip()

    elif query == 6: #exit
        print("Bye Bye\n")
        exit()

    else: #handles the any other case.
        print("Invalid Input\n")
