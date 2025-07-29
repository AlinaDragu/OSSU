def remove_elem(L, e):
    """ 
    L is a list
    e is an object
    Returns a new list with elements in the same order as L
    but without any elements equal to e. 
    """
    # your code here
    newlist = []
    for i in L:
        # i is 1 then 2 then 2 then 2
        if i != e:
            newlist.append(i)
    return newlist
  
L = [1,2,2,2]
print(remove_elem(L, 2))    # prints [1]
L = [1,2,2,2]
print(remove_elem(L, 1))    # prints [2,2,2]
L = [1,2,2,2]
print(remove_elem(L, 0))    # prints [1,2,2,2]
