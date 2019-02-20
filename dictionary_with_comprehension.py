# i = int(input("Enter any number "))
# d = {n:int(n**0.5) for n in range(1,i)}
# print(d)

#*********************************************

i = int(input("Enter any number "))
d = {n: ("Odd" if n%2!=0 else "Even") for n in range(1,i)}
print(d)