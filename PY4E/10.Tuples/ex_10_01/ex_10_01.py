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
    words = line.split()
    
    for wds in words:
        many[wds] = many.get(wds, 0) + 1
        
#find the top 5 word by frequency

tmp = dict()
newlist = list()
for k,v in many.items():
    tup = (v,k)
    newlist.append(tup)
    
cool = sorted(newlist, reverse = True)

for v,k in cool[:5] : 
    print(k,v)