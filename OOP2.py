# del keyword
# used to delete object properties or object itself.

"""
del s1.name
del s1

"""

class Student:
    def __init__(self, name):
        self.name = name


s1 = Student("shradha")
print(s1.name)
del s1.name   # delete


# private(like) attributes & methods
# Conceptual Implementations in Python
# private attributes & methods are meant to be used only within the class and are not accessible from outside the class

"""
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.acc_pass = acc_pass


acc1 = Account("12345", "abcde")

print(acc1.acc_no)  # print both acc_no and acc_pass

"""
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass   # __acc_no is private

    def reset_pass(self):
        print(self.__acc_pass)   # it is inside class


acc1 = Account("12345", "abcde")

print(acc1.acc_no)    # print both acc_no and acc_pass
# print(acc1.__acc_pass)    # cannot access outside class
print(acc1.reset_pass())

# to private , we just put two underscore before attributes & methods

class Person:
    __name = "anonymous"    # conceptually private

    def __hello(self):      # private
        print("hello person")

    def welcome(self):   # can access outside, here is no __
       self.__hello()

p1 = Person()

print(p1.welcome())  # becomes public
# print(p1.__name)  # becomes private
# print(p1.__hello())  # becomes private



# 3. Inheritance
# when one class(child/derived) derives the properties & methods of another class(parent/base)

"""
class Car:

    ....


class ToyotaCar(Car):
    
    ....

"""

class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

print(car1.name)
print(car1.start())   # inheritance
print(car1.color)


# three types of inheritance
"""
1. single inheritance
--> single parent to single child 

class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

print(car1.name)
print(car1.start())   # inheritance
print(car1.color)


2. multi_level inheritance

-->parent to child, child becomes parent and that to another child

class Car:
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("diesel")
car1.start()


3. multiple inheritance

--> multiple parent to single child

class A:
    varA = "welcome to class A"

class B:
        varB = "welcome to class B"

class C(A, B):
     varC = "welcome to class C"

c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varA)


"""

# super method
# super() method is used to access methods of the parent class.

class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)    # super() method
        super().start()

car1 = ToyotaCar("Prius","electric")
print(car1.type)

# class method
# A class method is bound to the class & receive the class as an implicit first arguement.

# Note - static method can't access or modify class & generally for utility.

"""
class Student:
    @classmethod   # decorator
    def college(cls):
        pass

"""
class Person:
    name = "anonymous"

    def changeName(self, name):
        self.name = name
        # 1. Person.name = name     # indirect access
        # 2. self.__class__.name = "rahul kumar"   # indirect access

        @classmethod    # direct access 
        def changeName(cls, name):
            cls.name = name

p1 = Person()
p1.changeName("rahul kumar")
print(p1.name)
print(Person.name)


"""
1. static method (doesnot access or change attributes of both class or instance)
2. class method (cls)
3. instance method (self), normal method

"""

# property (decorator)
# we use @property decorator on any method in the class to use the method as a property.

class Student:
    def __init__(self, phy, chem, maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths
        # self.percentage = str((self.phy + self.chem + self.maths) / 3) + "%"

    # def calcPercentage(self):
        # self.percentage = str((self.phy + self.chem + self.maths) / 3) + "%"

    @property   # automatic change
    def percentage(self):
       return str((self.phy + self.chem + self.maths) / 3) + "%"

stu1 = Student(98,97,99)
print(stu1.percentage)

stu1.phy = 86 
# print(stu1.phy)
# stu1.calcPercentage()
print(stu1.percentage)

# we have more decorators 
"""
1. @getter
2. @setter

"""

# 4. polymorphism : operator overloading
# when the same operator is allowed to have different meaning according to the context.

"""
operators & dunder function

a + b   # addition        a. __add__(b)
a - b   # subtraction     a. __sub__(b)
a * b   # multiplication  a. __mul__(b)
a / b   # division        a. __truediv__ (b)
a % b   # addition        a. __mod__(b)

"""
# operator overloading of +

print(1 + 2)    # addition
print(type(1))

print("apna" + "college")   # concatenation
print(type("apna"))

print([1,2,3] + [4,5,6])   # merge
print(type([1,2,3]))


class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i +", self.img,"j")

    def __add__(self, num2):    # dunder function
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

    def __sub__(self, num2):    # dunder function
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)

num1 = Complex(1,3)
num1.showNumber()

num2 = Complex(2,5)
num2.showNumber()

num3 = num1 - num2
num3.showNumber()


# let's practice
# 1. define a Circle class to create a circle with radius r using the constructor. Define an Area() method of the class which calculates the area of the circle. Define a Perimeter() method of the class which allows you to calculate the parimeter of the circle.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius ** 2
    
    def perimeter(self):
        return 2 * (22/7) * self.radius

c1 = Circle(21)
print(c1.area())
print(c1.perimeter())


# 2. define a Employee class with attributes role, department & salary. This class also has a showDetails() method. Create an Engineer class that inherits properties from Employee & has additional attributes : name & age.


class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role = ", self.role)
        print("dept =", self.dept)
        print("salary =", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer","IT","75,000")

engg1 = Engineer("Elon Musk",45)
engg1.showDetails()

e1 = Employee("accountant","Finance","60,000")
e1.showDetails()


# 3. create a class called Order which stores item & its price. Use Dunder function __gt__() to convey that:  order1 > order2 if price of order1 > price of order2

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, odr2):
        return self.price > odr2.price

odr1 = Order("chips", 20)
odr2 = Order("tea", 15)

print(odr1 > odr2)







