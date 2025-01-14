fname = 'file.txt'
fhand = open(fname)
many = dict()
for line in fhand:
	line = line.rstrip()
	wds = line.split()
	# print(wds)
	for w in wds:
		print('====>', w)
		print('before', many)
		'''
                    # oldvalue = 0
                    # if w in many oldvalue = many [w]
 #this setting the default value to 0 if the key is not present and if the word is present it will get the value of the key can be also written as
		'''
            #oldvalue = many.get(w, 0)
            #print('oldvalue', oldvalue)
            #many[w] = oldvalue + 1
 # evev more simpler way to write the above code is
		many[w] = many.get(w, 0) + 1
		print('after', many)
print(many)
bigword = None
bigcount = None
for key, value in many.items():
    print(key, value)

    if bigcount is None or value > bigcount:
        bigword = key
        bigcount = value
print(bigword, bigcount)