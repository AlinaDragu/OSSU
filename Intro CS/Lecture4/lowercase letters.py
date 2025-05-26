# Assume you are given a string of lowercase letters in variable s. 
# Count how many unique letters there are in s. For example, if 
# s = "abca" Then your code prints 3. 

# your code here
s = 'abca'
seen = ''

for char in s:
    if char not in seen:
        seen = seen + char
        
print(len(seen))