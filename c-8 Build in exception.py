'''
There is two kind of exception, 
1. Syntex error 
2. Logical error
'''

# 1.Syntex Error : Syntex error aka aka thik hoy nah ok thik kore nite hoy.

a=19
b=40
if a==b:
  print("This is if")  # SyntaxError: expected ':'
else:
  print("This is else")

# Note: python code print one by one line (Interpreted) thats why the code dose not work next line.



# 2.Logical Error : 

d=23
f=34
# print(d/0) # ZeroDivisionError: division by zero

i=[10,20,30]
print(i[7])   # IndexError: list index out of range