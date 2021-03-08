import subprocess
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option('-i', '--interface', dest='interface',help='Interface to change its MAC address.')
    parser.add_option('-m', '--mac', dest='mac', help='New MAC address.')
    (options, arguments) = parser.parse_args()
    if not options.interface:
        # code to handle error of no interface argument
        parser.error('[-] Please specify an interface, use --help for more info.')
    if not options.mac:
        # code to handle error of no mac argument
        parser.error('[-] Please specify a new mac, use --help for more info.')
    return options


def mac_changer(interface, mac):
    print('Changing MAC address for '+interface+' to '+mac+'.')
    subprocess.call(['sudo', 'ifconfig', interface, 'down'])
    subprocess.call(['sudo', 'ifconfig', interface, 'hw', 'ether', mac])
    subprocess.call(['sudo', 'ifconfig', interface, 'up'])
    print('Done!')


# print(options)
# interface = 'enp3s0'
# mac = '00:11:22:33:44:55'
options = get_arguments()
mac_changer(options.interface, options.mac)
