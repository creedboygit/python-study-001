from datetime import datetime, timedelta

today = datetime.today()

year = today.year
month = today.month
day = today.day
hour = today.hour
minute = today.minute
second = today.second


print(today)
print(year)
print(month)
print(day)
print(hour)
print(minute)
print(second)

print(datetime.today().strftime("%Y%m%d %H%M%S"))
print(datetime.today().strftime("%Y-%m-%d %H:%M0:%S"))

print()

yesterday = datetime.today() - timedelta(2)
print(yesterday)
print(yesterday.strftime("%Y-%m-%d"))
