class rishav:
    def __init__(self):
        print("__init__")
    def __del__(self):
        print("__del__")

d = rishav()
del d
f = input("Please Press Enter...")