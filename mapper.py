from scapy.all import sr1, get_if_addr, conf, IP, ICMP
from scapy.layers.l2 import getmacbyip
from threading import Thread
from time import sleep

# manuf needs to be present in the directory
# https://gitlab.com/wireshark/wireshark/raw/master/manuf

manufacturers = {}
dump = [i.split('\t') for i in open("manuf", "r").readlines()[65:]]
for i in dump:
    manufacturers[i[0]] = [i[1]]

class mapper:
    """
    class meant to scan for hosts with the ICMP protocol, resolve their mac adress and vendors
    the timeout is set to 0.2 but you might need to scale it up depending on how good the network is
    """
    def __init__(self):
        self.netmap = {}
        self.netmap['you'] = get_if_addr(conf.iface)
        self.netmap['gateway'] = conf.route.route("0.0.0.0")[2]
        self.fargmented = get_if_addr(conf.iface).split('.')
        self.TIMEOUT = 0.2

    def resolve_mac(self, ip):
        mac = getmacbyip(ip).upper()
        try:
            vendor = manufacturers[mac[0:8]][0]
        except:
            vendor = "unknown"
        return (mac,vendor)

    def ping(self,ip):
        reply = sr1(IP(dst=str(ip), ttl=20)/ICMP(), timeout=self.TIMEOUT, verbose=0)
        if (reply is not None):
            self.netmap[ip]=self.resolve_mac(ip)

    def start(self):
        for ip in range(0, 256):
            Thread(target=self.ping, args=(f"{self.fargmented[0]}.{self.fargmented[1]}.{self.fargmented[2]}.{ip}",)).start()
            sleep(0.01) # Scapy doesn't seems to handle too much requests so I added a timeout to keep it as accurate as possible. I'll speed up the process later

if __name__ == "__main__":
    map = mapper()
    map.start()
    print(map.netmap)


