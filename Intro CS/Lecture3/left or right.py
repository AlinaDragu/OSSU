#Expand this code to show a sad face when the user entered the while loop more than 2 times
#Hint: use a variable as a counter

n = 0
where = input("Go left or right? ")
while where == "right":
    n = n + 1
    if n > 2:
        print(":(")
    where = input("Go left or right? ")
print("You got out!")