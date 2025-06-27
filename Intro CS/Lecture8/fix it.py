# Fix this buggy code so it works according to the specification:

def is_triangular(n):
    """ n is an int > 0 
        Returns True if n is triangular, i.e. equals a continued
        summation of natural numbers (1+2+3+...+k) 
    """
    total = 0
    for i in range(n+1):
        total += i
        if total == n:
            return (True)
    return (False)

# # start by runing it on simple test cases
print(is_triangular(4))  # print False
print(is_triangular(6))  # print True
print(is_triangular(1))  # print True