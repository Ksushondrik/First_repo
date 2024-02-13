# class Pokemon:
#     def __init__(self, name, type, health):
#         self.name = name
#         self.type = type
#         self.health = health

#     def attack (self, other_pokemon):
#         print(f"{self.name} attacks {other_pokemon.name}!")

#     def dodge(self):
#         print(f"{self.name} dodged the attack!")

#     def evolve(self, new_form):
#         print(f"{self.name} is evolving into {new_form}!")
#         self.name = new_form

# pikachu = Pokemon("Pikachu", "Electric", 100)

# pikachu.attack(Pokemon("Charmander", "Fire", 100))
# pikachu.dodge()
# pikachu.evolve("Raichu")

# class A:

# class Animal:
#     def __init__(self, nickname: str, age: int):
#         self.nickname = nickname
#         self.age = age

#     def make_sound(self):
#         pass

# class Cat(Animal):
#     def make_sound(self):
#         return "Meow"

# class Dog(Animal):
#     def make_sound(self):
#         return "Woof"

# def animal_sounds(animals):
#     for animal in animals:
#         print(animal.make_sound())

# animals = [Cat("Simon", 4), Dog("Rex", 5)]
# animal_sounds(animals)

# class Duck:
#     def quack(self):
#         print("Quack, quack!")

# class Person:
#     def quack(self):
#         print("I'm Quacking Like a Duck!")

# def make_it_quack(duck):
#     duck.quack()

# duck = Duck()
# person = Person()

# make_it_quack(duck)
# make_it_quack(person)

# from enum import Enum, auto
# from typing import Any

# class OrderStatus(Enum):
#     NEW = auto()
#     PROCESSING = auto()
#     SHIPPED = auto()
#     DELIVERED = auto()

# class Order:
#     def __init__(self, name: str, status: OrderStatus):
#         self.name = name
#         self.status = status

#     def update_status(self, new_status: OrderStatus):
#         self.status = new_status
#         print(f"Замовлення '{self.name}' оновлено до статусу {self.status.name}.")

#     def display_status(self):
#         print(f"Статус замовлення '{self.name}' : {self.status.name}.")

# order1 = Order("Ноутбук", OrderStatus.NEW)
# order2 = Order("Книга", OrderStatus.NEW)

# order1.display_status()
# order2.display_status()

# order1.update_status(OrderStatus.PROCESSING)
# order2.update_status(OrderStatus.SHIPPED)

# order1.display_status()
# order2.display_status()

# class AgeVerificationError(Exception):
#     def __init__(self, message = "Вік не задовольняє мінімальній вимозі"):
#         self.message = message
#         super().__init__(self.message)

# def verify_age(age: int):
#     if age < 18 :
#         raise AgeVerificationError("Вік особи менший за 18 років")

# if __name__ == "__main__" :
#     try:
#         verify_age(20)
#     except AgeVerificationError as e:
#         print(f"Виняток: {e}")
#     else:
#         print("Вік перевірено, особа доросла.")

class NameTooShortError(Exception):
    pass

class NameStartsFromLowError(Exception):
    pass

def enter_name():
    name = input("Enter name: ")
    if len(name) < 3 :
        raise NameTooShortError("Name is too short, need more than 2 symbols")
    if not name[0].isupper():
        raise NameStartsFromLowError("Name should start from capital letter")
    return name

if __name__ == "__main__" :
    try:
        name = enter_name()
        print(f"Hello, {name}")
    except (NameTooShortError, NameStartsFromLowError) as e :
        print(e)

