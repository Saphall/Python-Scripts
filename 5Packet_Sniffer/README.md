#### Capture data flowing through an interface and filter the data to gain useful infos like visited sites, login info etc. 

> Run the <a href='https://github.com/Saphall/Python-Scripts/tree/main/4ARP_Spoofer'>`ARP_Spoofer`</a> before sniffing.

ARP_Spoofer + Packet_Sniffer :
* Target a computer on same network.
* `arp_spoof` to redirect flow of packet (MITM). 
* `packet_sniffer` to see URLs,login_infos etc. sent by target.

---
Command: 
        
    python packet_sniffer.py

> Use of `sudo` or `administrator privilage` may be necessary.

---
Help:
    
    python packet_sniffer.py -h 
     
---

