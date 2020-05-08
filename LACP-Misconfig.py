#!/usr/bin/python
from netmiko import ConnectHandler
from getpass import getpass
import csv, re
from itertools import zip_longest

username = "username"
password = "password"

device1 = {
    'device_type': 'cisco_nxos',
    'host': 'NX01.rodriguez.net',
    'username': username,
    'password': password,
}
device2 = {
    'device_type': 'cisco_nxos',
    'host': 'NX02.rodriguez.net',
    'username': username,
    'password': password,
}

all_devices = [device1, device2]
"""*********************************************************************************************************
*   The all_devices variable will be used to define what devices to iterate the code through. In this case *
*   dsw11 will be logged into first then dsw13.  Created empty lists to store values that python needs to  * 
*   store for later use in another command or use in split function with REGEX.                            *
*********************************************************************************************************"""
for a_device in all_devices:
    port_id_list = []
    port_mem_list = []
    port_desc_list = []
    port_chann_interfaces = []
    net_connect = ConnectHandler(**a_device)
    indy_port_member = net_connect.send_command("show port-channel summary | inc 'I'")
    indy_list = indy_port_member.split('\n')
    indy_list = indy_list[1:]
    """*****************************************************************************************************
    *  The previous block of code runs "show port-channel summary | inc 'I'" and splits the string variable*
    *  into a list at every newline.  Found any port channels w/ more than 3 interfaces the 4th and above  *
    *  would be on their own newline. Next for loop solved this inconsistancy. For i in indy_list will see *
    *  if the value 'Po' is in the list and if so will append list item 0 which is the port ID to variable *
    *  port_chann_interfaces list.                                                                         *
    *****************************************************************************************************"""
    for i in indy_list:
        value = 'Po' in i
        if value == True:
            i = i.split()
            i = i[0]
            port_chann_interfaces.append(i)
    """*****************************************************************************************************
    *  The following for loop 'for port_numbers in port_chann_interfaces:' utilizes Port Channel IDs from  *
    *  the port_chann_interfaces list and runs the commmands utilizing the format function to insert Port  *
    *  IDs one at a time. Then this data is appended to the 3 empty lists defined earlier.                 *
    *****************************************************************************************************"""
    for port_numbers in port_chann_interfaces:
        net_connect = ConnectHandler(**a_device)
        port_summary_pc = net_connect.send_command("show port-channel summary interface port-ch {}".format(port_numbers))
        port_chann_desc = net_connect.send_command("show interface port-chann {} description".format(port_numbers))
        port_channel_summary = re.findall('(\d+)\s+\S+\s+\S+\s+\S+\s+(.+\s\S.*\S\s.*)',port_summary_pc,re.M|re.I)
        port_desc = re.findall('(port-channel\d+)\s+(\S.+)',port_chann_desc,re.M|re.I)
        port_desc_output = [item for t in port_desc for item in t] # changes the list of tuples to a single list to be modified. 
        port_summary_list = [item for t in port_channel_summary for item in t] # changes the list of tuples to a single list to be modified. 
        # https://www.geeksforgeeks.org/python-convert-list-of-tuples-into-list/
        port_id_list.append(port_summary_list[0])
        port_mem_list.append(re.sub('\s+', ',', port_summary_list[1].strip()))
        port_desc_list.append(port_desc_output[1])

    output_lists = [port_id_list, port_desc_list, port_mem_list]
    export_data = zip_longest(*output_lists, fillvalue = '')
    with open(a_device['host'] + 'PortChannels_Misconfig.csv', 'w',encoding="ISO-8859-1", newline='') as myfile:
        wr = csv.writer(myfile)
        wr.writerow(("Port-ID", "Int Desc", "Members"))
        wr.writerows(export_data)
    myfile.close()
