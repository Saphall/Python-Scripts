Capture data flowing through an interface and filter the data to gain useful info like visited sites, login info etc. 

> Run the `ARP_Spoofer` before sniffing.

ARP_Spoofer + Packet_Sniffer :
* Target a computer on same network.
* `arp_spoof` to redirect flow of packet(MITM).
* 'packet_sniffer' to see URLs,login_infos etc. sent by target.

---
Command: 
        
    python packet_sniffer.py

> Use of `sudo` or `administrator privilage` may be necessary.

---
Help:
    
    python packet_sniffer.py -h 
     
---

