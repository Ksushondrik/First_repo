class Pet:
    def __init__(self, name: str, age: int, color: str):
        self.name = name
        self.age = age
        self.color = color
        self.__count = 0
    
    def setCount(self, count:int):
        self.__count = count
        
    def voice(self, phrase: str):
        print(phrase)
    
    def walk(self,) -> str:
        return 'steps '*self.__count

# if __name__ == "__main__"    
#     pet1 = Pet('Atmo', 2, 'red')
#     pet1.voice('Mew')
#     pet1.setCount(12)
#     print(pet1.walk())