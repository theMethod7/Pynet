from netmiko import ConnectHandler
from getpass import getpass

device = { 'device1' : {
    "host" :  "cisco3.lasthop.io",
    "username" : 'pyclass',
    "password" : getpass(),
    "device_type" : 'cisco_ios',
    #session_log : "my_log.txt"},
 'device2' : {
    "host" : "nxos1.lasthop.io",
    "username" : 'pyclass',
    "password" : getpass(),
    "device_type" : 'nxos'}
 }
for x in device:
    print(x.net_connect.find_prompt())
    print(x.net_connect.send_command("show version"))
