import requests
from prettytable import PrettyTable

class Query: 
    def __init__(self):
        self.result = []

    def api_call(self,url):
        r =requests.get(url)

        self.result = r.json()['data']

    def ascii_table(self):  
        # creating an empty PrettyTable
        x = PrettyTable()

        fields = {"interface":"Interface", "ip_address":"IP Address", "subnet":"Subnet", "description":"Description"}
        x.field_names = list(fields.values())

        for interface in self.result:
            temp = []
            for field in fields:
                temp.append(interface.get(field,None))
            x.add_row(temp)

        print(x)

query_all = Query()
query_all.api_call('http://127.0.0.1:5000/api/')
query_all.ascii_table()

query_one = Query()
query_one.api_call('http://127.0.0.1:5000/api/FastEthernet0/0/')
query_one.ascii_table()

query_unknown = Query()
query_unknown.api_call('http://127.0.0.1:5000/api/wrong')
query_unknown.ascii_table()