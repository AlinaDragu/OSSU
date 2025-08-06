def find_in_L(Ld, k):
    """ L is a list of dicts
        k is an int
    Returns True if k is a key in any dicts of L and False otherwise """
    # your code here
    for d in Ld:
        #d is k1 , v1
        if k in d:
            return True
    return False
  
d1 = {1:2, 3:4, 5:6}
d2 = {2:4, 4:6}
d3 = {1:1, 3:9, 4:16, 5:25}

print(find_in_L([d1, d2, d3], 2))  # returns True
print(find_in_L([d1, d2, d3], 25))  # returns False