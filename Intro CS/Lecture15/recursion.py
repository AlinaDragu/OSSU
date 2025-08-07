# Calculate n**p recursively by writing this function
def power_recur(n, p):
    if p==0 :
        return 1
    elif p==1 :
        return n
    else:
        return n*power_recur(n,p-1)

print(power_recur(2,3))  # prints 8