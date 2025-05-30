# FOR loop challenges

#1. print numbers 1 to 10
# Expected Output:
# 1
# 2
# ...
# 10

i = 0

for i in range(1,11):
    print(i)



#2. print even numbers from 2 to 20
# Expected Output:
# 2
# 4
# ...
# 20

i = 0

for i in range(2,21):
    if i % 2 == 0 :
        print(i)
        
        

#3. print each letter in a word
# Input: apple
# Output:
# a
# p
# p
# l
# e

word = input("Type your word here: ")

for w in word :
    print(w)
    
    
    
#4. loop through a list of items
# Print: "Item: book", etc.

items = ["book", "pen", "laptop", "phone"]

for item in items:
    print('Item:',item)
    
    
    


# WHILE loop challenges


# 5. count until 5
# Use a while loop to count from 1 to 5 and print each number

y = 1

while y <= 5:
    print(y)
    y += 1


#6. password checker
# correct_password = "open123"
# Keep asking: "Enter password: "
# Stop only when it's correct


correct_password = "open123"
password =""

while password != correct_password:
    password = input('Enter password: ')
    if password != correct_password:
        print("incorrect")
print("correct")
    
    
# #7. exit on command
# # Keep printing "Type a command: "
# # If they type "exit", print "Goodbye!" and end


command = "exit"
com = ""

while com != command:
    com = input('Type a command: ')
    if com == command:
        print("Goodbye!")
 