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
    def area(Shape):
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




                                ## Method Overriding ##

class Devise:
   def __init__(self): #constructor
     print("I am a devise class")
     
class Laptop(Devise):
    def __init__(self):
        super().__init__()  
        print("I am in Laptop class")
        
D = Laptop()
