# 1. Write code that satisfies the following specs:
def keep_consonants(word):
    # """ word is a string of lowercase letters
    #     Returns a string containing only the consonants 
    #     of word in the order they appear
    # """
    vowels = "aeiou"
    ans = ""
    for char in word:
        if char not in vowels:
            ans += char
    return ans
    

# For example
print(keep_consonants("abcd"))  # prints bcd
print(keep_consonants("aaa"))  # prints an empty string
print(keep_consonants("babas"))  # prints bbs


#  2. Write code that satisfies the following specs:
def first_to_last_diff(s, c):
    """ s is a string, c is single character string
        Returns the difference between the index where c first
        occurs and the index where c last occurs. If c does not 
        occur in s, returns -1. 
    """
    # your code here
    if c not in s:
        return -1
    # if reach here, c is in s
    for i in range(len(s)):
        if s[i]==c:
            # break here to save i as the first instance of c in s
            break
    # loop through s backwards
    for j in range(len(s)-1,-1,-1):
        if s[j]==c:
            # break here to save j as the last instance of c in s
            break
    # this return is ok becasue the loops iterated through indices not chars of s
    return j-i
# For example
print(first_to_last_diff('aaaa', 'a'))  # prints 3
print(first_to_last_diff('abcabcabc', 'b'))  # prints 6
print(first_to_last_diff('xyz', 'b'))  # prints -1