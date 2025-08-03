import math

def count_sqrts(nums_list):
    """
    nums_list: a list
    Assumes that nums_list only contains positive numbers and that there are no duplicates.
    Returns how many elements in nums_list are exact squares of elements in the same list, including itself.
    """
    # Your code here
    
    # nums_set = set(nums_list) # convert the list to a set for faster lookups
    # count = 0 # counter
    # for num in nums_list:
    #     root = math.isqrt(num) # get the integer square root of the number
    #     if root * root == num and root in nums_set: # check if the number is a perfect square and its root is in the list
    #         count += 1  # increment
    # return count
    nums_set = set(nums_list) # convert the list to a set for faster lookups
    count = 0 # counter
    for num in nums_list:
        root = math.isqrt(num) # get the integer square root of the number
        if root * root == num and root in nums_set: # check if the number is a perfect square and its root is in the list
            count += 1  # increment
    return count

# Examples:    
print(count_sqrts([3,4,2,1,9,25])) # prints 3