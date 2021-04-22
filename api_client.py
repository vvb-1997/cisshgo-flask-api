import requests
r =requests.get('http://127.0.0.1:5000/api/')

print(r.json())
from prettytable import PrettyTable
  
# creating an empty PrettyTable
x = PrettyTable()
  
# adding data into the table
# column by column
x.add_column("First name",
             ["Shubham", "Saksham", "Preeti", "Ayushi",
              "Abhishek", "Dinesh", "Chandra"])
  
x.add_column("Last name", ["Chauhan", "Chauhan", "Singh",
                           "Chauhan", "Rai", "Pratap",
                           "Kant"])
  
x.add_column("Salary", [60000, 50000, 40000, 65000, 70000,
                        80000, 85000])
x.add_column("City", ["Lucknow", "Hardoi", "Unnao", "Haridwar",
                      "Greater Noida", "Delhi", "Ghaziabad"])
  
x.add_column("DOB", ["22 Feb 1999", "21 Aug 2000", "10 Jan 1995",
                     "30 Jan 2002", "16 Jan 1999", "3 Aug 1998",
                     "18 Sept 1997"])
  
# printing generated table
print(x)