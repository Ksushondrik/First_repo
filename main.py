print("Hello World!")

print("Hello Git")

#Python Core 2.0
#на практиці пробую приклади з конспекту

#Периметр квадрата

#a = float(input("Введіть сторону квадрата a: "))
#P = 4 * a
#print(f"Периметр кавдрата дорівнює {P}")

#Вартість їжі для кава-брейків

#Встановлюємо ціни на продукти
#price_per_croissant = 1.04
#price_per_glass = 0.34
#price_per_coffee_pack = 4.42

#Кількість кожного продукту
#num_croissants = int(input("Введіть кількість круасанів: "))
#num_glasses = int(input("Введіть кількість склянок: "))
#num_coffee_packs = int(input("Введіть кількість упаковок кави: "))

#Обчислення загальної вартості
#total_cost = num_croissants * price_per_croissant + \
#            num_glasses * price_per_glass + \
#            num_coffee_packs * price_per_coffee_pack

#Визначаємо кількість повних доларів і центів
#total_dollars=int(total_cost)
#total_cents=int(total_cost*100)

#Вивід результату
#print(f"Загальна вартість у повних доларах: {total_dollars} доларів.")
#print(f"Загальна вартість у центах: {total_cents} центів.")

#f-рядки
#num_1=int(input("Введіть перше ціле число: "))
#num_2=int(input("Введіть друге ціле число: "))
#print(f"{num_1}+{num_2}={num_1+num_2}")
#print(f"{num_1}-{num_2}={num_1-num_2}")
#print(f"{num_1}*{num_2}={num_1*num_2}")
#print(f"{num_1}/{num_2}={num_1/num_2}")

#f-рядки 2
#name=input("Введіть Ваше ім'я: ")
#last_name=input("Введіть Ваше прізвище: ")
#full_name=f"Ваше ім'я: {name} {last_name}"
#print(full_name)

# Множини
#add(elem) — додає елемент у множину
numbers = {1, 2, 3}
numbers.add(4)
print(numbers)  # {1, 2, 3, 4}
#remove(elem) — видаляє елемент із множини, викликає виняток, якщо такого елемента немає
numbers = {1, 2, 3}
numbers.remove(3)
print(numbers)  # {1, 2}