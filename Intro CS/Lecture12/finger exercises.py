

def count_sqrts(nums_list):
    """
    nums_list: a list
    Assumes that nums_list only contains positive numbers and that there are no duplicates.
    Returns how many elements in nums_list are exact squares of elements in the same list, including itself.
    """
    # Your code here
    nums_set = set(nums_list)  # use a set for faster lookups
    count = 0
    for num in nums_list:
        root = math.isqrt(num)
        if root * root == num and root in nums_set:
            count += 1
    return count

# Examples:    
print(count_sqrts([3,4,2,1,9,25])) # prints 3