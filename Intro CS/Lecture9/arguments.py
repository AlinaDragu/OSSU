### example of variable number of arguments
###################
def mean(*args):
    """
    Assumes at least one argument and all arguments are numbers. 
    Returns the mean of the arguments.
    """
    tot = 0
    for a in args:
        tot += a
    return tot/len(args)

print(mean(1,2,3,4,5,6))
print(mean(6,0,9))

## Compare above code with this one:
# Note args vs *args and mean((6,0,9)) vs mean(6,0,9)
def mean(args):
    tot = 0
    for a in args:
        tot += a
    return tot/len(args)

print(mean((1,2,3,4,5,6)))
print(mean((6,0,9)))