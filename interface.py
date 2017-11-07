from imagedht import ImageDHT
import sys

dht_object = ImageDHT(sys.argv[1],int(sys.argv[2]),(sys.argv[3],int(sys.argv[4])))

while True:
	
	query = input("Enter your query\n")
	query = int(query)

	if query == 1:
		key = input("Enter your key\n")
		dht_object.get_item_iptocpu(key)

	elif query == 2:
		key = input("Enter your key\n")
		dht_object.get_item_exttoip(key)

	elif query == 3:
		dht_object.get_peers()

	elif query == 4:
		dht_object.get_all_keys_iptocpu()

	elif query == 5:
		dht_object.get_all_keys_exttoip()
	
	elif query == 6:
		print("Bye Bye\n")
		exit()

	else:
		print("Invalid Input\n")
