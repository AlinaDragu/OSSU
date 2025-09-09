import math
import time

## ----------------------------------
## CONSTANT Theta(1)
## ----------------------------------

## Theta(1)
def add(x, y):
    return x+y

## Theta(1)
def convert_to_km(m):
    return m*1.609

## ----------------------------------
## LINEAR Theta(n)
## Specify what n is in terms of input
## ----------------------------------

# constant in x: Theta(1)
# linear in y: Theta(y)
def mul(x, y):
    tot = 0
    for i in range(y):
        tot += x
    return tot

## Theta(len(s))
def add_digits(s):
    val = 0
    for c in s:
        val += int(c)
    return val

## Theta(a)
def fact_iter(a):
    prod = 1
    for i in range(1, a+1):
        prod *= i
    return prod

## Theta(x)
def fact_recur(x):
    """ assume x >= 0 """
    if x <= 1: 
        return 1
    else: 
        return x*fact_recur(x - 1)

## Theta(n_months)
def compound(invest, interest, n_months):
    total=0
    for i in range(n_months):
       total = total * interest + invest
    return total

## Theta(n)
def fib_iter(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_i = 0
        fib_ii = 1
        for i in range(n-1):
            tmp = fib_i
            fib_i = fib_ii
            fib_ii = tmp + fib_ii
        return fib_ii 