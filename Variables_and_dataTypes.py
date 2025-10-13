print("Hello world")
print("Bhuwan is my name","my age is 26")
print("my age is 26")
print(23)
print(21+98)

name = "Ashok"
age = 26
price = 25.99

#value assigned from right to left

age2 = age

print(name)
print(price)
print(age2)

print("my name is : ", name)
print("my age is : ", age)

print(type(name))
print(type(age))
print(type(price))


# data types can be int, float, string, boolean and none


# string can be written inside single, double or triple quote.

name1 = "Barsha"
name2 = 'Ale'
name3 = '''Magar'''

print(name1)
print(name2)
print(name3)


"""
 boolean values can True or False
 capital T or capital F 

 age = 26 
 old = False
"""
 

age4 = 23
old = False
a = None

print(type(old))
print(type(a))


#keywords = reserverd word

# variable can't be keywords

# print sum

b = 2
c = 5
sum = b + c
print(sum)


""""""
# punctuators = symbols to organize sentence structure

# typed language
# implicit and explicit
# python is implicit typed language

# implicit in python

# age = 26

# explicit in other language like java, c++

# int age = 26


# expression execution

# 1) string and numeric values operate with * 
A, B = 2,3
Txt = "@"
print(2*Txt*3) #(numeric * string * numeric)  => @@@@@@

# 2) string and string can operate with +

C, D ="2",3
Txt ="@"
print((C+Txt)*D) #(string + sring) * numeric  => 2@2@2@

# 3) numeric values can operate with all arithmetic operators   a * b + c

# 4) int * float = float  2 * 2.5 = 5

# 5) result of div operator with two integers will be float

# 6) integer division (//) with float and int will give int displayed as float 

F,G = 1.5, 3
H = F//G
print(H, F/G) #answer will be 0.0 0.5 

# floor gives closest integer, which is lesser than or equal to the float value i.e. result of (A // B) is same as floor (A/B)

X,Y = 1.5, 3
Z = X//Y
print(Z)

J, K= -12,5
L =J//K
print(L)

# 7) remainder(%) i.e. modulo is negative when denominator is negative

S, T=5,-2
U = S%T
print(U)

# single line comment

""" multi 
    line
    comment """

"""

# input in python

 accept values (using keyboard) from user

 1. string input 
    name = input("name : ")


"""
name = input("name : ")
print(name)

"""


"""

# 1. string input 
name = input("name : ")
print(name)

# 2. int input
age =  int(input("age : "))
print(age)

# 3. float input
price = float(input("price : "))
print(price)


print("My name is", name,"and I am ", age, "years old")

# operator precedence
# not > and > or
# and operator => if one False , o/p is False
# or operator => if one True , o/p is True
# ex. not True and false or True => True


# operator
num = 10
num = num + 10
num += 10 # 2 and 3 statement are same
print("num : ", num)


# type conversion
"""
1. type converion 
automatically


2. type casting
manually

"""
a = float("2")
b = 2.65

print(type(a))
print(a + b)




a = 2
b = 4.25

sum = a + b
print(sum)



c = 3.15
c = str(c)

print(type(c))


name = input("enter name : ")
age = int(input("enter age : "))
marks = float(input("enter marks : "))

print("welcome", name)
print("age", age)
print("marks", marks)

# practice question , write a program to input 2 numbers & print their sum

num1 = float(input("enter number1 : "))
num2 = float(input("enter number2 : "))

sum = num1 + num2 

print("sum of num1 and num2 is : ",sum)

# WAP to input side of a square & print its area

length = float(input("enter length of one side of a square in meter : "))

area = length ** 2 

print("area of a square is : ", area , " meter square")

# WAP to input 2 int numbers, a and b.
# print True if a is greater than or equal to b. If not print False.

a = int(input("enter a : "))
b = int(input("enter b : "))

if(a >= b ):
    print("True")
else:
    print("False")