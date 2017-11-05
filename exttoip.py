
class ExtToIP:

    def __init__(self, dht, data):

        self.dht = dht
        self.data = data

    def getbest(self):
        try:
            iplist = self.dht.ext_to_ip[self.data["type"]]
            bestnode = iplist[0]
            cur = 100
            for node in iplist:
                usage = self.dht.ip_to_cpu[node]
                if usage < cur:
                    cur = usage
                    bestnode = node
            return bestnode

        except:
            pass
            """TODO DOWNLOAD DOCKER IMAGE ON THE SAME SYSTEM AND DEPLOY"""
