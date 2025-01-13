'''
apple = input ("Enter a string: ")
apple = int(apple)
x= apple - 10
print (x)

fruit = 'banana'
letter = fruit[0]
print(letter)
#find length of a string using len() function
print(len(fruit))
#find last letter of a string
print(fruit[len(fruit)-1])

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
#string concatenation   
a = 'Hello'
b = a + 'There'
print(b)
c = a + ' ' + 'There'   
print(c)

#using in as a logical operator
fruit = 'banana'
print('n' in fruit)
print('m' in fruit)
print('nan' in fruit)
if 'a' in fruit:
    print('Found it!')

#string comparison
word = 'ban'
if word == 'banana':
    print('All right, bananas.')
if word < 'banana':
    print('Your word,' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word,' + word + ', comes after banana.')
else:
    print('All right, bananas.')

#string library
greet = 'Hello Bob'
zap = greet.lower()
print(zap)
print(greet)
print('Hi There'.lower())
print('Hi There'.upper())

#searching a string
fruit = 'banana'
pos = fruit.find('na')
print(pos)
aa = fruit.find('z')
print(aa)

#search and replace
greet = 'Hello Bob'
nstr = greet.replace('Bob','Jane')
print(nstr)
nstr = greet.replace('o','X')
print(nstr)

#stripping whitespace
greet = ' Hello Bob '   
print(greet.lstrip())
print(greet.rstrip())
print(greet.strip())

#prefixes
line = 'Please have a nice day'
print(line.startswith('Please'))
print(line.startswith('p'))

print(len('banana')*7)
'''


