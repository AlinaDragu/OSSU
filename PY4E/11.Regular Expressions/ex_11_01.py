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