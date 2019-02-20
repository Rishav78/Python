# class Person:
#     count=0
#     def __init__(self,first_name,last_name,age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         Person.count = self.count + 1

#     def com_Cat(self):
#         return f"{self.first_name} {self.last_name}"


# p = Person('rishav','garg',19)
# p2 = Person('rupam','kumari',19)
# print(p.com_Cat())
# print(p2.com_Cat())
# print(Person.count)

#************************************************

class Person:
    count = 0
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        Person.count = Person.count + 1

    @classmethod
    def class_Person(cls,s):
        first_name, last_name, age = s.split(',')
        return cls(first_name,last_name,age)

    def con_Cat(self):
        return f"{self.first_name} {self.last_name}"

l = Person.class_Person('rishav,garg,12')
print(l.con_Cat())