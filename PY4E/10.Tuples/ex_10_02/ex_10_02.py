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