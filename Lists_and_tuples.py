# lists in python
# built-in data types that stores set of values.It can store elements of different types (integer,float,string,etc.)
marks = [98.2,89.5,88.5,78.6,99.8]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])

# we can store multiple types of data types 
student = ["Bhuwan",26,"Gorkha"]
print(type(student))
print(len(student))

# we cannot change/mutate in strings
# we can change/mutate in lists

print(student[0])
student[0] = "Barsha"
print(student)

# list slicing
# similar to string slicing

marks2 = [87, 64, 33, 95, 76]
print(marks2[1:4])
print(marks2[:4])
print(marks2[2:])
print(marks2[-3:-1])


# list methods 

list = [2,1,3]

list.append(4) # adds one element at the end
print(list)

list.sort() # sorts in ascending order
print(list)

list.sort(reverse=True) # sorts in descending order
print(list)

list.reverse() # reverses list
print(list)

list.insert(2,0) # insert element at index
print(list)

list.remove(1) # removes first occurance of element
print(list)

list.pop(3) # removes elements at index
print(list)

# there are many more list methods

# tuples in python
# built-in data types that lets us create immutable sequences of values
# instead of [] we use ()

tup = (2,1,3,1)
# print(tup[0]) # not allowed in tuple

# types of tuple

# 1. empty tuple
tup = ()
print(tup)
print(type(tup))

# 2. single value tuple
# we always use tuple like tup(1,) 
tup1 = (1,)
print(tup1)
print(type(tup1))
# if we don't use comma then the type will be int, float or string

tup1 = (1)
print(tup1)
print(type(tup1)) # int

tup1 = (1.2)
print(tup1)
print(type(tup1)) # float

tup1 = ("hello")
print(tup1)
print(type(tup1)) # string

# but tup like 
# 1. eg 1
tup2 = (1,2,3,4,)
print(tup2)
print(type(tup2))

# 2. eg 2
tup3 = (1,2,3,4)
print(tup3)
print(type(tup3))
# both eg are same , using comma at the last is optional

# slicing in tuple is same as slicing in list

tup4 = (1,2,3,4,5)
print(tup4[1:3])


# tuple methods

tup = (1,2,3,4,5,1,1,1)

print(tup.index(2)) # returns index of first occurance , here 2 is index(element)
print(tup.count(1)) # counts total occurance


# practice question

# 1. wap to ask the user to enter names of their 3 favourite movies & store them in a list.

# answer 1
name1 = str(input("enter name of first movie : "))
name2 = str(input("enter name of second movie : "))
name3 = str(input("enter name of third movie : "))

list = [name1, name2, name3]
print(list)

# answer 2 yt
movies = []
movie1 = input("enter 1st movie : ")
movie2 = input("enter 2nd movie : ")
movie3 = input("enter 3rd movie : ")

movies.append(movie1)
movies.append(movie2)
movies.append(movie3)

print(movies)

# 2. wap to check if a list contains a palindrome of elements. (hint:use copy() method)

list1 = [1,2,1]
list2 = [1,2,3]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("not palindrome")


# 3. wap to count the number of students with the "A" grade in the following tuple.

grade = ("C", "D", "A","A","B","B","A")
print(grade.count("A"))

# store the above values in a list & sort them from "A" to "D"

grade2 = ["C", "D", "A","A","B","B","A"]
grade2.sort()
print(grade2)