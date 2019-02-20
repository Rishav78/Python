from functools import wraps
def dec(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):
        print("welcome in wrapper")
        return fun(*args, **kwargs)
    return wrapper

@dec
def function(n):
    '''hi there'''
    return n*n
print(function.__doc__)
print(function(3))