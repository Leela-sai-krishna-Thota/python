#program for sets
s={1,2.0,45.67}
print(s)

#set inside 
s={1,2.0,(45,67)}
print(s)
s1={1,2.0,45.67,"leela"}
print(s1)

#set operations
s={1,2.0,45,67}
p={2,45,6.0,53}
print(s|p) #union
print(s&p) #intersection
print(s-p) #difference
print(s^p) #set symmetric difference
print(2.0 in p) #membership operator

# set methods
s={1,2.0,45,67}
p={2,45,6.0,53}
s.add("leela") #add
print(s)
p.clear() #clear
print(p)
s.discard(2.0) #discard
print(s)
s.pop() #pop
print(s)

# set methods 
s={1,2.0,45,67}
s1=s.copy() #copy
print(s1)
s={1,2.0,45,67}
p={2,45,6.0,53}
print(s.difference(p)) #difference
print(s.symmetric_difference(p)) #symmetric_difference
print(45 not in s) #membership operator
print(s.intersection(p)) #intersection
print(s.union(p)) #union
