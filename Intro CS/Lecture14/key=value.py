def count_matches(d):
    """ d is a dict
    Returns how many entries in d have the key equal to its value """
    # your code here
    count = 0
    for value,key in d.items():
        if value == key:
            count = count +1            
    return count

            
    

d = {1:2, 3:4, 5:6}
print(count_matches(d))   # prints 0

d = {1:2, 'a':'a', 5:5}
print(count_matches(d))   # prints 2