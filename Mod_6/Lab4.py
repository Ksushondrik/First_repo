class Animal:
    RED = 4
    GRAY = 3
    WHITE = 2
    BLACK = 1
    MULTI = 0
    
    def __init__(self, age, type, color):
        self.age = age
        self.type = type
        if color in (range(5)):
            self.color=color
        else:
            raise(Exception("Varning! Error"))
        
    def print(self):
        print(f"age: {self.age}, type: {self.type}, color: {self.color}")

dog = Animal(10, 'dog', 6)
dog.print()