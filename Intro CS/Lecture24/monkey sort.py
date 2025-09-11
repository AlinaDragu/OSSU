import random
import time

############################
## Bogo/Random/Monkey Sort Example
############################
def is_sorted(L):
    i = 0
    j = len(L)
    while i + 1 < j:
        if L[i] > L[i + 1]:
            return False
        i += 1
    return True
 
def bogo_sort(L):
    count = 0
    while not is_sorted(L):
        random.shuffle(L)
        count += 1
    return count
 
print("--- BOGO SORT ---")
# L = []
# for i in range(0, 9):
#     L.append(random.randint(0, 100))
L = [8, 4, 1, 6, 5, 11, 2, 0]
print('L:       ', L)
t0 = time.time()
count = bogo_sort(L)
print('Sorted L:', L)
print(count, "shuffles and sorting took: ", time.time() - t0, "s")
