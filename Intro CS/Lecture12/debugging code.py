##### STEPS TO DEBUG THE FOLLOWING BUGGY CODE ########
#######################################
## STEP 1: run it with test cases
def is_pal(x):
    """ Returns True is list x is a palindrome and False otherwise """
    temp = x
    temp.reverse
    if temp == x:
        return True
    else:
        return False

# print(is_pal(list('abcba')))  # input is ['a','b','c','b','a']
# print(is_pal(list('ab')))     # input is ['a','b']

## STEP 2: add print statements about halfway through       
def is_pal(x):
    """ Returns True is list x is a palindrome and False otherwise """
    temp = x
    temp.reverse
    print(temp, x)  # add this
    if temp == x:
        return True
    else:
        return False

# print(is_pal(list('abcba')))  # input is ['a','b','c','b','a']
# print(is_pal(list('ab')))     # input is ['a','b']
 
## STEP 3: Add more print statements before and after critical points
def is_pal(x):
    """ Returns True is list x is a palindrome and False otherwise """
    temp = x
    print('before reverse', temp, x)  # add this
    temp.reverse
    print('after reverse', temp, x)  # add this
    if temp == x:
        return True
    else:
        return False
 
# print(is_pal(list('abcba')))  # input is ['a','b','c','b','a']
# print(is_pal(list('ab')))     # input is ['a','b']

## STEP 4: Fix one issue, notice something is still wrong
def is_pal(x):
    """ Returns True is list x is a palindrome and False otherwise """
    temp = x
    print('before reverse', temp, x)
    temp.reverse()                      # fix this
    print('after reverse', temp, x)
    if temp == x:
        return True
    else:
        return False

# print(is_pal(list('abcba')))  # input is ['a','b','c','b','a']
# print(is_pal(list('ab')))     # input is ['a','b']

## STEP 5: Recall with lists, aliasing/mutability is an issue
def is_pal(x):
    """ Returns True is list x is a palindrome and False otherwise """
    temp = x[:]     # fix this
    print('before reverse', temp, x)
    temp.reverse()
    print('after reverse', temp, x)
    if temp == x:
        return True
    else:
        return False

# print(is_pal(list('abcba')))  # input is ['a','b','c','b','a']
# print(is_pal(list('ab')))     # input is ['a','b']
