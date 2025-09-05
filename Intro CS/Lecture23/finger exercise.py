# Question 1: Choose the worst case asymptotic
# order of growth (upper and lower bound) for the following function. 
# Assume n = a.

def running_product(a):
    """ a is an int """
    product = 1
    for i in range(5,a+5):
        product *= i
        if product == a:
            return True
    return False