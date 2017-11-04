"""Send cpu load average to the server every n seconds."""

import socket
import time
import sys
import ipaddress
import os
import threading


class SendLoadAvg(object):
    """Send load average to server.

    A thread in the background starts the run method
    """

    def __init__(self, server_ip, server_port=10001, n=5):
        """Constructor.

        A daemon thread is created in the background which sends the cpu load
        average to the server every n seconds

        Args:
                server_ip (ipaddress): IP address of the server to send usage
                server_port (int): Port of the server (default 10001)
                n (int): Send cpu usage every `n` secs (default 5)

        """
        self.server_ip = server_ip
        self.server_port = server_port
        self.n = n
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        """Connect and send cpu usage to the server."""
        serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serv_sock.connect((self.server_ip, self.server_port))
        while True:
            cpu_avg = str(os.getloadavg()[0])
            serv_sock.sendall(cpu_avg.encode())
            time.sleep(self.n)


if __name__ == "__main__":

    if(len(sys.argv) < 2):
        print("usage: " + sys.argv[0] + " %ip [port] [interval]")
        sys.exit(2)
    ipaddress.ip_address(sys.argv[1])
    host = sys.argv[1]
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 10001
    n = int(sys.argv[3]) if len(sys.argv) > 3 else 5
    SendLoadAvg(host, port, n)
    while True:
        pass
