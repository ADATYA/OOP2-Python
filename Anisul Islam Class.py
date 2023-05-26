                                    ## Inheritance ##


class Car:
    def engine(self):
        print("This is engine")
    def wheel(self):
        print("This is wheel")

 # class
class BMW(Car):
    # method
    def color(self):
        print("This is white bmw")
#     def wheel(self):
#         print("This is bmw wheel")
#     def engine(self):
#         print("This is bmw engine")
# #object :
# c = Car()
# c.engine()
# c.wheel()


bmw = BMW() 
bmw.color()
bmw.engine()
y=issubclass(Car,BMW)
print(y)


## Practic...

class Shape:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def area(self):
        print("I am area method of shape class")


class Triangle(Shape):
    def area(self):
        area = 0.5* self.name * self.id
        print("area of Triangle :" , area)


class Rectangle(Shape):
    def area(self):
        area =self.name * self.id
        print("area of Rectangle :" , area)

t1 = Triangle(20,30)
t1.area()

r1 = Rectangle(20,30)
r1.area()


class Person:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def printto(self):
        print("This is Perrson class")

class Ankur:
    def printto(self):
        printto = "His name is Ankur"
        print("Name is :",printto)

class Bikrom:
    def printto(self):
        printto = "His name is Bikrom"
        print("Name is :",printto)
A = Ankur()
A.printto()

B=Bikrom()
B.printto()

                                ## Method Overriding ##

class Devise:
   def __init__(self): #constructor
     print("I am a devise class")
     
class Laptop(Devise):
    def __init__(self):
        super().__init__()  
        print("I am in Laptop class")
        
D = Laptop()


                                ## Exception Handling ##

## Type,syntex,value,Zero,Syntex,out of bound Error..

##1
try:
    list = [20,0,30]
    a=(list[4])
    print(a)
except IndexError:
    print("This is exception")
    print("This is out of exception")
finally:
    print("This is finaly and it is always printed")
##2
try:
    list = [12,20,2,0]
    i = (list[1])/list[3]
    print(i)
except ZeroDivisionError:
    print("Devideng by zero is not posiable")
finally:
    print("Finally is always exicuted before exception")

##2
try:
    a = int(input("Enter number :"))
    s = int(input("Enter number :"))
    r = a/s
    print(r)
except(IndexError,ValueError):
    print("This is Error input")
finally:

 print("Succesfully Exicute!!!")


                    ### Encapsulation ###
