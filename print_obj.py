class parent:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
    def __repr__(self):
        return f"{self.first_name} {self.last_name}"
    # def __str__(self):
    #     return f"{self.first_name} {self.last_name}"
    def __del__(self):
        print("rishav")

obj = parent('rishav','garg')
print(obj)
print([obj])