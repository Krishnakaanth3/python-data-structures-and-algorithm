"""
This script reads a file (default is "mbox-short.txt") and processes its content to count the distribution of email messages by the hour of the day.

The script performs the following steps:
1. Prompts the user to enter a file name. If no name is entered, it defaults to "mbox-short.txt".
2. Opens the specified file.
3. Initializes an empty dictionary `d` to store the count of emails per hour and an empty list `lst` to store the sorted results.
4. Iterates through each line of the file:
    - If the line starts with "From ", it splits the line into words.
    - Extracts the hour from the timestamp (which is the 6th word in the line).
    - Updates the dictionary `d` with the count of emails for each hour.
5. Converts the dictionary `d` into a list of tuples and sorts it by hour.
6. Prints the sorted list of hours and their corresponding email counts.

Example output:
04 3
06 1
07 1
09 2
10 3
11 6
...
"""

# Prompt the user to enter a file name. If no name is entered, default to "mbox-short.txt"
name = input("Enter file:")
if len(name) < 1: 
    name = "mbox-short.txt"

# Open the specified file
handle = open(name)

# Initialize an empty dictionary to store the count of emails per hour
# Initialize an empty list to store the sorted results
d, lst = {}, []

# Iterate through each line of the file
for line in handle:
    # Check if the line starts with "From "
    if line.startswith("From "):
        # Strip any leading/trailing whitespace and split the line into words
        line = line.strip().split()
        # Extract the hour from the timestamp (6th word in the line)
        hour = line[5][0:2]
        # Update the dictionary with the count of emails for each hour
        d[hour] = d.get(hour, 0) + 1

# Convert the dictionary into a list of tuples and sort it by hour
for key, value in d.items():
    lst.append((key, value))
lst = sorted(lst)

# Print the sorted list of hours and their corresponding email counts
for key, value in lst:
    print(key, value)