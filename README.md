
<h1 align="center">
  <br>
  🌌SuperNova🌌
  <br>
</h1>

<h4 align="center">Performs a man in the middle with ease (and <a href="https://scapy.net/" target="_blank">Scapy</a>)</h4>


<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#download-manually">Download manually</a> •
  <a href="#how-does-it-work">How does it work</a>
</p>

<!-- ![screenshot](http://thing.gif) -->

## Key Features

* Network Scan - Scan on your network to find all the devices connected to it
  - Displays the IP, MAC, Vendor name and the hostname of the device
* ARP poisoning - Perform an ARP poisoning attack on the network
  - Choose a device to poison
  - Launch the attack
  - That's all ? Damn !

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
$ sudo python3 main.py
```

> **Note**
> The install file might not need the execution rights, but the mains script does.


## Download manually

Download scapy from [here](https://scapy.net/download/)  
Download the manufacutrer database from [here](https://gitlab.com/wireshark/wireshark/raw/master/manuf)

## How does it work

#### Network scanning

The script will find out what your local IP is and then perform a ping sweep for every IP in the range of your local IP from 0 to 255.  
Scanning the network is done like xxx.xxx.xxx.0-255 but it's also possible to scan like xxx.xxx.0-255.0-255 but the time spent scanning would be much longer.

#### MAC address resolver

The MAC address is resolved using the [getmacbyip()](https://scapy.readthedocs.io/en/latest/routing.html#get-mac-by-ip) function from the scapy library and then the script will use the manufacturer database to find out the vendor name of the device based on that MAC address.

#### ARP poisoning

The ARP poisoning is done using the [ARP()](https://scapy.readthedocs.io/en/latest/api/scapy.layers.l2.html#arp) function from the scapy library which allows you to send a custom ARP packet to your targeted device and to the router, telling them that you are the router and that the targeted device is you. Now the only thing you need to do is [relay the packets](https://en.wikipedia.org/wiki/Packet_forwarding) between the targeted device and the router and you will be able to see all the traffic between the two devices.

#### More about the MITM attacks  
A Man In The Middle attack occurring on your personal network is actually a trick that exploit the MAC on the data link layer (check out the [OSI model](https://en.wikipedia.org/wiki/OSI_model) if you need a quick refresh).  
What our script is doing here is basically telling the router "hey i am the victim" and telling the victim "hey i am the router" therefore, you can act as a relay and see the packets sent from the victim to the router and vice versa assuming you've set your IP Forwarding on.

