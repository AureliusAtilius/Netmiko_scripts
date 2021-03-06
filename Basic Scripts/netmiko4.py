from netmiko import ConnectHandler

# Switches s2-s6
iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.255.72',
    'username': 'josh',
    'password': 'cisco',
}

iosv_l2_s3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.255.82',
    'username': 'josh',
    'password': 'cisco',
}

iosv_l2_s4 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.255.83',
    'username': 'josh',
    'password': 'cisco',
}

iosv_l2_s5 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.255.84',
    'username': 'josh',
    'password': 'cisco',
}

iosv_l2_s6 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.255.85',
    'username': 'josh',
    'password': 'cisco',
}

# Open configuration file and save lines in variable
with open('iosv_l2_cisco_design') as f:
    lines = f.read().splitlines()
print (lines)


all_devices = [iosv_l2_s4, iosv_l2_s5, iosv_l2_s6]
# Iterate over devices, connecting and applying configuration.
for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)

# Open core switch configuration file and save lines in variable
with open('iosv_l2_core') as f:
    lines = f.read().splitlines()
print (lines)


all_devices = [iosv_l2_s6, iosv_l2_s5, iosv_l2_s4, iosv_l2_s3, iosv_l2_s2]
# Iterate over devices, connecting and applying configuration.
for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)
