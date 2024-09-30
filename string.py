#strings
s1='Hello' #using single quotes
s2="Hii"  # uisng double quotes
s3='''hello hi''' #using triple quotes
print(s1,s2,s3)

#string indexing
s="leela"
print(s[3])
s1="leela sai"
s2=" krishna"
print(s1+s2) #concatenation
print(s2*3) #repitition
for i in "lela sai krishna":
  print(i) #iteration
print("k" in s2) # membership operator
s3="leela sai krishna"
print(s3[6:9:1]) #slicing


#string methods
s="leela sai krishna"
print(s.capitalize()) #capitalize
print(s.upper()) #upper
print(s.lower()) #lower
s1="1234"
s2="sai"
s3 = "hello world"
s4="My name is {fname},im {age}".format(fname="leela",age=19)
s5="abcdefgh"
print(s1.isupper()) #isupper
print(s2.isupper())
print(s1.islower()) #islower
print(s2.islower())
print(s3.title()) #title
print(s4) # format
print(s1.isalnum()) #isanum
print(s5.isalpha()) #isalpha
print(s1.isdigit()) #isdigit
print(s5.isdigit())




