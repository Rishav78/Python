class person:
    def __init__(self):
        self.name = input("Enter Your Name ")
    def printf(self):
        print(self.name)

p = person()
print(p.__dict__)
print(getattr(p,'name'))
print(hasattr(p,'name'))
print(setattr(p,'name',p.name + ' garg'))
print(p.name)