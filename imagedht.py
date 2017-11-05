"""kad dht server

The dht will store the image and the list of nodes where the image lies.
"""
from kad import DHT


class ImageDHT(object):
    """Store the list of resources in a DHT."""

    def __init__(self, ip, port=12550, seed=()):
        """Constructor.

        A DHT is created based on the arguments.By default this is the first
        node of the DHT.If a tuple is provided, it is used as seed.

        Args:
            ip (ipaddress): IP address of the dht node.
            port (int): Port of the dht node (default 12550).
            seed (tuple): A single ip address along with port (default empty)

        """
        self.ip = ip
        self.port = port
        self.seed = seed
        if not seed:
            self.ip_to_cpu = DHT(self.ip, self.port)
            self.ext_to_ip = DHT(self.ip, self.port + 1)
        else:
            self.ip_to_cpu = DHT(self.ip, self.port, seeds=[seed])
            self.ext_to_ip = DHT(self.ip, self.port + 1, seeds=[seed])
