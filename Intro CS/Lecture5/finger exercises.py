# Assume you are given a string variable named my_str. 
# Write a piece of Python code that prints out a new string containing the even indexed characters of my_str.
# For example, if my_str = "abcdefg" then your code should print out aceg.

my_str = 'abcdefg'
s = ''

for i in range(0,len(my_str),2): #start a for loop where i takes values from 0 to len(my_str) - 1, stepping by 2 ;  range(0, 7, 2) produces: [0, 2, 4, 6]

    s += my_str[i]   #For each even index i, this line takes the character my_str[i] and adds it to the string s.
    

print(s)