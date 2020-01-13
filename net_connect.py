from netmiko import ConnectHandler
from getpass import getpass

net_connect = ConnectHandler(
    host = "cisco3.lasthop.io",
    username = 'pyclass',
    password = getpass(),
    device_type = 'cisco_ios',
    session_log = "my_log.txt"
)

print(net_connect.find_prompt())
