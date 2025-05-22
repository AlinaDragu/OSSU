# Assume you are given a variable named number (has a numerical value). Write a piece of Python code that prints out one of the following strings: 

# positive if the variable number is positive
# negative if the variable number is negative
# zero if the variable number is equal to zero


number = float(input('Type here your number = '))
if number > 0 :
    print('positive')
elif number < 0 :
    print('negative')
elif number == 0 :
    print('zero')
    
print("Your number is", number)
