                        ## Encapsulation ##

# An object variable should not always be directly accessable.
#This method can ensure the correct values are set.If an incorrect value is set the method can return an error.
# class er vator use kora jay but class er bire use kora jay nah
#

# class Bus:
#     __volvo="" # Encapsuletion privet represent [__variable]

# obj=Bus()
# p=obj.__volvo
# print(p)  # AttributeError: 'Bus' object has no attribute '__volvo'


## use as a variable
class Bus:
    volvo="This is a volvo bus" # Encapsuletion privet represent [__variable]

obj= Bus()
p=(obj.volvo)
print(p)

print()

## use as a constractor.
class Bus:
    __volvo="Volvo is great" # Encapsuletion privet represent [__variable]

#[create a constructor]
    def __init__(self):
        print(self.__volvo)

obj=Bus() # call the object

print()

## use as a privet method:

class car:
    __bmw="I love to drive bmw"

    def __init__(self):  ## constructor
        print(self.__bmw)
        self.__display1() ## automaticly print hoye jabe
    def __display1(self):
        print('I love to write python code')
obj=car()
# obj.__display1() ## call the privet function// direct access kora jay nah


class Pharmacy:
    __medicin="This is a drug to save our life"

    # create a constructor
    def __init__(self):
        print(self.__medicin)

obj=Pharmacy()
    # obj.__medicin

class mobile:
    __name="I am carry redme"

    def __init__(self):
        print(self.__name)
        self.__display101() 
    def __display101(self):
        print("April is full of hot summer")

obj= mobile()
# obj.__display101()