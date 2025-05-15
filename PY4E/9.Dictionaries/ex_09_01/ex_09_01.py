# Counting word frequency using a dictionary
import os
# fname = input("Enter file: ")
# if len(fname) < 1 : fname = 'mbox-short.txt'

# fhand = open(fname)

fname = input("Enter file name: ")
try:
    # Construct the full path to the file in the same directory as the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, fname)
    fhand = open(file_path)
except:
    print('File cannot be opened:', fname)
    exit()
    
many = dict()

for line in fhand:
    line = line.rstrip()
    words = line.split()
    
    for wds in words:
        many[wds] = many.get(wds, 0) + 1
        
#find te word with the largest count

largest = None
bigword = None

for key , value in many.items() :
    if largest is None or largest < value :
        largest = value
        bigword = key
        
print(bigword,largest)        

