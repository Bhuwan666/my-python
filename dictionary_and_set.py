# dictionary in python
# used to store data values in key:value pairs
# they are unordered, mutable(cheangeable) & don't allow duplicate keys

info = {
    "key" : "value",
    "name" : "ale",
    "subjects" : ["Python", "SQL", "Numbpy", "Pandas"], #lists
    "topics" : ("dict","set"), #tuples
    
    "learning" : "coding",
    "age" : 35, # integer
    "is_adult" : True, # boolean
    "marks" : 94.4,
    5 : 6, # key can be integer
    5.5 : 51 # key can be float
}

print(type(info))
print(info)

# we can print individual values
print(info["name"])
print(info["subjects"])
print(info["age"])

# we can assign 

info["name"] = "ashok"  # new values
info["surname"] = "ale"  # new key : value pair
print(info)

# we can create null dictionary

null_dict = {}
null_dict["name"] = "barsha"  # add new key:value
null_dict["surname"] = "ale"
print(null_dict)

# nested dictinary

student = {
    "name" : "  ashok ale",
    "subjects" : {
        "maths" : 85,
        "science" : 86,
        "english" : 88
    }
}
print(student["subjects"]["science"])  # print nested dictinary

# dictionary methods

# 1. myDict.keys()  #returns all keys

student = {
    "name" : "ashok ale",
    "subjects" : {
        "maths" : 89,
        "science" : 88,
        "english" : 85
    }
}
print(student.keys())   #returns all keys
print(list(student.keys()))  # to type cast list 


# to find total number of keys
# 1. 
print(len(student))
# or we can 2. 
print(len(list(student.keys())))


# 2. myDict.values()  #return all values
print(student.values())
print(list(student.keys()))  # to type cast into list

# we can store list inside dict , and vice versa


# 3. myDict.items()  #returns all (key, val) pairs as tuples
print(student.items())
print(list(student.items()))  # to type cast into list

pairs = list(student.items())  # to access
print(pairs[0])


# 4. myDict.get("key")  # returns the key according to value
print(student.get("name"))


# 5. myDict.update( newDict )  # inserts the specified items to the dictionary
student.update({"city" : "london"})
print(student)


# sets in python
# collection of the unordered items.
# each element in the set must be unique & immutable
# sets = mutable
# sets_elements = immutable

# we can store boolen, int, float, str, tuple but we cannot store list and dict bacause they are mutable

collection = {1,2,3,4,"hello",8, "world", 1,1,2,2,2,5} # set ignore duplicate values

print(collection)
print(type(collection))
print(len(collection))  # total number of items

collection2 = {}  #empty dictionary
print(type(collection2))

collection3 = set()  #empty set
print(type(collection3))


 # set methods

collection = set()
collection.add(1) # adds an element
collection.add(2)
collection.add("apna_college")
collection.add((1,2,3))
# collection.add([1,2,3])   # we cannot add list

collection.remove(2)  # removes the element 
# collection.clear()  # empties the set




print(collection)
print(type(collection))


collection2 = {"hello","who","are","you"}
print(collection2.pop())  # removes a random value
print(collection2.pop())  # removes a random value

set1 = {1,2,3}
set2 = {3,4,5}

print(set1.union(set2))  # {1,2,3,4,5}  union
print(set1.intersection(set2))  # {3}  intersection


# practice question

# 1. store following word meanings in a python dictionary :
#    table : "a piece of furniture", "list of facts & figures"
#    cat : "a small animal"

pyDict = { 
    "table" : ["a piece of furniture" , " list of facts & figures"],
    "cat" : "a small animal"
    
}
print(pyDict)
print(type(pyDict))


# 2. you are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.

# "python","java", "C++","python","javascript","java","python","java","c++","c"

subjects = {
    "python","java", "C++","python","javascript","java","python","java","C++","c"
}

print(subjects)
print(len(subjects))

# 3. wap to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.

marks = {}

x = int(input("enter marks of maths : "))
marks.update({"maths" : x})
y = int(input("enter marks of science : "))
marks.update({"science" : y})
z = int(input("enter marks of english : "))
marks.update({"english" : z})

print(marks)
print(type(marks))

# 4. figure out a way to store 9 & 9.0 as separate values in the set. (you can take help of built-in data types)

set3 = {9,9.0}
print(set3) # it will print only 9

set4 = {9, "9.0"}  # one way
print(set4)

set5 = {   # other way
    ("float",9.0),
    ("int",9)
}
print(set5)