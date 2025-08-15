## Fibonacci with a dictionary 
#################
def fib_recur(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib_recur(n-1)+fib_recur(n-2)

print(fib_recur(34))


def score_count(x):
    """ Returns all the ways to make a score 
    of x by adding 1, 2, and/or 3 together. 
    Order doesn't matter. """
    if x == 1:
        return 1  # 1+0
    elif x == 2:
        return 2  # 2+0 or 1+1
    elif x == 3:
        return 3  # 3+0 or 2+1 or 1+1+1
    else:
        # make a score of x-1 then add 1
        # and make a score of x-2 then add 2
        # and make a score of x-3 then add 3
        return score_count(x-1)+score_count(x-2)+score_count(x-3)
    
print(score_count(4))  # prints 6
print(score_count(6))  # prints 20
print(score_count(13))  # prints 1431


## sum of a list, recursive
def total_recur(L):
  if L == []:
    return 0
  else:
    return L[0] + total_recur(L[1:])

test = [30, 40, 50]
print(total_recur(test))