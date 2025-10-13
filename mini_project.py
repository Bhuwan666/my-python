# 1. guess the number

import random

target = random.randint(1, 100)

while True:
    userChoice = input("Guess the target or Quit(Q) : ")
    if(userChoice == "Q"):
        break

    userChoice = int(userChoice)
    if(userChoice == target):
        print("Success : Correct Guess!!!")
        break
    elif(userChoice < target):
        print("your number was too small. Take a bigger guess...")
    else: 
        print("your number was too big. Take a smaller guess...")

print("-----GAME OVER------")


# 2. random password generator

import random
import string

pass_len = 8
charValues = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(pass_len):
    password += random.choice(charValues)

print("your random password is :", password)

"""
other way
1. list comprehension [function for i in range(n)]

res = [random.choice(charValues) for i in range(pass_len)]
print(res)

"""

"""
other way
2. res = "".join([random.choice(charValues) for i in range(pass_len)])
print(res)

"""
