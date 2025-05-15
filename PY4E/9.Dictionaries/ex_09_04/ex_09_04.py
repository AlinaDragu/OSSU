# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
import os
fname = input("Enter file name: ")
try:
    # Construct the full path to the file in the same directory as the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, fname)
    fhand = open(file_path)
except:
    print('File cannot be opened:', fname)
    exit()

dir = dict()

for line in fhand:
    if not line.startswith('From '):
        continue
    words = line.split()
    mail = words[1] 
    dir[mail] = dir.get(mail, 0) + 1

count = None
email = None

for key,value in dir.items():
    if count is None or value > count:
        count  = value
        email = key

print(email,count)