# Class : class is a [blueprint].
# Shudu class banale hobe nah tar ekta object banano lagbe then oita call korte hobe.
# Akti class er [multiple object] thke.
# [camel] case : BikromRoy
# #class err vator jaita banai tak e [method]bole 

class Car:
    a=10
# Method/funtion
    
    def add(self):     # Class er vator function banate gele akta argument pass korte hobe [self] / eri akta object err moto kaj kore.
        print("Bikrom is learning OOP")
    
    #    [ for i in Car:   TypeError: 'type' object is not iterable
    #         print(i)]
          

# create a class object
Car1=Car()
Car2=Car()
print (Car.a)
print(Car2.a)
Car1.add()  #  object diye printt korbo
