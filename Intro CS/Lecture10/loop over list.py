## Loops over lists
################
def square_list(L):
    for i in range(len(L)): 
        L[i] = L[i]**2

print(square_list([2,3,4]))  # prints None

Lin = [2,3,4]
print("before fcn call:",Lin)
square_list(Lin)
print("after fcn call:",Lin)   # mutated L

