# #convert the data in tuple

# def fun(o, *args):
#     for i in args:
#         print(i)

# #fun(1,2,3,4,5,6,7,8,9)
# a = [1,2,3,4]
# print(*a) # * is for unpacking the data in list same we can use with other data types too

#**********************************

# def fun(n,*args):
#     l = []
#     for i in args:
#         l.append(i**n)
#     return l

# print(*fun(3,2,3,4,5,6,6,7,8))

#************************************

def Upper(l):
    for x in range(0,len(l)):
        l[x] = l[x].title();
    return l

l = ["rishav","garg","rupam","kumari"]
print(Upper(l))