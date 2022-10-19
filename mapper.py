from scapy.all import sr1, get_if_addr, conf, IP, ICMP, Ether
from scapy.layers.l2 import getmacbyip
from threading import Thread
from time import sleep
from ui import uprint

# manuf needs to be present in the directory
# https://gitlab.com/wireshark/wireshark/raw/master/manuf

manufacturers = {}
dump = [i.split('\t') for i in open("manuf", "r", encoding='utf-8').readlines()[65:]]
for i in dump:
    manufacturers[i[0]] = [(i[2] if len(i)>2 else i[1])]

class mapper:
    """
    class meant to scan for hosts with the ICMP protocol, resolve their mac adress and vendors
    the timeout is set to 0.2 but you might need to scale it up depending on how good the network is
    """

    def resolve_mac(self, ip):
        mac = getmacbyip(ip).upper()
        try:
            vendor = manufacturers[mac[0:8]][0]
        except:
            vendor = "unknown"
        return (mac,vendor)

    def ping(self,ip):
        self.runningthread.append(True)
        reply = sr1(IP(dst=str(ip), ttl=20)/ICMP(), timeout=self.TIMEOUT, verbose=0)
        if (reply is not None):
            self.netmap[ip]=self.resolve_mac(ip)
        self.runningthread.pop(0)

    def start(self):
        uprint("Starting new scan...\n")
        self.runningthread = []
        for ip in range(0, 256):
            Thread(target=self.ping, args=(f"{self.fargmented[0]}.{self.fargmented[1]}.{self.fargmented[2]}.{ip}",)).start()
            sleep(0.015) # Scapy doesn't seems to handle too much requests so I added a timeout to keep it as accurate as possible. I'll speed up the process later
    
    def get_info(self, index):
        count = -1
        for i in self.netmap:
            if count==index:
                return(i,self.netmap[i][0])
            count+=1

    def get_gateway(self):
        return self.netmap["gateway"],self.netmap[self.netmap["gateway"]][0]

    def __init__(self):
        self.netmap = {}
        self.netmap['you'] = get_if_addr(conf.iface)
        self.netmap['gateway'] = conf.route.route("0.0.0.0")[2]
        self.netmap[get_if_addr(conf.iface)] = (Ether().src.upper(),(manufacturers[Ether().src.upper()[0:8]][0] if (Ether().src.upper()[0:8] in manufacturers) else "unknown")) #building your own packet with scapy seems to revent you from pinging yourself so you'll automatically add youself this also be true if you try to ping your gateway
        self.fargmented = get_if_addr(conf.iface).split('.')
        self.TIMEOUT = 2
        self.runningthread = []

if __name__ == "__main__":
    map = mapper()
    map.start()
    print(map.netmap)


