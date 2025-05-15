# Read through the mbox-short.txt file and count how many messages have been sent from each email address.

# Instructions:

# Open the File:

# Prompt the user to enter the filename.

# Open the specified file for reading.

# Initialize a Dictionary:

# Create an empty dictionary to store email addresses as keys and their corresponding message counts as values.

# Read the File Line by Line:

# Iterate through each line in the file.

# Process Relevant Lines:

# For each line:

# Remove any trailing whitespace.

# Check if the line starts with 'From ' (note the space after 'From').

# This ensures you only process lines that begin exactly with 'From ' and not lines that start with 'From:'.

# Extract Email Addresses and Count Messages:

# If a line starts with 'From ':

# Split the line into words using the split() method.

# Extract the second word in the line, which is the email address of the sender.

# Update the dictionary:

# If the email address is already a key in the dictionary, increment its value by one.

# If not, add the email address to the dictionary with a value of one.

# Display the Results:

# After processing all lines, iterate through the dictionary and print each email address along with its corresponding message count.


fname = input("Enter file name: ")
fn = open(fname)

count = dict()

for line in fn:
    line = line.strip()
    if line.startswith('From '):
        words = line.split()
        email = words[1]
        count[email] = count.get(email, 0) + 1

for email , cnt in count.items():
    print(email, cnt)
        
