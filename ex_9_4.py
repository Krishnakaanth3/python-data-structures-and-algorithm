'''
Write a program to read through the mbox-short.txt and figure out who has
sent the greatest number of mail messages. The program looks for 'From ' lines 
and takes the second word of those lines as the person who sent the mail. The 
program creates a Python dictionary that maps the sender's mail address to a 
count of the number of times they appear in the file. After the dictionary is 
produced, the program reads through the dictionary using a maximum loop to 
find the most prolific committer.
Desired Output: cwen@iupui.edu 5

This script processes a file to find the email address that appears the most
in lines that start with 'From '. It keeps track of the count of each email
address and determines the one with the highest count.

Usage:
    Run the script and enter the filename when prompted.

Example:
    Enter file: mbox-short.txt

Variables:
    name (str): The name of the file to be processed.
    fh (file object): The file handle for the opened file.
    count (int): A counter for the number of lines processed.
    d (dict): A dictionary to store the count of each email address.
    max_count (int): Stores the highest count of occurrences of an email address.
    max_email (str): Stores the email address with the highest count.
'''

# Prompt the user to enter the file name
name = input("Enter file:")

# Open the file with the given name
fh = open(name)

# Initialize a counter for the number of lines processed
count = 0

# Initialize a dictionary to store the count of each email address
d = {}

# Iterate through each line in the file
for line in fh:
    # Remove any trailing whitespace characters from the line
    line = line.rstrip()
    
    # Check if the line starts with 'From: '
    if line.startswith('From: '):
        # Split the line into words
        word = line.split()
        
        # Check if the line has more than one word
        if len(word) > 1:
            # Get the email address (second word in the line)
            mail = word[1]
            
            # Update the count of the email address in the dictionary
            d[mail] = d.get(mail, 0) + 1

# Initialize variables to store the email address with the highest count
max_count = -1
max_email = None

# Iterate through the dictionary items (email, count)
for email, count in d.items():
    # Check if the current count is greater than the max_count
    if count > max_count:
        # Update max_count and max_email with the current email and count
        max_count = count
        max_email = email

# Print the email address with the highest count and the count
print(max_email, max_count)