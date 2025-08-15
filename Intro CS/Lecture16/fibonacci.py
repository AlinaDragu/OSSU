## Fibonacci with a dictionary 
#################
def fib_recur(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib_recur(n-1)+fib_recur(n-2)

print(fib_recur(34))