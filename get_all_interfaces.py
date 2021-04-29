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
                                        r"( .*\r\n)*",
                                        resp,
                                        re.MULTILINE)

    fields = {'ip_address' : r"( ip address (?P<ip_address>\S+) .*)\r\n*",
    'subnet' : r"( ip address .* (?P<subnet>\S+))\r\n*",
    'description': r"(description (?P<description>.*))\r\n"}

    for intf_part in interface_descriptions:
        temp = resp[intf_part.start():intf_part.end()-1]
        interface_data = [('interface',intf_part.group("intf_name"))]
        
        for field_name,field in fields.items():

            if re.search(field, temp, re.MULTILINE) is not None:
                for interface_type in re.findall(field, temp, re.MULTILINE):     
                    interface_data.append((field_name,interface_type[1]))
            else:
                interface_data.append((field_name,None))

        ord_dict = OrderedDict(interface_data)
        interfaces.append(ord_dict)

    if (interface !=None):
        interfaces = [inter for inter in interfaces if inter['interface']== interface]

    client.close()

    return (interfaces)

# print(SSHConnector())
