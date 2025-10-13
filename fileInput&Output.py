# file I/O in python 
# python can be used to perform operations on a file. (read & write data)

# types of all files

# 1. Text Files : .txt, .docx, .log etc.
# 2. Binary Files : .mp4, .mov, .png, .jpeg etc.

"""

# open, read & close file
# we have to open a file before reading or writing.

# f = open("file_name","mode")

# file_name --> sample.txt , demo.docx
# mode --> r : read mode, w : write mode    # by default read

# data = f.read()
# f.close()

"""

f = open("demo.txt","r")
data = f.read()    # reads entire file

# data = f.read(5)  # reads only 5 spaces
 
# data = f.readline()  # reads one line at a time

print(data)
print(type(data))
f.close()

"""
r - open for reading(default)
w - open for writing, truncating the file first
x - create a new file and open it for writing
a - open for writing, appending to the end of the file if it exists
b - binary mode
t - text mode(default)
+ - open a disk file for updating(reading and writing)

"""

f = open("demo.txt","r")
data = f.read(5)
print(data)
print(type(data))
f.close()


f = open("demo.txt","r")


""" 
data = f.read()   # nothing to print if already read
print(data)

"""

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

line3 = f.readline()
print(line3)
print(type(data))

f.close()



# writing to a file


"""
f = open("demo.txt","w")
f.write("this is a new line")   # overwrites the entire file


f = open("demo.txt","a")
f.write("this is a new line")   # adds to the file

"""

f = open("demo.txt","w")   # overwrites data
f.write("I want to learn pandas tomorrow")
f.close()

f = open("demo.txt","a")   # adds new data
f.write("\nThen i will learn numpy")
f.close()

f = open("sample.txt","w")  # automatically creates new file  in 'w' or 'a'
f.close()

# reading and writing simultaneosly --> different types

# 1. r+  --> can read and write existing data(pointer is at the start), no truncate

f = open("demo.txt","r+")  # overwrites data from the front
f.write("abc")
print(f.read())   # starts print from where it is printed
f.close()

# 2. w+   --> can read and overwrite, truncate

f = open("demo.txt","w+")   # all truncated
print(f.read())
f.write("def")   # now i can write something new
f.close()

# 3. a+  --> can read and append, no truncate(pointer at the end)

f = open("demo.txt","a+")
print(f.read())  # nothing prints , because it prints at the end of the pointer
f.write("ghi")   # data will append not overwrite
f.close()


# with syntax

"""
syntax

with open("demo.txt","a") as f:
    data = f.read()

"""

with open("demo.txt","r") as f:   # as = alias , i.e. ironman || tony stark

    data = f.read()
    print(data)
# when we use with, no need to close file, it automatically closes file

with open("demo.txt","w") as f:
    f.write("new data")


# deleting a file

# using the os module

# module (like a code library) is a file written by another programmer that generally has a funcions we can use.

"""
import os   # os = operating system
os.remove("filename")

"""
import os     # to install module , --> pip install tensorflow, pip / pip3

os.remove("demo.txt")


# let's practice

# 1. create a new file "practicey.txt" using python. Add the following data in it:

"""
Hi everyone
we are learning File I/O
using Java.
I like programming in Java.

"""

with open("practicey.txt","w") as f:
    f.write("Hi everyone\nwe are learning File I/O\n")
    f.write("using Java.\nI like programming in Java.")


# 2.  waf that replaces all occurances of "Java" with "python" in above file.

with open("practicey.txt","r") as f:
    data = f.read()

new_data = data.replace("Java","Python")
print(new_data)   # print answer in terminal

with open("practicey.txt","w") as f:
    f.write(new_data)   # print answer in practicey.txt file


# 3. search if the word "learning" exists in the file or not

def check_for_word():  # using function
    word = "learning"
    with open("practicey.txt","r") as f:
        data = f.read()
        if(data.find(word) != -1):  # or # if (word in data):   # if -1 doesnot come , its a valid index
            print("Found")
        else:
            print("not found")

check_for_word()  # calling function


# 4. waf to find in which line of the does the word "learning" occur first. print-1 if word not found.

def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practicey.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
            line_no += 1  

    return -1

print(check_for_line())
        
# 5. from a file containing numbers separated by comma, print the count of even numbers.

count = 0
with open("practicey.txt","r") as f:
    data = f.read()
    

    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1
   
print(count) 
       






