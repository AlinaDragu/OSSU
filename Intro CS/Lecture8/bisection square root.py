# bisection square root as a function
#########################
def bisection_root(x):
    epsilon = 0.01
    low = 0
    high = x
    ans = (high + low)/2.0
    while abs(ans**2 - x) >= epsilon:
        if ans**2 < x: 
            low = ans
        else: 
            high = ans
        ans = (high + low)/2.0
#    print(ans, 'is close to the root of', x)
    return ans

print(bisection_root(4))
print(bisection_root(123))