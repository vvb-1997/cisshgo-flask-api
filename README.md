# cisshgo-flask-api
An simple implementation of flask connection with various dummy cisco routers for collecting real time information from the routers.
(#cisshgo: SSH server to emulate network equipment - kudos to @tbotnz @lykinsb and team!)

## Setup

Following are the basic requirement for exceution.
1. python 3.5 and above [python](https://www.python.org/downloads/)
2. go installed for simulation of cisco routers.

## Usage

1. Follow the steps for simulation of cisco routes [here](https://github.com/tbotnz/cisshgo)
2. Install python packages required as shown below:
```python
> pip install -r requirements.txt
... <snip>
```

3. SSH into one of the open ports with `admin` as the password for ssh key generation.
Change the path of the key in connect.py file as well as the host I/P Address of the cisco device.
```python
...
client.load_host_keys('load your path of the key')
client.connect('ip_address',port=port_number, username='user', password='pass')
...
```

4. Start Flask by running the following command
```python
python main.py
```

## Features

1. `main.py` : Flask instance for connection with the cisco routers for collection as well as monitering of config and connections with the router in Real Time.

2. Two API endpoints for getting information from the cisco router 
1.`/api/` : To get all the interfaces conneted to the router with their IP, Subnet Mask and Description.
2.`/api/<interface>` :  To get all the information of a particular interface conneted to the router with their IP, Subnet Mask and Description.

3.  `api_client.py` : Python script to consume the APIs hosted by flask and display the data in an ascii table format.
For example, in the packaged output of the  `api_client.py` script  is listed as:
```python
+-----------------+------------+---------------+-----------------------+
|    Interface         | IP Address |     Subnet       |      Description           |
+-----------------+------------+---------------+-----------------------+
| FastEthernet0/0 | 10.0.2.27  | 255.255.255.0 |        netpalm               |
| FastEthernet3/0 | 172.16.2.1 | 255.255.255.0 |       Dataset                |
+-----------------+------------+---------------+-----------------------+
```

4.  An User Interface for the user to input an interface name and then view the corresponding interface details in the browser.


### Disclaimer
Cisco IOS is the property/trademark of Cisco.
