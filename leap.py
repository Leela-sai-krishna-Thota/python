#programe to find the given year leap or not
y=int(input('enter the year'))
if y%4==0:
  if (y%100!=0 or y%400==0):
    print(y,' is a leap year')
else:
  print(y,' is not a leap year')
