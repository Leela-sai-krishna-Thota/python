#program for adding and average
l=[10,20,30,40]
print("sum=",sum(l))
print("average=",sum(l)/len(l))

#program for reversing the list
l=[10,20,30,40]
print(l[::-1])

#program to reverse the list using reverse method
l=[10,20,30,40]
l.reverse()
print(l)

#program to extract even and odd numbers from a given list
l=[]
n=int(input("enter n value"))
for i in range(n):
  ele=int(input("enter the elements"))
  l.append(ele)
even=[]
odd=[]
for i in l:
  if i%2==0:
    even.append(i)
  else :
    odd.append(i)
print("even list=",even)
print("odd list=",odd)


#program to to interchange first and last elements of a list
l=[10,20,30,40]
temp=l[0]
l[0]=l[-1]
l[-1]=temp
print(l)

#program to find the posisition of maximum and minimum elements in the list
l=[]
n=int(input("enter the n value"))
for i in range(n):
  ele=int(input("enter the elements"))
  l.append(ele)
print("maximum index",l.index(max(l)))
print("minimum index",l.index(min(l)))


#program to remove first occurence of a given elements in the  list
l=[10,20,10,30]
l.remove(10)
print(l)

#program to concatenate two lists
l1=["m","na","i","abhi"]
l2=["y","me","s","ram"]
l3=[]
for i,j, in zip(l1,l2):
  l3.append(i+j)
print(l3)
