# string 

str1 = "this is a string.\t we are creating it in python" # (\n) or (\t) escape sequence character => tab , next line

str2 = 'ashish ale magar'
str3 = """ my brother """

print(str1)

# basic operations 
# 1. concatenation

final_str = str1 + str2
print(final_str)

# 2. length of string

len1 = len(str1)
print(len1)

# empty spaces are also count : " "

# Indexing

str = "Barsha"
print(str[0])

# slicing
# accessing parts of a string

str4 = "Bhuwan Ale Magar"
print(str4[1:8])

# for slicing upto last of string
print(str4[5:len(str4)]) # or we can miss last string like str4(len[1:])
print(str4[5:]) #and this line is same as [5:0]

print(str4[:5]) #[0:5]

# in python we can count index backwards

str5 = "Apple"
print(str5[-3:-1])


# string functions

# 1. str.endswith("er") # returns true if string ends with substr

str6 = "I am a coder"
print(str6.endswith("er"))

# 2. str.capitalize() # capitalizes 1st char

str7 = "i am a coder"
print(str7.capitalize())
# for actual string
# str7 = str7.capitalize
#print(str7)


# 3. str.replace(old, new) # replaces all occurances of old

str8 = "I am a coder"
print(str8.replace("coder","pro coder"))

# 4. str.find(word) # returns 1st index of 1st occurance

str9 = "I am an engineer"  # returns -1 for unvalid index
print(str9.find("e"))

# 5. str.count()

str10 = "I am a boy"
print(str10.count("am"))

# str. shows all valid functions , slowly get used to it

# practice

# 1. Wap to input user's first name & print its length.

name = input("enter your first name : ")
print("length of your name is : ", len(name))

# 2. Wap to find the occurance of '$' in a string.

str11 = "I have $100 and $98"
print(str11.count("$"))



# conditional statements


"""
# conditional statements
# if-elif-else (syntax)

#indentation => proper spacing
if(condition):
    Statement1
elif(condition):
    Statement2
else:
    StatementN

"""

#Traffic lights code

light = input("light color : ")
if(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("look")
elif(light == "green"):
    print("go")
else:
    print("light is broken")


#Grades of students

marks = int(input("marks : "))
if(marks >= 90):
    print("A")
elif(marks >= 80 and marks < 90):
    print("B")
elif(marks >= 70 and marks < 80):
    print("C")
else:
    print("D")


#Practice

A = int(input("A : "))
G = input("M/F : ")

if((A == 1 or A == 2) and G == "M"):
    print("fee is 100")
elif(A == 3 or A == 4 or G == "F"):
    print("fee is 200")
elif(A == 5 and G =="M"):
    print("fee is 300")
else:
    print("no fee")


# nesting 

age = 34
if(age >= 18 ):
    if(age >= 80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")


# single line if / Ternary Operator

food = input("food : ")
eat = "yes" if food == "cake" else "no"
print(eat)

# another way of single line if

food = input("food : ")
print("sweet") if food == "cake" or food == "jalebi" else print("not sweet") #if ko awgadi ki else ko paxadi print garni
# if and else must be lower case

#clever if / ternary operator
# square bracket ma
age = int(input("age : "))
vote = ("yes","no") [age <= 18]
print(vote)

#ex: 2

sal = float(input("salary : "))
tax = sal*(0.1,0.2) [sal <= 50000]
print(tax)

p = float(input("p : "))
t = float(input("t : "))
r = float(input("r : "))
si = (p*t*r)/100
print(si)


age = 98
if(age >= 18 ):
    if(age >= 80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")


# 1. wap to check if a number entered by the user is odd or even.

num = int(input("enter any number : "))
rem = num % 2
if(rem == 0):
    print("even number")
else:
    print("odd number")

# 2. wap to find the greatest of 3 numbers entered by the user.

a = int(input("enter a : "))
b = int(input("enter b : "))
c = int(input("enter c : "))
d = int(input("enter d : "))

if((a >= b) and (a >= c) and (a >=d)):
    print("a is the greatest number")
elif(b >= c) and (b >= d):
    print("b is the greatest number")
elif(c >=d ):
    print("c is the greatest number")
else:
    print("d is the greatest number")

# 3. wap to check if a number is a multiple of 7 or not

x = int(input("enter number : "))

if(x % 7 == 0):
    print("mulltiple of 7")
else:
    print("not a multiple of 7")