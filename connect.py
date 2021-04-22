from paramiko import SSHClient, AutoAddPolicy
import time
import re
from collections import OrderedDict

def SSHConnector(interface=None):
    client = SSHClient()
    
    #LOAD HOST KEYS
    client.load_host_keys(r"C:\Users\Admin\.ssh\known_hosts")
    client.load_system_host_keys()

    #Known_host policy
    client.set_missing_host_key_policy(AutoAddPolicy())

    client.connect('127.0.0.1',port=10000, username='cisshgo1000v', password='admin')

    chan = client.invoke_shell()
    chan.send('show running-config\n')
    time.sleep(1)
    resp = chan.recv(10000).decode("utf-8")

    interfaces = []

    interface_descriptions = re.finditer(r"^(interface (?P<intf_name>\S+))\r\n"
                                        r"( .*\r\n)*"
                                        r"( description (?P<description>.*))\r\n"
                                        r"( ip address (?P<ipv4_address>\S+) (?P<subnet_mask>\S+))\r\n",
                                        resp,
                                        re.MULTILINE)
    
    for intf_part in interface_descriptions:
        ord_dict = OrderedDict([('interface',intf_part.group("intf_name")),
        ('ip_address',intf_part.group("ipv4_address")),
        ('subnet',intf_part.group("subnet_mask")),
        ('description',intf_part.group("description").replace('"',''))])
        
        interfaces.append(ord_dict)
    
    if (interface !=None):
        interfaces = [inter for inter in interfaces if inter['interface']== interface]

    client.close()

    return (interfaces)

