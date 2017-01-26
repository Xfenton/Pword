import random
from datetime import date
import re
w = date.today().weekday()
month = date.today().month
year = date.today().year
y = str(year)
m = str(month)

if w == 1:
    w = 'Monday'
elif w == 2:
    w = 'Tuesday'
elif w == 3:
    w = 'Wednesday'
elif w == 4:
    w = 'Thursday'
elif w == 5:
    w = 'Friday'
elif w == 6:
    w = 'Saturday'
elif w == 7:
    w = 'Sunday'

Username = (w + m + y)
print (Username)

pWord = ('words.txt')
#q = pWord.read()
# p = re.sub('r'([a-z][A-Z]),'r'\1'r',q)
#print(p)
posWords = []
O = open(pWord, 'r')
Open = O.read()O.splitlines()
for x in range (0, len(Open)-1):
    if Open[x] == 6:
        append.posWords()
    else:
        pass

print (posWords)
print (Open)        





