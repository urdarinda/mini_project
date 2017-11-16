'''Extension to IP

Returns the best node (minimum cpu usage) having the particular image at its location.

'''
class ExtToIP:

    def __init__(self, dht, data):
        '''
            constructor of this class.It initialises the DHT and data object passed to it. 
        '''

        self.dht = dht
        self.data = data

    def getbest(self):
        '''
            function to return the best node present in the DHT for computation of the data.
        '''

        try:

            iplist = self.dht.ext_to_ip[self.data["type"]]
            ''' gets the list of the nodes having the image(image name is data["type"]) at its location in a varaible
                name iplist from the DHT(ext_to_ip)            
            '''
            bestnode = iplist[0]
            cur = 100
            for node in iplist:
                usage = self.dht.ip_to_cpu[node]
                if usage < cur:
                    cur = usage
                    bestnode = node
            return bestnode # returns the best node

        except:
            raise KeyError
            """TODO DOWNLOAD DOCKER IMAGE ON THE SAME SYSTEM AND DEPLOY"""
