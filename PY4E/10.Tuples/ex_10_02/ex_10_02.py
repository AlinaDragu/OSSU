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
    
    
many = dict()

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    time = words[5]
    hour = time.split(':')[0]
    many[hour] = many.get(hour, 0) + 1
    
sorted = sorted(many.items())
for hour,count in sorted:
    print(hour,count)
    

    
