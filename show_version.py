#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

device1 =  {    
    "host" : 'nxos1.lasthop.io',
    'username' : "pyclass",
    'password' : getpass(),
    'device_type' : 'cisco_nxos',
}

device2 =  {
    'host' : 'nxos2.lasthop.io',
    'username' : 'pyclass', 
    'password' : getpass(),
    'device_type' : 'cisco_nxos',
}

for devices in (device1, device2):
    net_conn = ConnectHandler(**devices)
    print(net_conn.find_prompt())
    if device2:
        output = net_conn.send_command("show version")
with open("show_version.txt", 'w') as f:
    f.write(output)
net_conn.disconnect()
