#programeto determine the day of a week
import datetime
d=int(input('enter the date'))
m=int(input('enter the month'))
y=int(input('enter the year'))
date=datetime.date(y,m,d)
print(date.strftime('the week day is %A'))
