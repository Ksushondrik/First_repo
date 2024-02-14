from dataclasses import dataclass

@dataclass
class heart:
    def __init__(self, value:int):
        self.value=value

    def __eq__(self, outer) :
        return self.value==outer.value
    


# a = heart(3)
# b = heart(3)
# print(a==b)
    
a = heart(3)
b = a
a.value = 5
print(b.value)
print(a.__eq__(b))