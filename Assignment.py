import re

file = open('File.txt')
lst = []

for line in file:
	line = line.rstrip()
	tmp = re.findall('[0-9]+', line)
	if tmp:
		lst.append(tmp)

cout = 0
for slst in lst:
	for i in slst:
		cout += int(i)

print("The sum is:", cout)

file.close()