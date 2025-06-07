# Object Oriented Programming in Python
# Classes and Objects

'''class Car():
    a = 10
c1 = Car()
print(c1.a)
'''
'''
class Car():
    a = 'raman'
c1 = Car()
print(c1.a.upper())
c1.a = 'kumar'
print(c1.a.upper())
'''
'''
class Counting:
    count = 0
    
    def counts(self):
        self.count = self.count + 1
        print(f"Count :{self.count}")
c1 = Counting()
c1.counts()
c1.counts()
'''

# Class with Constructor and Destructor

'''
class Car:
    def __init__(self, name , type):
        self.name = name
        self.type = type
        print("Constructor called")
    def __del__(self):
        print("Destructor called")
c1 = Car("BMW", "SUV")
print(c1.name)
print(c1.type)
c2 = Car("Audi", "Sedan")
print(c2.name)
print(c2.type)
'''


        # Function and Class with same name
'''
def c1(x):
    print("Hello", x)
c1("Jim")
c1("Bob")

class C1:
    def __init__(self, x):
        self.x = x
        print("Hello", self.x)
c2 = C1("Jim")
c3 = C1("Bob")

'''

#Inheritance

'''
class name:
    def __init__(self, z):
        x = 10
        self.name = z
        print("Name:", self.name)
        
class football_fans(name):
    def pts(self , x):
        self.x = x
        print("Points:", self.x)
x1 = name("Raman")
x2 = football_fans("Kumar")
x2.pts (100)

'''

#Single Inheritance
'''
class A:
    def state_1(self):
        print("State 1")
    def state_2(self):
        print("State 2")
    def state_3(self):
        print("State 3")
class B(A):
    def state_4(self):
        print("State 4")
    def state_5(self):
        print("State 5")
a = A()
a.state_1()
a.state_2() 
a.state_3()
b = B()
b.state_4()
b.state_2()
'''

#Multiple Inheritance
'''
class A:
    def state_1(self):
        print("State 1")
class B(A):
    def state_4(self):
        print("State 4")
class C(B):
    def state_5(self):
        print("State 5")

c1 = C()
c1.state_1()
c1.state_4()
c1.state_5()
'''

#multilevel Inheritance
'''
class A:
    def state_1(self):
        print("State 1")
class B():
    def state_2(self):
        print("State 2")
class C(A, B):
    def state_3(self):
        print("State 3")
        
c1 = C()
c1.state_1()
c1.state_2()  
c1.state_3()

'''
#Operator Overloading
'''
class Vegetable:
    def __init__(self , carrot , potato):
        self.carrot = carrot
        self.potato = potato
    def __add__(self, other):
        self.carrot = self.carrot + other.carrot
        self.potato = self.potato +  other.potato
        return Vegetable(self.carrot, self.potato)
        
v1 = Vegetable(10, 20)
v2 = Vegetable(30, 40)
v3 = v1 + v2
print("Carrot:", v3.carrot)
print("Potato:", v3.potato)
'''

#Data Hiding
'''
class simple:
    def __init__(self):
        self.__x = 10
        self.y = 20
    def __value_1(self):
        print("Value of x:", self.__x)
    
    def value_2(self):
        print("Value of y:", self.y)
        
s1 = simple()
print(dir(s1))
print(s1._simple__x)  # Accessing private variable using name mangling
# print(s1.__x)
# s1.value_1()
print(s1._simple__value_1())# Accessing private method using name mangling
# s1.value_2()
s1.value_2()  # Accessing public method

'''