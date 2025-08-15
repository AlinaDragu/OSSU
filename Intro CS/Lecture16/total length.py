# Modify the code we wrote to return the total length 
# of all strings inside L:   
    
def total_len_recur(L):
    if len(L) == 1:
        # "ab"
        return len(L[0]) 
    else:
        # "ab" "cde" "fghij"
        return total_len_recur(L[1:]) + len(L[0])

test = ["ab", "c", "defgh"]
print(total_len_recur(test))  # should print 8