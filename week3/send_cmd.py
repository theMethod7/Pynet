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
output += net_connect.send_command('', expect_string=r':')
output += net_connect.send_command('8.8.8.8', expect_string=r':')
output += net_connect.send_command('', expect_string=r':')
output += net_connect.send_command('', expect_string=r':')
output += net_connect.send_command('', expect_string=r':')
output += net_connect.send_command('', expect_string=r':')
output += net_connect.send_command('', expect_string=r':')
print(output)
