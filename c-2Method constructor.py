# Method:

class car:
    a=10
    def __init__(self):  # Constructor:ek call nah korrleo print korte pare
        print("Adatya is learning python")

    def bus(self):
        print(self.a)
        self.c = self.a*self.a # [c=a*a]
        print(self.c)
    
    
    def truck(self,a,b): ## argument(self,a,b)
        print(a+b)
        print("Bikrom is typing code")
    

obj=car() #class
obj.bus() #object
obj.truck(20,30)





