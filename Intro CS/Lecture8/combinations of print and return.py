# combinations of print and return
#########################

def is_even_with_return( i ):
    """ 
    Input: i, a positive int
    Returns True if i is even, otherwise False
    """
    print('with return')
    remainder = i % 2
    return remainder == 0

is_even_with_return(3)          # -> False
print(is_even_with_return(3))  # -> print(False)

def is_even_without_return( i ):
    """ 
    Input: i, a positive int
    Returns None
    """
    print('without return')
    remainder = i % 2
    has_rem = (remainder == 0)
    print(has_rem)
    ##return None

is_even_without_return(3)          # -> None
print(is_even_without_return(3))  # -> print(None)
