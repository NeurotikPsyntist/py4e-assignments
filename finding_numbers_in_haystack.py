fname = input('Enter file: ')
fh = open(fname)
import re
numlist = list()
for line in fh:
    line = line.rstrip()
    data = re.findall('[0-9]+',line)
    if len(data) == 0 : continue
    for nums in data:
        num = int(nums)
        numlist.append(num)
    #for nums in data:
        #if nums != 0 or ' ':
            #num = int(nums)
            #numlist.append(num)

print(numlist)
print('Values:',len(numlist))
print('Sum:',sum(numlist))

