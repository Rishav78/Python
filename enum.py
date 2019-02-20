def index(l,s):
    for x,y in enumerate(l):
        if y==s:
            return x
    return -1

l = list([1,2,3,4,5,6])
print(l,4)
print(index(l,4))
