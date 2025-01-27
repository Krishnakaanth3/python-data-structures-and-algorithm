import re

with open('regex_sum_2157102.txt') as hand:  # you need to put the terminal in the directory of the file (Best of lucks)
	numbs = []
	tot = 0
	for line in hand:
		x = re.findall('[0-9]+', line)
		if len(x) > 0:
			numbs.append(x)
	for elements in numbs:
		nums = list(map(int, elements))
		tot = tot + sum(nums)
	print(tot)