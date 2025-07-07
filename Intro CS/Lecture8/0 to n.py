def apply(criteria,n):
    """ criteria is a function that takes in a number and returns a Boolean
        n is an int
    Returns how many ints from 0 to n (inclusive) match the criteria 
    (i.e. return True when criteria is applied to them)
    """ 
    # your code here
    count = 0
    for i in range(n+1):
        if criteria(i): #is a boolean
            count += 1
    return count


def is_even(x):
    return x%2==0

def is_five(x):
    return x == 5

how_many = apply(is_even,10)
how_manyy = apply(is_five,10)
print(how_many,how_manyy)
