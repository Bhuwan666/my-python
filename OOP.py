# OOP in python
# to map with real world scenarios, we started using objects in code.
# this is called object oriented programming.

# class & object in Python
# class is a blueprint for creating objects


# creating class
 
"""
class Student:        # class className:
    name = " Ashok Ale"

"""

# creating object (instance)

"""
s1 = Student()     # obj_var = className()
print(s1.name)

"""
class Student:
    name = "Ashok Ale"

s1 = Student()
print(s1.name)    # name same for every student

s2 = Student()
print(s2.name)


class Car:
    color = "blue"
    brand = "mercedes"

car1 = Car()
print(car1.color)
print(car1.brand)


# __init__ function
# Constructor
# all classes have a function called _init_(), which is always executed when the object is being initiated.

# creating class

"""
class Student:
    def __init__(self, name, marks):      # automatically invoked or called
        self.name = name
        self.marks = marks
        print("adding new students in database")

"""

# creating object

"""
s1 = Student("Karan", 98)
print(s1.name, s1.marks)

s2 = Student("Arjun", 88)
print(s2.name, s2.marks)


"""

# the self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

class Student:
    college_name = "ABC college"
    name = "anonymous"  # class attribute

    # default constructor
    def __init__(self, name, marks):      # automatically invoked or called
        pass

    # parameterized constructor
    def __init__(self, name, marks):      # automatically invoked or called
        self.name = name  # obj attribute > class attr
        self.marks = marks
        print("adding new students in database")


s1 = Student("Karan", 98)
print(s1.name, s1.marks)

s2 = Student("Arjun", 88)
print(s2.name, s2.marks)

print(Student.college_name)


# class & instance attributes

"""
class.attr   # same for all objects
obj.attr   # diff for each objects

"""

# methods
# methods are functions that belong to objects.

# creating class

"""
class Student:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print("hello", self.name)

"""

# creating object

"""
s1 = Student("Karan")
s1.hello()

"""

class Student2:    # define class
    college_name = "ABC college"  # class attri

    def __init__(self, name, marks):    # define constructor 
        self.name = name    # obj attr
        self.marks = marks

    def welcome(self):     # method1
        print("welcome student,", self.name)

    def get_marks(self):    # method2
        return self.marks
    


s1 = Student2("Ashok", 97)   # create objects
s1.welcome()    # call method1
print(s1.get_marks())  # call method2


# let's practice
# 1. create student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average.

class Student:  # create class

    def __init__(self, name, marks):  # create constructor
        self.name = name   # define
        self.marks = marks

    def get_avg(self):  # define method
        sum = 0   # create loop
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg score is:", sum/3)

s1 = Student("tony stark", [99,98,97])  # object attr
s1.get_avg()

s1.name = "ironman"   # changing/manipulating attribute
s1.get_avg()


# static methods
# methods that don't use the self parameter (work at class level)

"""
class Student:
    @staticmethod  # decorator
    def college():
        print("ABC College")

Decorators allow us to wrap another function in order to extend the bahaviour of the wrapped function, without permanently modifying it


"""
class Student:  # create class


    def __init__(self, name, marks):  # create constructor
        self.name = name   # define
        self.marks = marks

    @staticmethod   # decorator
    def hello():
        print("hello")

    def get_avg(self):  # define method
        sum = 0   # create loop
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg score is:", sum/3)

s1 = Student("tony stark", [99,98,97])  # object attr
s1.get_avg()

s1.name = "ironman"   # changing/manipulating attribute
s1.get_avg()

s1.hello()




# important
# 1. abstraction
# hiding the implementation details of a class and only showing the essential features to the user.

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("car started..")

car1 = Car()
car1.start()




# 2. encapsulation
# wrapping data and functions into a single unit 

# let's practice

# 1. create account class with 2 attributes - balance & account no. create methods for debit, credit & printing the balance.

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    # debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("total balance =", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("total balance =", self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)
acc1.debit(10000)


# 3. inheritance
# 4. polymorphism