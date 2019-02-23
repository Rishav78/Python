s=[]
i=5
while i:
    a = input("Enter Any String ")
    s.append(a.center(6,"#"))
    i = i - 1
print(*s)