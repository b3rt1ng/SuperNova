from scapy.all import sr1, get_if_addr, conf, IP, ICMP, Ether
from scapy.layers.l2 import getmacbyip
from threading import Thread
from time import sleep
from ui import uprint
import logging, resolver
logging.getLogger("scapy.runtime").setLevel(40)

# manuf needs to be present in the directory
# https://raw.githubusercontent.com/boundary/wireshark/master/manuf

class mapper:
    """
    class meant to scan for hosts with the ICMP protocol, resolve their mac adress and vendors
    the timeout is set to 1 but you might need to scale it up depending on how good the network is
    """

    def resolve_mac(self, ip, with_mac=False):
        if with_mac:
            mac = ip
        else:
            mac = getmacbyip(ip).upper()

        try:
            vendor = self.resolver.get_vendor(mac)
        except Exception as e:
            vendor = "unknown"
        return (mac,vendor)

    def ping(self,ip):
        self.runningthread.append(True)
        reply = sr1(IP(dst=str(ip), ttl=20)/ICMP(), timeout=self.TIMEOUT, verbose=0)
        if (reply is not None):
            self.netmap[ip]=self.resolve_mac(ip)
        try:
            self.runningthread.pop(0)
        except:
            uprint("Error while removing thread from list (should not be important)", char="?")

    def start(self, large = False, sleep_time = 0.015):
        uprint("Starting new scan...")
        if large:
            """
                implementing a scan that will be more specific to a network trunk
            """
            try:
                uprint("Minimal integer: ", same_line=True, char="?")
                minimal = int(input())
                uprint("Maximal integer: ", same_line=True, char="?")
                maximal = int(input())
                if minimal>maximal:
                    uprint("Minimal integer cannot be greater than maximal integer", char="!")
                    return
                for ip in range(minimal, maximal):
                    for ip2 in range(0, 256):
                        uprint(f"Started {int(((ip-minimal)+((ip2/256)*(maximal-minimal)))*100)}% of threads", same_line=True)
                        Thread(target=self.ping, args=(f"{self.fargmented[0]}.{self.fargmented[1]}.{ip}.{ip2}",)).start()
                        sleep(sleep_time)
            except KeyboardInterrupt:
                uprint("Aborting scan")
                sleep(2)
                return
        else:
            for ip in range(0, 256):
                uprint(f"Started {int((ip/255)*100)}% of threads", same_line=True) #comment this line if you wanna gain time
                Thread(target=self.ping, args=(f"{self.fargmented[0]}.{self.fargmented[1]}.{self.fargmented[2]}.{ip}",)).start()
                sleep(sleep_time)
                # Scapy doesn't seems to handle too much requests so I added a timeout to keep it as accurate as possible. I'll speed up the process later
                # the issue is that the socket library cannot handle too much file opening
                # https://stackoverflow.com/questions/2569620/socket-accept-error-24-to-many-open-files
                # this stackoverflow post suggest increasing the number of file you can open but i won't
                # do so if I can manage a "safer" way to fix the issue

    def get_info(self, index):
        count = -1
        for i in self.netmap:
            if count==index:
                return(i,self.netmap[i][0])
            count+=1

    def get_gateway(self):
        return self.netmap["gateway"],self.netmap[self.netmap["gateway"]][0]

    def isvalid(self, int_value):
        if 0<int_value<len(self.netmap)-1:
            return True
        return False

    def __init__(self):
        self.resolver = resolver.vendor_resolver()
        self.netmap = {}
        self.netmap['you'] = get_if_addr(conf.iface)
        self.netmap['gateway'] = conf.route.route("0.0.0.0")[2]
        self.netmap[get_if_addr(conf.iface)] = (self.resolve_mac(Ether().src.upper(), with_mac=True)) #building your own packet with scapy seems to revent you from pinging yourself so you'll automatically add youself this also be true if you try to ping your gateway
        self.fargmented = get_if_addr(conf.iface).split('.')
        self.TIMEOUT = 2
        self.runningthread = []

if __name__ == "__main__":
    map = mapper()
    map.start()
    print(map.netmap)   


