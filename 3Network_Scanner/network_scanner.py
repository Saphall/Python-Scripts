import scapy.all as scapy
import argparse


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--target', dest='target',
                        help='Target IP/ IP range.')
    options = parser.parse_args()
    return options


def scan(ip):
    print('\033[92m\nStarting Scan .....\033[0m')
    # scapy.arping(ip)
    arp_request = scapy.ARP(pdst=ip)
    # print(arp_request.summary())
    # scapy.ls(scapy.ARP())
    # arp_request.show()
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    # scapy.ls(scapy.Ether())
    # print(broadcast.summary())
    # broadcast.show()
    arp_request_broadcast = broadcast/arp_request
    # print(arp_request_broadcast.summary())
    # arp_request_broadcast.show()
    answered_list = scapy.srp(
        arp_request_broadcast, timeout=1, verbose=False)[0]
    # print(answered_list.summary())

    client_list = []

    for element in answered_list:
        # print(element[1].show())
        client_dict = {'ip': element[1].psrc, 'mac': element[1].hwsrc}
        client_list.append(client_dict)
        # print(element[1].psrc + "\t\t" + element[1].hwdst)
        # print(element[1].hwsrc)
    # print(client_list)
    return client_list


def print_result(results_list):
    print('\033[1m--------------------------------------------\nIP\t\t\tMAC Address\n--------------------------------------------')
    for client in results_list:
        print(f"{client['ip']}\t\t{client['mac']}")
    print('--------------------------------------------\033[0m')
    print('\033[92mDone.\n\033[0m')


options = get_arguments()
scan_result = scan(options.target)
print_result(scan_result)
