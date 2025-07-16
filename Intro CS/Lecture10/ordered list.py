# Write a function that meets the specification:
def make_ordered_list(n):
    """ n is a positive int
    Returns a list containing all ints in order 
    from 0 to n (inclusive)
    """
    # your code here
    mylist = []
    for i in range(n+1):
        mylist.append(i)
    return mylist
    
print(make_ordered_list(6))  # prints [0, 1, 2, 3, 4, 5, 6]
