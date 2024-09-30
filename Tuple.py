#programm for tuples
l=(1,2.0,34,33)
print(l)

#concatenation of tuples
l=(1,2.0,34,33)
s=(32,45,33)
print(l+s)

#index
l=(1,2.0,34,33)
print(l[3])

#membership operators
l=(1,2.0,34,33)
print(34 in l)
print(1 not in l)

#slicing reverse
l=(1,2.0,34,33)
print(l[::-1])

#tuple methods (index)
l=(1,2.0,34,33)
print(l.index(33))

#tuple length method
l=(1,2.0,34,33)
print(len(l))

#count method () repited values
l=(1,2.0,34,33)
print(l.count(44))

#copy method
l=(1,2.0,34,33)
s=l
print(s)

#zip method
l=(1,2.0,34,33)
s=(12,43,67,43)
k=tuple(zip(l,s))
print(k)
