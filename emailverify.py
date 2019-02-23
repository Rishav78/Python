import re
email = input("Enter yout Name ")
m=re.match(r'^[a-zA-Z1-9_]+(\.[a-zA-Z1-9]+)*@[a-zA-Z1-9]+(\.[a-zA-z1-9]+)*(\.[a-zA-z1-9]+)$',email)
if(m):
    print(m)