import random
from datetime import date
import re
w = date.today().weekday()
month = date.today().month
year = date.today().year
y = str(year)
m = str(month)

if w == 0:
    w = 'Monday'
    x = 8
elif w == 1:
    w = 'Tuesday'
    x = 8
elif w == 2:
    w = 'Wednesday'
    x = 8
elif w == 3:
    w = 'Thursday'
    x = 9
elif w == 4:
    w = 'Friday'
    x = 9
elif w == 6:
    w = 'Saturday'
    x = 10
elif w == 6:
    w = 'Sunday'
    x = 10

print (w + m + y)

f = open("words.txt")

characters = ['!','"','£','$','%','^','&','*']


import ocpsecurity

sec = ocpsecurity.security()

usr_name = ('Friday22017')

for line in f:    
    word = line.rstrip("\n")
    if len(word) == x:
        for digit in range(0,10):
            for y in range(0,len(characters)-1):
                pWord = word.capitalize() + str(digit) + characters[y]
                response = sec.SignIn(usr_name,pWord)
                if response != "Access Denied":
                    print('pwd:',pWord,'response:',response)

#poswords.append(word)
#print (len(poswords1))
#print (poswords1[0], "\t",poswords1[len(poswords1)-1])

#for line in poswords1:
#    poswords1.title()
print(len(pWord)/1)


