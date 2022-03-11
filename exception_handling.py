from ast import Try
from datetime import datetime, timedelta 

today = datetime.today()


print(today)

print('Hello in Age calculator ! Please enter your birthday DD/MM/YYYY :')

try:
    birthday = input()
    birthday = datetime.strptime(birthday,'%d/%m/%Y')
except   :
    print('please enter the age in numerical format')
    exit()


age = today - birthday

print ('Your Age : ',age.days // 365)

for _ in range(age.days):
    print ('Happy Birthday to You')
    10/10