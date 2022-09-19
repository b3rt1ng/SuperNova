from scapy.all import *
from threading import Thread
from time import sleep

class mapper:
    """
    class meant to scan for hosts with the ICMP protocol
    the timeout is set to 0.2 but you might need to scale it up
    """
    def __init__(self):
        self.netmap = []
        self.TIMEOUT = 0.2

    def ping(self,ip):
        reply = sr1(IP(dst=str(ip), ttl=20)/ICMP(), timeout=self.TIMEOUT, verbose=0)
        if (reply is not None):
            self.netmap.append(ip)

    def start(self):
        for ip in range(0, 256):
            Thread(target=self.ping, args=("192.168.1."+str(ip),)).start()
            sleep(0.01) # Scapy doesn't seems handle too much requests so i added a timeout  

if __name__ == "__main__":
    map = mapper()
    map.start()
    print(map.netmap)
