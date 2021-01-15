from urllib.request import urlopen
from bs4 import BeautifulSoup
#import ssl
import re
counts = list()

## TO IGNORE SSL CERTIFICATES
#ctx = ssl.create_default_context()
#ctx.check_hostname = False
#ctx.verify_mode = ssl.CERT_NONE

url = input('Enter: ')
html = urlopen(url).read()
data = BeautifulSoup(html,'html.parser')

text = str(data)
com_counts = re.findall('>([0-9]+)<',text)
for com_count in com_counts:
    num = int(com_count)
    counts.append(num)

print(counts)
print('Values:',len(counts))
print('Sum:',sum(counts))

