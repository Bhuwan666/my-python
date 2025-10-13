# functions in python
# block of statements that perform a specific task

# sum of two numbers
# redundant/repeat code are known as bad code


#function definition
def calc_sum(a,b):     # function syntax  # parameters are input
    sum = a + b
    print(sum)
    return sum

calc_sum(1,3)   # function call  # parameters are now arguements, actual value
# a = 5
# b = 10

# sum = a + b
# print(sum)

# more lines of code
calc_sum(6,18)    # function call
# a = 6
# b = 18

# sum = a + b
# print(sum)

# more lines of code
calc_sum(9,11)    # function call
# a = 9
# b = 11

# sum = a + b
# print(sum)

# function definition
def calc_diff(a,b):   # function parameters
    return a - b    # we can also write this 

diff = calc_diff(6,8)  # function call; arguments # store value in a variable
print(diff)  


def print_hello():   # it can also be empty
    print("hello")

print_hello()
print_hello()
print_hello()
print_hello()
print_hello()

output = print_hello()
print(output)   # None   # no return 

# average of 3 numbers

def cal_avg(a,b,c):
    sum = a + b + c
    avg = sum / 2
    print(avg)
    

cal_avg(6,7,9)

"""
#  types of function in python
# 1. built_in functions
print()
len()
type()
range()

print("apnacollege", end=" ")  # sep = " "
print("ashok)  #end = "\n"y

# 2. user defined functions 

"""
# default parameters 
# assigning a default value to parameter, which is used when no argument is passed.

def calc_prod(a = 1,b = 1): # to return default parameter
    print(a * b)
    return a * b

calc_prod() 

"""
# we can also  give 
def cal_prod(a, b = 2):
    print(a*b)
    return a*b

cal_prod(1)

"""

# let's practice

# 1. waf to print the length of a list. (list is the parameter)

cities = ["po","lo","ko","io","yo"]
heroes = ["dad","mom","brother","wife","grandparents","friends"]

# len(cities)   --> we can print it directly

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)

# 2. waf to print the elements of a list in a single line. (list is the parameter)

heroes = ["dad","mom","brother","wife","grandparents","friends"]

# print(heroes[0], end=" ")
# print(heroes[1], end=" ")

def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(heroes)
print()

# 3. waf to find the factorial of n. (n is the parameter)

"""
n = 5
fact = 1
for i in range(1, n+1):
    fact *= i
print(fact)

"""

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

cal_fact(5)

# 4. waf to convert GBP to NRS

def converter(gbp_val):
    nrs_value = gbp_val * 190
    print(gbp_val, "USD =", nrs_value, "NRS")

converter(80)

# 5. waf to check if a numner is even or odd

def numType(num):
    rem = num % 2
    if (rem == 0):
        print("EVEN")
    else :
        print("ODD")

numType(8)

# Recursion
# when a function calls itself repeatedly

# recursive function
def show(n):
    if(n == 0):  # base case
        return
    print(n)
    show(n-1)

show(5)  #5,4,3,2,1

def fact(n):
    if (n == 1 or n == 0):
        return 1
    return fact(n-1) * n

ans = fact(6)
print(ans)

# let's practice
# 1. write a recurcive function to calculate the sum of first n natural numbers.

def cal_sum(n):
    if(n == 0):    # base case
        return 0
    else :

        return cal_sum(n-1) + n

sum = cal_sum(6)
print(sum)


# 2. write a recursive function to print all elements in a list. Hint : use list & index as parameters.

def print_list(list, idx = 0):
    if(idx == len(list)):     # base case
        return
    print(list[idx])
    print_list(list, idx+1)

fruits = ["mango","banana","apple","orange","pineapple","grape"]

uttar = print_list(fruits)
print(uttar)





