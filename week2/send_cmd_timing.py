#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

password = getpass() 

device = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_ios"
}

net_connect = ConnectHandler(**device)
command = "ping"
output = net_connect.send_command_timing(command)
output += net_connect.send_command_timing('ip')
output += net_connect.send_command_timing('8.8.8.8')
output += net_connect.send_command_timing('5')
output += net_connect.send_command_timing('100')
output += net_connect.send_command_timing('2')
output += net_connect.send_command_timing('n')
output += net_connect.send_command_timing('n')
print(output)
