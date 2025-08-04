def pairwise_div(Lnum, Ldenom):
    """ Lnum and Ldenom are non-empty lists of 
        equal lengths containing numbers

    Returns a new list whose elements are the pairwise 
    division of an element in Lnum by an element in Ldenom. 

    Raise a ValueError if Ldenom contains 0. """
    # your code here
    # challenge: write this with list comprehension!
    L = []
    # L = [Lnum[i]/Ldenom[i] for i in range(len(Lnum))]
    # other way
    for i in range(len(Lnum)):
        # l is 0,1,2,3,4.....
        try:
            L.append(Lnum[i]/Ldenom[i])
        except:
            raise ValueError('nice message')
    return L
    
# For example:
L1 = [4,5,6]
L2 = [1,2,3]    
print(pairwise_div(L1, L2))  # prints [4.0,2.5,2.0]

L1 = [4,5,6]
L2 = [1,0,3]    
# print(pairwise_div(L1, L2))  # raises a ValueError

## to run after introducing assertions
L1 = [4,5,6,7,8]
L2 = [1,8,3]    
# print(pairwise_div(L1, L2))  # raises an AssertionError

L1 = []
L2 = []    
# print(pairwise_div(L1, L2))  # raises an AssertionError