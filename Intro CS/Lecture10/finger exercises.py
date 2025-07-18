def all_true(n, Lf):
    """ n is an int
        Lf is a list of functions that take in an int and return a Boolean
    Returns True if each and every function in Lf returns True when called 
    with n as a parameter. Otherwise returns False. 
    """
    # Your code here
    flag = True
    for f in Lf:
        if not f(n):
            flag = False
            break
    return flag

# Examples:    
# all_true() # prints 6
is_even = lambda x: x % 2 == 0
greater_than_3 = lambda x: x > 3

print(all_true(6, [is_even, greater_than_3]))  # True
print(all_true(2, [is_even, greater_than_3]))  # False