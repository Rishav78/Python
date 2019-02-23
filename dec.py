d={}
updated={}
n = int(input("Enter Any Number "))

for x in range(0,n):
    k = input("Enter Your Key ")
    v = int(input("Enter Your Value "))
    d.update({k:v})
s=len(d)
for x in range(0,s):
    k = max(d,key = lambda item:d[item])
    updated.update({k:d[k]})
    d.pop(k)

print(*updated.keys())
print(*updated.values())
