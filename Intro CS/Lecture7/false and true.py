############## YOU TRY IT ###################
# Write code that satisfies the following specification:
def div_by(n, d):
    """ n and d are ints > 0
        Returns True if d divides n evenly and False otherwise 
    """
    if n % d == 0:
        return True
    else:
        return False
    #return n % d == 0
# For example: 
print(div_by(10,3))     # print False
print(div_by(195,13))   # returns True