import subprocess
import optparse
import re


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option('-i', '--interface', dest='interface',
                      help='Interface to change its MAC address.')
    parser.add_option('-m', '--mac', dest='mac', help='New MAC address.')
    (options, arguments) = parser.parse_args()
    if not options.interface:
        # code to handle error of no interface argument
        parser.error(
            '[-] Please specify an interface, use --help for more info.')
    if not options.mac:
        # code to handle error of no mac argument
        parser.error('[-] Please specify a new mac, use --help for more info.')
    return options


def mac_changer(interface, mac):
    print('\033[1mChanging MAC address for '+interface+' to '+mac+'.\033[0m')
    subprocess.call(['sudo', 'ifconfig', interface, 'down'])
    subprocess.call(['sudo', 'ifconfig', interface, 'hw', 'ether', mac])
    subprocess.call(['sudo', 'ifconfig', interface, 'up'])
    print('\nTask Complete.')


def get_current_mac(interface):

    ifconfig_result = subprocess.check_output(["ifconfig", interface])
# print(ifconfig_result)

    mac_address_search_result = re.search(
        r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result.decode('utf-8'))

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("\033[91m\n[-] Could not read MAC address.Check Interface.\033[0m")


# print(options)
# interface = 'enp3s0'
options = get_arguments()


current_mac = get_current_mac(options.interface)
print("\033[1m\nCurrent MAC = "+str(current_mac)+'\033[0m')

mac_changer(options.interface, options.mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.mac:
    print('\033[92m\n[+] MAC address was successfully changed to ' +
          current_mac+'\033[0m\n')
else:
    print('\033[91m\n[-] MAC address did not change.\033[0m\n')
