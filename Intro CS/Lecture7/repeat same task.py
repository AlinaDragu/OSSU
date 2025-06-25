# A very simple example of a function that has one
#argument and returns one value
def is_even(i):   
    # """Assumes: i, a positive int
    # Returns True if i is even, otherwise False"""
    if i%2 == 0:
        return True
    else:
        return False

is_even(3) # <- returns False
is_even(8) # <- returns True

print(is_even(3)) # <- prints False
print(is_even(8)) # <- prints True
