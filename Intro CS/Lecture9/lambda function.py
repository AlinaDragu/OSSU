def apply(criteria,n):
    """ criteria is a function that takes in a number and returns a Boolean
        n is an int
    Returns how many ints from 0 to n (inclusive) match the criteria 
    (i.e. return True when criteria is applied to them)
    """ 
    count = 0
    for i in range(0, n+1):
        if criteria(i):
            count += 1
    return count

def is_even(x):
    return x%2==0

def is_5(x):
    return x==5

# print('apply with is_5:',apply(is_5,10))
print('apply with anon fcn:', apply(lambda x: x==5, 100))


# Shown another way, the following are equivalent:
# is_even(8)              # returns True
# (lambda x: x%2==0)(8)   # returns True