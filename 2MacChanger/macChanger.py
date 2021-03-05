import subprocess

# interface = 'enp3s0'
# mac = '00:11:22:33:44:55'

interface = input('interface > ')
mac = input('new mac > ')

print('[+] Changing MAC address for '+interface+' to '+mac)

subprocess.call('sudo ifconfig ' + interface+' down', shell=True)
subprocess.call('sudo ifconfig '+interface+' hw ether '+mac, shell=True)
subprocess.call('sudo ifconfig ' + interface + ' up', shell=True)
