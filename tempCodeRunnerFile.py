class Bus:
    __volvo="" # Encapsuletion privet represent [__variable]

obj=Bus()
p=obj.__volvo
print(p)  # AttributeError: 'Bus' object has no attribute '__volvo'
