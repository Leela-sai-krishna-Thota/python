#programe to find the triangle is valid or not by giving its sides
import math
a=int(input('enter the a value'))
b=int(input('enter the b value'))
c=int(input('enter the c value'))
s=(a+b+c)/2
a=math.sqrt(s*(s-a)*(s-b)*(s-c))
if a!=0:
  print('triangle exist and area=',a)
else:
  print('triangle does not exist')
