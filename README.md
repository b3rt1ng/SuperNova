<h1 align="center">
  <img
     src="https://img.shields.io/badge/Python%20Version-3.10-yellow"
     alt="python version">
  <img
     src="https://img.shields.io/badge/Linux-%E2%9C%94-purple"
     alt="working on linux">
  <img
     src="https://img.shields.io/badge/Windows-%E2%9C%94-red"
     alt="working on windows">
  <img
     src="https://img.shields.io/badge/OSX-maybe%20one%20day,%20who%20knows-blue"
     alt="not tested on osx">
  <br>
  🌌SuperNova🌌
  <br>
</h1>

<h4 align="center">Performs a man in the middle with ease (and <a href="https://github.com/secdev/scapy" target="_blank">Scapy</a>)</h4>


<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#download-manually">Download manually</a> •
  <a href="#how-does-it-work">How does it work</a><br>
  <img src="https://i.imgur.com/gVoBKLC.png" alt="Screenshot of the main UI">
</p>

## Key Features

* Network Scan - Scan on your network to find all the devices connected to it
  - Displays the IP, MAC, Vendor name and the hostname of the device
* ARP poisoning - Perform an ARP poisoning attack on the target and the router to put yourself in between
  - Choose a device to poison
  - Launch the attack
  - That's it !

## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com) installed on your computer and [Python 3.10](https://www.python.org/) or higher.  From your command line:

```bash
# Clone this repository
$ git clone https://github.com/b3rt1ng/SuperNova

# Go into the repository
$ cd SuperNova

# grant execution rights to the install script or simply run it with SU rights
$ chmod +x install.sh
$ ./install.sh

# Run the app with SU rights
$ sudo python3 supernova.py
```

> **Note**
> The install file might not need the execution rights, but the main script does.


## Download manually

Download scapy from [here](https://scapy.net/download/)  
Download the manufacutrer database from [here](https://standards-oui.ieee.org/oui/oui.txt)

## How does it work

#### Network scanning

The script will find out what your local IP is and then perform a ping sweep for every IP in the range of your local IP from 0 to 255.  
Scanning the network is done like xxx.xxx.xxx.0-255.

#### MAC address resolver

The MAC address is resolved using the [getmacbyip()](https://scapy.readthedocs.io/en/latest/routing.html#get-mac-by-ip) function from the scapy library and then the script will use the manufacturer database to find out the vendor name of the device based on that MAC address.

#### ARP poisoning

The ARP poisoning is done using the [ARP()](https://scapy.readthedocs.io/en/latest/api/scapy.layers.l2.html#arp) function from the scapy library which allows you to send a custom ARP packet to your targeted device and to the router, telling them that you are the router and that the targeted device is you. Now the only thing you need to do is [relay the packets](https://en.wikipedia.org/wiki/Packet_forwarding) between the targeted device and the router and you will be able to see all the traffic between the two devices.

#### More about the MITM attacks  
A Man In The Middle attack occurring on your personal network is actually a trick that exploit the MAC on the data link layer (check out the [OSI model](https://en.wikipedia.org/wiki/OSI_model) if you need a quick refresh).  
What our script is doing here is basically telling the router "hey i am the victim" and telling the victim "hey i am the router" therefore, you can act as a relay and see the packets sent from the victim to the router and vice versa assuming the script successfully managed to enable IP Forwarding or you manually set it on.

## Useful to know  

You can modify the code to process some packet as the following line shows (on [relay.py](https://github.com/b3rt1ng/SuperNova/edit/main/relay.py))
``` python
pkts = sniff(prn=lambda x:x.sprintf("{IP:%IP.src% -> %IP.dst%}"), filter=f"ip host {self.victim_ip} and not arp")
```
But I highly recommend using wireshark for the packet shelling since it's way more convenient and it's a lot more powerful / complete
