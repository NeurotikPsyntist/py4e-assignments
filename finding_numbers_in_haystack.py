fname = input('Enter file: ')
fh = open(fname)
import re
numlist = list()
for line in fh:
    line = line.strip()
    data = re.findall('[0-9]+',line)
    if len(data) != 1 : continue
    num = int(data[0])
    numlist.append(num)

print(numlist)
print('Values:',len(numlist))
print('Sum:',sum(numlist))

