# Write a function that meets these specifications:
def char_counts(s):
    """ s is a string of lowercase chars 
    Returns a tuple where the first value is the 
    number of vowels in s and the second value 
    is the number of consonants in s 
    """
    # your code here
    vowels = 'aeiou'
    (c,v) = (0,0)
    for char in s :
        #char is 'a' then 'b' then 'c'
        if char in vowels : #vowels count
            v += 1
        else: #cons count
            c +=1
    return (v,c)
print(char_counts("abcd"))  # prints (1,3)
print(char_counts("zcght"))  # prints (0,5)