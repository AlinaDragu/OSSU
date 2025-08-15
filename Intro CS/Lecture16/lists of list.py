def in_lists_of_list(L, e):
    """
    L is a list whose elements are lists containing ints
    Returns True if e is an element within the lists of L
    and False otherwise. 
    Hint, the in operator is useful here, i.e. e in something
    """
    # your code here
    if len(L) == 1:
        return e in L[0]
    else:
        first = L[0]
        if e in first:
            return True
        else:
            return in_lists_of_list(L[1:],e)
    

test = [[1,2], [3,4], [5,6,7]]
print(in_lists_of_list(test, 3))  # prints True

test = [[1,2], [3,4], [5,6,7]]
print(in_lists_of_list(test, 0))  # prints False
