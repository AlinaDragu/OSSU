# Write code that satisfies the following specification:
# Hint, use paper and pen for a strategy before coding!
def is_palindrome(s):
    # """ s is a string
    # Returns True if s is a palindrome and False otherwise
    # """
       
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            return False
    return True      

s="2222"
print(is_palindrome(s))

s="222"
print(is_palindrome(s))

s="abc"
print(is_palindrome(s))
