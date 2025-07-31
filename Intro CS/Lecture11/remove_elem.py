def remove_all(L, e):
    """ 
    L is a list
    Mutates L to remove all elements in L that are equal to e
    Returns None.
    """
    # your code here
    Lnew = L[:]
    #clear the list
    L.clear() # L becomes emptylist []
    for n in Lnew:
        if e != n:
            L.append(n)

Lin = [1,2,2,2]
remove_all(Lin, 2)
print(Lin)    # prints [1]

Lin = [1,2,2,2]
remove_all(Lin, 1)
print(Lin)    # prints [2, 2, 2]

Lin = [1,2,2,2]
remove_all(Lin, 0)
print(Lin)    # prints [1, 2, 2, 2]
