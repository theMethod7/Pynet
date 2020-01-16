#!/usr/bin/env python
from netmiko import Netmiko # We are calling netmiko from the netmiko but before we called ConnectHandler from netmiko.
from getpass import getpass # This calls the getpass() method which allows you to get prompted for the password without having to store it. 

'''Listed below is the device dictionary that will provide the arguments for the Netmiko function to work. 
Previously you could have the following: 

device1 = (
    host = "cisco3.lasthop.io",
    username = "pyclass",
    password = getpass(),
    device_type = 'cisco_ios',
)

This would then be passed along into net_conn = Netmiko(device1)
As you can see it is better to use a dictionary as it is cleaner and more scalable. 
Previously the listed the device1 is a list with variables which are assigned a string or a method, such getpass().
'''
password = getpass()
device = {
    "host": "cisco3.lasthop.io",
    'username': "pyclass",
    'password': password,
    "secret" : password, # This is required for the net_con.enable()
    'device_type': 'cisco_ios'
}

net_conn = Netmiko(**device)
net_conn.send_command_timing("disable")
print(net_conn.find_prompt())

net_conn.enable()
print(net_conn.find_prompt())
output = net_conn.send_command("show ip inter brief")
print(output)

net_conn.send_command("conf t", expect_string = r'#')
net_conn.send_command("inter loop 100", expect_string = r'#')
print("After interface loop 100")

output = net_conn.send_command("end", expect_string = r'#')
output = net_conn.send_command("show ip inter brief")
print(output)

