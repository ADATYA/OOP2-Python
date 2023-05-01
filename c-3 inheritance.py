            ## Inheritance ## 

#2 ba er basi class thakte pare.
# parent class ke child e nite pari eikhane sudu inherit hobe take call korle parent soho sob peint korbe.

#  Type of inheritance : 1. Single 2.Multiple 3.Multilevle 

# 1. Single : 
class car:
    def display1(self):
        print("This is a car class")
class bike(car): # this parinthasis is represent the inherit class 

    def display2(self):
        print("This is bike class but inherit car class")

obj=bike() # call the class bike ah inherit in class car
obj.display1 ()
obj.display2 ()

print()

# 2.Multilevel :

class car:
    def display1(self):
        print("This is a car class")
class bike(car): # this parinthasis is represent the inherit class 

    def display2(self):
        print("This is bike class but inherit car class")
class bus(bike):
    def display3(self): #  this self argu. is most impt.
        print("This is class bus and inhaerit bike class")


obj=bus() # call the class bike ah inherit in class car
obj.display1 ()
obj.display2 ()
obj.display3 ()


print()

# 3.Multiple :
# Note : Multiple are supported in python 

class car:
    def display1(self):
        print("This is a car class")
class bike: # this parinthasis is represent the inherit class 

    def display2(self):
        print("This is bike class but inherit car class")
class bus(car,bike):
    def display3(self): #  this self argu. is most impt.
        print("This is class bus and inhaerit bike class")


obj=bus() # call the class bike ah inherit in class car
obj.display1 ()
obj.display2 ()
obj.display3 ()