def flatten(L):
    """ 
    L: a list 
    Returns a copy of L, which is a flattened version of L 
    """
    # Your code here  
    if L == []:   # base case: if the list is empty, stop recursion
        return []
    elif isinstance(L[0],list):   # if the first element is a list
        return flatten(L[0]) + flatten(L[1:])  # recursive step — it breaks the problem into smaller problems
    else:   # if the first element is not a list
        return [L[0]] + flatten(L[1:])

# Examples:
L = [[1,4,[6],2],[[[3]],2],4,5]
print(flatten(L)) # prints the list [1,4,6,2,3,2,4,5]