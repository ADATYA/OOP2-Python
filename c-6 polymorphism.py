                                        ## polymorphism ##
# polymorphism : means same function name (but differten signatures) bring user for different types.
# funcrion overloding / overriding

list=[10,20,30,40]
print(len(list))

string="sporsho"
print(len(string))

                        # function Overloding#
#function name same rhakbe but parameter change kora alada result asbe.

class adi:
    def display3(self,name=""):
        print("Bikrom adatya roy " + name)

obj=adi()
obj.display3()
obj.display3('learn python oop')

                                # function Overriding#
class bireswer:
    def display01(self):
        print('Bikrom roy is Bireswer roys son')

class bikrom(bireswer):
    def display01(self):
        super().display01()  # use supper keyword to display parents value
        print("Bireswer roy is bikroms father")

obj=bikrom()
obj.display01()
obj.display01()

                                        # Class 02 (Overloding / overriding)
# Overloding :
class area:
    def find_area(self,x=None,y=None):

        if x!=None and y!=None:
            print(x*y)
        elif x!=None:
            print(x*x)
        else:
            print("Nothing")

obj=area()
obj.find_area()
obj.find_area(10)
obj.find_area(10,20)

                                                # Overriding
class a:
    def showData(self):
        print("I am in A class")

class b (a):
    def showData(self):
        print("I am in B class")

obj= b()
obj.showData()