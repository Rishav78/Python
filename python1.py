# age  = int(input("Enter Your Age "))
# if age>= 18:
#     print("You Are Eligible")
# else:
#     print("not eligible")

# a = 12j
# print(type(a))

import random
chance=1
number = random.randint(1,100)
while True:
    num = int(input("Enter A Number "))
    if num==number or chance==5 :
        if chance==5:
            print("You have loose all your chance")
            print(number)
        else:
            print("You Win")
        break
    else:
        if num<number :
            print("Too low")
        else:
            print("Too high")
    chance = chance + 1

# name = input("Enter your Name")
# name = name.lower();
# age = int(input("Enter your Age"))
# if name[0]=='a':
#     if age > 10:
#         print("You can Enter")
# else:
#     print("POGO dekh ja k")

# name = "Rishav"
# x='R'
# if x in name:
#     print(x)

# while True:
#     name = input("Enter your name ")
#     if name:
#         while True:
#             age = int(input("Enter your age "))
#             if age>0:
#                 print("All Done")
#                 break
#         break

# n = int(input("Enter Any Number "))
# Total = 0
# while n>0:
#     Total = Total + n
#     n = n - 1
# print (Total)

# n = int(input("Enter Any Number "))
# Total = 0
# while n>0:
#     Total = Total + n%10
#     n=n//10
# print(Total)

# n = input("Enter Any Number ")
# Total = 0
# for x in n:
#     Total = Total + int(x)
# print(Total)
#***********************************************************
# name = input("Enter Any Number ")
# for x in name:
#     print(f"{x} : {name.count(x)}")

# while True:
#     name = input("Enter Your Name ")
#     p = int(input("Enter Your Physic Marks "))
#     if p>100:
#         continue;
#     p = int(input("Enter Your Chemistry Marks "))
#     if p>100:
#         continue;
#     p = int(input("Enter Your Math Marks "))
#     if p>100:
#         continue;
#     print("All Done")
#     break

#******************************************

# def Sum(a,b):
#     return a+b
# n1 = input("Enter first value ")
# n2 = input("Enter second value ")
# choose = int(input("Enter 1 for int and 2 for string "))
# if choose==1:
#     n1=int(n1)
#     n2=int(n2)
# print(Sum(n1,n2))

#******************************************

# def Is_even(s):
#     if s%2==0:
#         return False
#     else:
#         return True

# s = int(input("Enter Any Number to check even or odd "))
# print(Is_even(s))

#*******************************************

# def greater(a,b):
#     if(a>b):
#         return a
#     return b

# def greatest(a,b,c):
#     return greater(greater(a,b),c)

# a, b, c = input("Enter Three Numbers ").split()
# print(greatest(int(a),int(b),int(c)))

#**********************************************

# def Is_palidrom(s):
#     return s==s[::-1]

# string = input("Enter Any string ")
# print(Is_palidrom(string))

#**********************************************

# def fabonacci_series(n=0):
#     a=0
#     b=1
#     for x in range(0,n,1):
#         if x==0:
#             print(a, end=" ")
#         elif x==1:
#             print(b, end = " ")
#         else:
#             b = b + a
#             a = b - a
#             print(b, end=' ')

# n = int(input("Enter Any Number "))
# fabonacci_series()

#***********************************

# name = ["Rishav" , "Rupam"]
# print(name[::-1])

#***********************************

# name = []
# n = int(input("Enter No Of Element You Wanna Insert In List "))
# for x in range(0,n,1):
#     string = input("Enter String ")
#     name.append(string)
# for x in name:
#     print(x, end=" ")

#***********************************

# name = "rishav,garg".split(",");
# n = ['ri' , 'ga']
# print(name)
# name.append(n)
# print(name[-1])

#************************************

# def sqr(l):
#     n = []
#     for x in l:
#         n.append(x*x)
#     return n

# n = [1 , 2 , 3 , 4 , 5]
# print(sqr(n))

#****************************************

# def reverse(l):
#     return l[::-1]

# l = list(range(0,11))
# print(reverse(l))

#*****************************************

# def string_rev(l):
#     n = []
#     for x in l:
#         n.append(x[::-1])
#     return n

# n = ['rishav' , 'garg']
# print(string_rev(n))

#******************************************

# def filter(l):
#     even = []
#     total = []
#     for x in l:
#         if x%2==0:
#             even.append(x)
#         l.remove(x)
#     total.append(even)
#     total.append(l)
#     return total

# l = list(range(0,11))
# print(filter(l))

#******************************************

# def unique(l1,l2):
#     l3 = []
#     for x in l1:
#         if x in l2:
#             l3.append(x)
#     return l3

# l1 = [1,2,3,4,5]
# l2 = [1,2,7,8,9]
# print(unique(l1,l2))
