# 🌌 SuperNova 🌌

## Work In Progress

  

SuperNova is an MITM attacking tool writen in python using [scapy](https://scapy.net/)

Also, he's the big Brother of [NOVA](https://github.com/b3rt1ng/NOVA) ;)

  

### Why is it better than Nova ?

Nova was made using os calls to ping and get mac addresses for Linux.

Basically SuperNova is building it's own requests based on the ICMP protocol, making it technically usable on every os as long as it support Scapy.

SuperNova's structure is designed to be easy to implement so you can mess with the code as you wish ;)

  
  

### current dev status

  

| status | feature |

| --- | --- |

| ✔️ | Precise network scan* |

| ✔️ | Mac address resolver |

| ✔️ | Vendor name resolver |

| ✔️ | ARP poisoning / MITM Attack |

| ❌ | IP Forwarding* |


*The Ip Forwarding method is pretty simple on Linux based OS since "ip_forward" file (located on "/proc/sys/net/ipv4/ip_forward" if you're wondering) just need to be set to 1 or 0.

On windows, the Tcpip data located on the Windows registry keys. And I still need to try out my script on windows so let's wait on that part.

  
dev note: the MITM part works for linux (according to several testings and visible proofs using wireshark) and the ARP poisoning method works but the IP Forwarding ain't working on all platform yet, I prefer not to consider it as achieved yet. If you're on linux you can perform MITM attacks without any problems.  

## Useful to know  

### About MITM attacks  
A Man In The Middle attack occurring on your personal network is actually a trick that exploit the MAC on the data link layer (check out the [OSI model](https://en.wikipedia.org/wiki/OSI_model) if you need a quick refresh).  
What our script is doing here is basically telling the router "hey i am the victim" and telling the victim "hey i am the router" therefore, you can act as a relay and see the packets sent from the victim to the router and vice versa assuming you've set your IP Forwarding on.
