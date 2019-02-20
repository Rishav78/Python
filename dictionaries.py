# person = {'name' : 'rishav', 'age' : 19}
# print(person)
# print(type(person))
# name = dict(name = 'rishav', age = 19)
# print(name)
# print(name['name'])

#*************************************

# person = {
#     'name' : ['rishav','garg','rupam','kumari']
# }
# person['age']=[19,19,19,19]
# print(person)

#*************************************

# person = {
#      'name' : ['rishav','garg','rupam','kumari'],
#      'age' : 12
#  }
# if 12 in person.values():
#     print(True)
# elif 'name' in person.keys():
#     print(True)
# else:
#     pass

#***************************************

# person = {
#      'name' : ['rishav','garg','rupam','kumari'],
#      'age' : 12
#  }

# for x in person.keys():
#     print(person[x])

#***************************************

# person = {
#      'name' : ['rishav','garg','rupam','kumari'],
#      'age' : 12
#  }

# for x,y in person.items():
#     print(f"{x} -> {y}")

#***************************************

# person = {
#      'name' : ['rishav','garg','rupam','kumari'],
#      'age' : 12
#  }
# person.update({'name' : "rishav garg"})
# print(person)

#****************************************

# person = dict.fromkeys(["name",'age','gender'],'unknown')
# person = dict.fromkeys(["name",'age','gender'],['unknown' , 'unknown']) #To assign same value to all keys
# person1 = dict.fromkeys("name",'unknown')
# print(person)
# print(person1)

#***************************************

# person = dict(name='rishav',age=12)
# n = person
# print(person is n)
# print(person.get('names')) #use to handle error if wrong key enter

#**************************************

def dictionary(n):
    sq = dict.fromkeys(range(1,n+1),0)
    for i in range(1,n+1):
        sq[i]=i**3
    return sq

print(dictionary(5))