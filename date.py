from datetime import datetime, timedelta

current_date = datetime.now()

print ('Today is: ' + str(current_date.date()))

today = datetime.now()
one_day= timedelta(days=1)
one_week= timedelta(weeks=1)
#one_month = timedelta(month=1)
#one_year= timedelta(years=1)

yesterday = today - one_day
#last_month= today - one_month
last_week= today - one_week
#last_year= today - one_year
print(yesterday)
#print(last_month)
print(last_week)
#print(last_year)

resv_date = input('Time the date to reserve (DD/MM/YYYY): ')
resv_date = datetime.strptime(resv_date,'%d/%m/%Y')

print(resv_date.date())
print('Reservation eve : ', resv_date - one_day)
