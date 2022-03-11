from datetime import datetime


current_date = datetime.now()

print('Day: ' + str(current_date.day))
print('Day: ' + str(current_date.month))
print('Day: ' + str(current_date.year))

print(str(current_date.day),str(current_date.month),str(current_date.year))

date_log=str(current_date.day)+str(current_date.month)+str(current_date.year)+str(current_date.hour)

print(date_log)

birthday = input('When is your birthday (dd/mm/yyyy)? ')

birthday_date = datetime.strptime(birthday,'%d/%m/%Y')
print('Birthday: ' + str(birthday_date))

one_day = timedelta(days=1)

birthday_eve= birthday_date - one_day