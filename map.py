#****************MAP FUNCTION WITH FUNCTION**********************

# def fun(n,v):
#     return n==v

# l = [1,2,3,4,5]
# print(list(map(fun,l,l)))

#****************MAP FUNCTION WITH LAMBDA*************************

# l = [1,2,3,4,5]
# print(list(map(lambda a,b:a==b,l,l)))

l = [1,2,3,4,5]
print(*map(lambda a,b:a==b,l,l))