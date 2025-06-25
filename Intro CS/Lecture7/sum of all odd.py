### EXAMPLE: sum of all odd numbers between (including) a and b
###########################
## with a for loop
def sum_odd(a, b):
    sum_of_odds = 0
    for i in range(a, b+1):
        if i%2 == 0:
            sum_of_odds += i
            print(i, sum_of_odds)
    return sum_of_odds

print(sum_odd(2,4)) 
print(sum_odd(2,7)) 