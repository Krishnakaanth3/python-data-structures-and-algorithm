'''
apple = input ("Enter a string: ")
apple = int(apple)
x= apple - 10
print (x)

#fun fact - 0 (ground floor of the building) is the lowest floor of the building in europe. So, technically they started using this principle for indexing an array from 0.

fruit = 'banana'
letter = fruit[0]
print(letter)
#find length of a string using len() function
print(len(fruit))
#find last letter of a string
print(fruit[len(fruit)-1])
'''
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

#slicing strings
s = 'Monty Python'
print(s[0:4])
print(s[6:7])   
print(s[6:20])
print(s[:2])
print(s[8:])
print(s[:])
print(s[12::-1])
