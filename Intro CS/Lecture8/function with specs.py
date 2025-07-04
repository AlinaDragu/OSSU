# Write a function that satisfies the following specs
# Use bisection_root we already wrote to get an approximation
# for the sqrt of an integer.
# For example: print(count_nums_with_sqrt_close_to(10, 0.1))
# prints 4 because all these integers have a sqrt within 0.1
#  sqrt of 99 is 9.949699401855469
#  sqrt of 100 is 9.999847412109375
#  sqrt of 101 is 10.049758911132812
#  sqrt of 102 is 10.099456787109375

def bisection_root(x):
    epsilon = 0.01
    low = 0
    high = x
    ans = (high + low) / 2.0
    while abs(ans**2 - x) >= epsilon:
        if ans**2 < x: 
            low = ans
        else: 
            high = ans
        ans = (high + low) / 2.0
    return ans


def count_nums_with_sqrt_close_to (n, epsilon):
    """ n is an int > 2
        epsilon is a positive number < 1
        Returns how many integers have a square root within epsilon of n 
    """
    count = 0
    # we reverse the sqrt range to get the range of i values
    start = int((n - epsilon)**2)
    end = int((n + epsilon)**2) + 1   #+1 because range end is exclusive
    for i in range(start, end):
        sqrt = bisection_root(i)
        if abs(sqrt - n) < epsilon :
            count += 1  #If sqrt(i) is within epsilon of n, count it
    return count
            
print(count_nums_with_sqrt_close_to(10, 0.1))