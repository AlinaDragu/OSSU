# Finding Numbers in a Haystack

# In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.

# Data Files
# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

# Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
# Actual data: http://py4e-data.dr-chuck.net/regex_sum_2218537.txt (There are 66 values and the sum ends with 538)
# These links open in a new window. Make sure to save the file into the same folder as you will be writing your Python program. 

# Handling The Data
# The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.


import re
import os

fname = input("Enter file name: ")
try:
    # Construct the full path to the file in the same directory as the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, fname)
    with open(file_path, 'r') as file:
        text = file.read()
except:
    print('File cannot be opened:', fname)
    exit()


numbers = re.findall(r'[0-9]+', text)
total = sum([int(num) for num in numbers])

print("Sum:", total)