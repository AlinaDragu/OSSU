# 1. What does this print?
# print(apply(lambda x: x%2==0, 10))

# 2. Call apply on n=100 and a lambda func 
#    that takes in a parameter and returns 
#    whether the parameter is a multiple of 10
#    What does it print?
# your code here


def do_twice(n, fn):
    return fn(fn(n))

print(do_twice(3, lambda x: x**2))