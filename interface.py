from imagedht import ImageDHT
import sys

dht_object = ImageDHT(sys.argv[1], int(sys.argv[2]),
                      (sys.argv[3], int(sys.argv[4])))


while True:

    query = int(input("Enter your query :"))

    if query == 1:
        key = input("Enter your key :")
        dht_object.get_iptocpu(key)

    elif query == 2:
        key = input("Enter your key :")
        dht_object.get_exttoip(key)

    elif query == 3:
        dht_object.get_peers()

    elif query == 4:
        dht_object.get_all_iptocpu()

    elif query == 5:
        dht_object.get_all_exttoip()

    elif query == 6:
        print("Bye Bye\n")
        exit()

    else:
        print("Invalid Input\n")
