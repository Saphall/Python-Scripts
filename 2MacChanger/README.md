Change the MAC address of an interface.

When we use command 'ifconfig' we see something like this : 

        enp3s0: flags= ---------------
                ether -:-:-:-:-:-  
        
        lo: flags= -------

        wlp2s0: flags= ---------  
        
Here options like 'enp3s0' denote interface and 'ether' denote mac address.

Use the script to change the MAC-Address of interface by:
  
        python macChanger.py -i 'INTERFACE NAME HERE' -m 'NEW MAC ADDRESS HERE'


