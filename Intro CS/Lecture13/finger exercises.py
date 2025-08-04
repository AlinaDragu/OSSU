def sum_str_lengths(L):
    """
    L is a non-empty list containing either: 
    * string elements or 
    * a non-empty sublist of string elements
    Returns the sum of the length of all strings in L and 
    lengths of strings in the sublists of L. If L contains an 
    element that is not a string or a list, or L's sublists 
    contain an element that is not a string, raise a ValueError.
    """
    # Your code here  
    length = 0
    for element in L:
        if isinstance(element,str):  #check if item is a string using isinstance(item, str)
            length +=len(element)
        elif isinstance(element, list):  #If the item is not a string, we check if it's a list
            for subelement in element:
                if isinstance(subelement, str):
                    length += len(subelement)
                else:
                    raise ValueError('Strings only')
        else:
            raise ValueError('List with only strings')
    return length

# Examples:
print(sum_str_lengths(["abcd", ["e", "fg"]]))  # prints 7
print(sum_str_lengths([12, ["e", "fg"]]))      # raises ValueError
print(sum_str_lengths(["abcd", [3, "fg"]]))    # raises ValueError