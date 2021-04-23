# cisshgo-flask-api
An simple implementation of flask connection with various dummy cisco routers for collecting real time information from the routers.
(#cisshgo: SSH server to [emulate network](https://github.com/tbotnz/cisshgo) equipment  - kudos to @tbotnz @lykinsb and team!)

## Setup

Following are the basic requirement for exceution.
1. python 3.5 and above [python](https://www.python.org/downloads/)
2. go installed for simulation of cisco routers.

## Usage

1. Change directory into cisshgo (All dependencies are included in the `/vendor` folder, so no installation step is necessary.)
2. Execute `go run cissh.go` as shown below:
3. If you only wish to launch with a single SSH listener for a testing process, you could simply apply `-listeners 1` to the run command:
```
go run cissh.go -listeners 1
2020/09/03 19:41:04 Starting cissh.go ssh server on port :10000
```

4. SSH into one of the open ports with `admin` as the password for ssh key generation.
Change the path of the key in connect.py file as well as the host I/P Address of the cisco device.
```python
...
client.load_host_keys('load your path of the key')
client.connect('ip_address',port=port_number, username='user', password='pass')
...
```

5. Install python packages required as shown below:
```python
> pip install -r requirements.txt
... <snip>
```

6. Start Flask by running the following command
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
|    Interface    | IP Address |     Subnet    |      Description      |
+-----------------+------------+---------------+-----------------------+
| FastEthernet0/0 | 10.0.2.27  | 255.255.255.0 |        netpalm        |
| FastEthernet3/0 | 172.16.2.1 | 255.255.255.0 |       Dataset         |
+-----------------+------------+---------------+-----------------------+
```

4.  An User Interface for the user to input an interface name and then view the corresponding interface details in the browser.


### Disclaimer
Cisco IOS is the property/trademark of Cisco.
