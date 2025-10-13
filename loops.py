# loops in python
# used to repeat instructions

count = 1       # variable are called iterator
while count <=5 :       # process is called iteration
    print("hello")
    count += 1
  
print(count)
 
# print number from 1 to 8
i = 1
while i <= 8 :
    print("world" , i)   # i is the count
    i += 1
print(i)
print("loop ended")


# print number in reverse
i = 5
while i >= 1:
    print(i)
    i -= 1
print("loop ended")

# lets practice 
# 1. print numbers from 1 to 100

num = 1 # initialization
while num <= 100:
    print(num)
    num += 1
print("number upto 100")

# 2. print number from 100 to 1

num2 = 100 # initialization
while num2 >= 1:
    print(num2)
    num2 -= 1
print("number from 100 to 1")

# 3. print the multiplication table of a number n.

num3 = int(input("enter any number : "))
print("multiplication of : ", num3)
i = 1  # initialization
while i <= 10:
    print(num3 * i)
    i += 1

# 4. print the elements of the following list using a loop:
#  [1,4,9,16,25,36,49,64,81,1001]
#  ["ironman","thor","superman","batman"]
#  traverse = going through each element

nums = [1,4,9,16,25,36,49,64,81,100]

i = 0  # initialization
while i < len(nums):
    print(nums[i])  # nums[0], nums[1]...
    i += 1

heroes = ["ironman","thor","superman","batman"]

j = 0  # initialization
while j < len(heroes):
    print(heroes[j])
    j += 1


# 5. search for a number x in this tuple using loop:
# [1,4,9,16,25,36,49,64,81,36,100]

num1 = (1,4,9,16,25,36,49,64,81,36,100)

x = 36
i = 0 # initialization
while i < len(num1):
    if(num1[i] == x):
        print("found at index", i)
    else:
        print("finding...")
    i += 1


# break and continue

# break : used to terminate the loop when encountered.
# continue : terminates execution in the iteration & continues execution of the loop with the next iteration.

""" break "" 
# print numbers from 1 to 5 but stop at 3
i = 1
while (i <= 5):
    print(i)
    if(i == 3):
        break
    i += 1
print("end of loop")

"""

"""
# find number and then stop
nums = (1,4,9,16,25,36,49,64,81,100)

x = 36
i = 0
while(i < len(nums)):
    if(nums[i] == x):
        print("found at index", i)
        break
    else:
        print("finding...")
    i += 1
print("end of loop")

"""

""" continue "" 
#print number from 0 to 5 but skip 3
i = 0

while (i <= 5):
    if( i == 3):
        i += 1
        continue  #skip
    print(i)
    i += 1

"""
"""
# print odd numbers and skip even numbers

i= 0
while (i <= 10):
    if(i%2 == 0):
        i += 1
        continue #skip
    print(i)
    i += 1

"""


# print even numbers and skip odd numbers 

i = 1
while(i <= 10):
    if(i%2 != 0):
        i += 1
        continue #skip
    print(i)
    i += 1



# for loops in python
# loops are used for sequential traversal. For traversing list, string, tuples etc.

nums = [1,2,3,4,5]   # list

for val in nums:     # syntax 
    print(val)

veggies = ["potato", "brinjal", "cucumber","ladyfinger"]  # list

for val1 in veggies :
    print(val1)

tup = (8,1,2,3,4,8,9,5)  # tuple

for val2 in tup:
    print(val2)

str = "apnacollege"    # string

for char in str:
    print(char)
else:
    print("end")

str2 = "barsha_syangtang"

for char2 in str2:
    if(char2 == 'y'):
        print("y found")
        break
    print(char2)
print("end")
    



# when using while or for , it is optional to use else




#so generally for iterators, like we have variable whose value needs to be updated, and we have stopping condition, => we do these using while loop

#kisi data type ke upar traverse karna hai , jaisi list , tuple or strings ,we use for loop


# lets practice
# 1. print the elements of the following list using a loop:
# [1,4,9,16,25,36,49,64,81,100]
 
num = [1,4,9,16,25,36,49,64,81,100]

for el in num:
    print(el)
    

# 1. search for a number x in this tuple using loop:
# (1,4,9,16,36,49,64,81,100,49)

num2 = (1,4,9,16,25,36,49,64,81,100,49)

x = 49

idx = 0
for el in num2:
    if(el == x):
        print("number found at idx", idx )
        break
    idx += 1


# range() 
# range functions returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number
# range( start?, stop, step?)  # here ? is optional

# for example

seq = range(5)
print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])
print(seq[4])

# or we can use for loop 
for i in seq:
    print(i)

# or most of the time we can use

for i in range(10):
    print(i)

for i in range(5):  #range(stop)
    print(i)

for i in range(1,10): #range(start,stop)
    print(i)

for i in range(1,10,2): #range(start,stop,step)
    print(i)

for i in range(2,100,2): #print even numbers upto 100
    print(i)

for i in range(1,100,2): #print odd numbers upto 100
    print(i)

# in programming, this process of searching is called linear search , search inside single line


# lets practice
# using for and range()
# 1. print numbers from 1 to 100.


for i in range(1,101):
    print(i)


# 2. print numbers from 100 to 1.

for i in range(100,0,-1):
    print(i)


# 3. print the multiplication table of number n.

num = int(input("enter number : "))

for i in range(1,11):
    print(num * i)
    


# pass statement
# it is a null statement that does nothing. It is used as a placeholder for future code.

for i in range(5):
    pass
if (i <= 5):
    pass
print("some useful work")



# lets practice
# 4. wap to find the sum of first n natural numbers. 

n = 9  #want to sum numbers from 1 to 9
sum = 0  #initialize variable sum to 0
for i in range(1,n+1):  #generates number from 1 uptp n inclusive
    sum += i  

print("total sum : ",sum)

#same question using while

n = 9  # the number of natural numbers to sum
sum = 0  # initialize sum to 0
i = 1   # start counter at 1


while(i <= n):  # continue loop until i exceeds n
    sum += i   # add current i to sum
    i += 1  # increment i by 1 to move to next number
print("total sum : ", sum)  # print the final sum

# 5. wap to find the factorial of first n natural numbers.

# using while

n = 5
fact = 1     # always initialize with 1 for factorial not 0 , because 0 multiplied is always 0
i = 1
while(i <= n):
    fact *= i
    i += 1
print("factorial of first : ", fact)

# 5. wap to find the factorial of first n natural numbers.

# using while

n = 5
fact = 1     # always initialize with 1 for factorial not 0 , because 0 multiplied is always 0
i = 1
while(i <= n):
    fact *= i
    i += 1
print("factorial of first : ", fact)

#same question using for loop

n = 9
fact = 1

for i in range(1,n+1):
    fact *= i
print("factorial of first : " , fact)
