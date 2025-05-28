# Assume you are given a positive integer variable named N. 
# Write a piece of Python code that finds the cube root of N. 
# The code prints the cube root if N is a perfect cube or it prints error if N is not a perfect cube. 
# Hint: use a loop that increments a counter—you decide when the counter should stop.


N = int(input('Type your number here: '))
i = 0

while i ** 3 <= N:
    if i ** 3 == N:
        print('Cube root : ',i)
        break 
    i += 1
else:
    print('error')

        
    


































# N = int(input('Enter a positive integer: '))
# i = 0

# while i ** 3 <= N:
#     if i ** 3 == N:
#         print("Cube root:", i)
#         break
#     i += 1
# else:
#     print('its an error')