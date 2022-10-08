![python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
# 🌌 SuperNova 🌌
## Work In Progess  

SuperNova is a MITM attacking tool writen in python using [scapy](https://scapy.net/)
Also, he's the big Brother of [NOVA](https://github.com/b3rt1ng/NOVA) ;)

### Why is it better than Nova ?  
Nova was made using os calls to ping and get mac adresses for Linux.  
Basically SuperNova is building it's own requests based on the ICMP protocol, making it technically usable on every os as long as it support Scapy.  
SuperNova's structure is designed to be easy to implement so you can mess with the code as you wish ;)


### current dev status

| status | feature |
| --- | --- |
| ✔️ | Precise network scan* |
| ✔️ | Mac adress resolver |
| ✔️ | Vendor name resolver |
| ❌ | ARP poisoning |
| ❌ | IP Forwarding** |
| ❌ | Deauther |  

*The network scan is proprely working, it's currently scanning assuming the network mask is set to 255.255.255.0 some network might use 255.255.0.0  
Assuming you're using a 1 second timeout you would have to scan for 255^2 host wich would take an absurd amount of time. I need to figure out a way to efficiently preform that without loosing too much time.  
  
**The Ip Forwarding method is pretty simple on Linux based OS since "ip_forward" file (located on "/proc/sys/net/ipv4/ip_forward" if you're wondering) just need to be set to 1 or 0.  
On windows, the Tcpip datas located on the Windows registry keys. And I still need to try out my script on windows so let's wait.  

