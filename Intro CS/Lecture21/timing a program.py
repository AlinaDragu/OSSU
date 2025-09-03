# constant fcn
def c_to_f(c):
    return c*9.0/5 + 32

# linear fcn -- finds 0+1+2+...+x
def mysum(x):
    total = 0
    for i in range(x+1):
        total += i
    return total

# quadratic fcn -- finds n*n inefficiently
def square(n):
    sqsum = 0
    for i in range(n):
        for j in range(n):
            sqsum += 1
    return sqsum

# helper function to show timing
def time_wrapper(f, L):
    print('Timing', f.__name__)
    for i in L:
        t = time.time()
        f(i)
        dt = time.time()-t
        print (f"{f.__name__}({i}) took {dt} sec")

##creates a list [1, 10, 100, ...] to test different input sizes
L_N = [1]
for i in range(8):
    L_N.append(L_N[-1]*10)

## time each function
# time_wrapper(c_to_f,  L_N)
# time_wrapper(mysum, L_N)
# time_wrapper(square, L_N)  # caution this will take 500 sec, then 50000 sec

