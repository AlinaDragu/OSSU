# Hardcode a number as a secret number. Write a program that 
# checks through all the numbers between 1 to 10 and prints the 
# secret value.If it's not found, prints that it didn't find it.


found = False
secret = 100

for s in range(1,11):
    # i is 1,2,3....,11)
    if s == secret:
        found = True
if not found:
    print('not found')
else:
    print('found')
        
        