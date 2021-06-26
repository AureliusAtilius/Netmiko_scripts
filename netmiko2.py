from netmiko import ConnectHandler

s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.255.72',
    'username': 'josh',
    'password': 'cisco'
}

s3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.255.82',
    'username': 'josh',
    'password': 'cisco'
}

s4 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.255.83',
    'username': 'josh',
    'password': 'cisco'
}

all_devices = [s1,s2,s3]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    for n in range (2,21):
       print ("Creating VLAN " + str(n))
       config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
       output = net_connect.send_config_set(config_commands)
       print (output)
