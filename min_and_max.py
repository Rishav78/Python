# l = [1,2,3,4,5,6]
# print(min(l))
# print(max(l))

#****************************************

l = {
    'person1' : {'Name' : 'Rishav', 'Last_name' : 'Garg' , 'Age' : 19},
    'person2' : {'Name' : 'Rupam', 'Last_name' : 'Kumari' , 'Age' : 18}
}

print(l.get(max(l,key = lambda item : l.get(item).get('Age'))).get("Name"))