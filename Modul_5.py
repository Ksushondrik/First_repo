# from collections import defaultdict
#
# d = defaultdict(list)
# d['a'].append(1)
# d['a'].append(2)
# d['b'].append(3)
# print(d)
#
# c = defaultdict(int)
# c['a'] += 1
# c['b'] += 1
# c['a'] += 1
# print(c)
#
# words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
# grouped_words = defaultdict(list)
# for word in words:
#     char = word[0]
#     grouped_words[char].append(word)
# print(dict(grouped_words))
#
# # Створення стеку
# def create_stack():
#     return []
#
# # Перевірка на порожнечу
# def is_empty(stack):
#     return len(stack) == 0
#
# # Додавання елементу
# def push(stack, item):
#     stack.append(item)
#
# # Вилучення елементу
# def pop(stack):
#     if not is_empty(stack):
#         return stack.pop()
#     else:
#         print("Стек порожній")
#
# # Перегляд верхнього елемента
# def peek(stack):
#     if not is_empty(stack):
#         return stack[-1]
#     else:
#         print("Стек порожній")
#
#
# stack = create_stack()
# push(stack, 'a')
# push(stack, 'b')
# push(stack, 'c')
#
# from collections import deque
# # Створення черги
# queue = deque()
# # Enqueue: Додавання елементів
# queue.append('a')
# queue.append('b')
# queue.append('c')
# print("Черга після додавання елементів:", list(queue))
# # Dequeue: Видалення елемента
# print("Видалений елемент:", queue.popleft())
# print("Черга після видалення елемента:", list(queue))
# # Peek: Перегляд першого елемента
# print("Перший елемент у черзі:", queue[0])
# # IsEmpty: Перевірка на порожнечу
# print("Чи черга порожня:", len(queue) == 0)
# # Size: Розмір черги
# print("Розмір черги:", len(queue))
#
# from collections import deque
# # Список завдань, де кожне завдання - це словник
# tasks = [
#     {"type": "fast", "name": "Помити посуд"},
#     {"type": "slow", "name": "Подивитись серіал"},
#     {"type": "fast", "name": "Вигуляти собаку"},
#     {"type": "slow", "name": "Почитати книгу"}
# ]
# # Ініціалізація черги завдань
# task_queue = deque()
# # Розподіл завдань у чергу відповідно до їх пріоритету
# for task in tasks:
#     if task["type"] == "fast":
#         task_queue.appendleft(task)  # Додавання на високий пріоритет
#         print(f"Додано швидке завдання: {task['name']}")
#     else:
#         task_queue.append(task)  # Додавання на низький пріоритет
#         print(f"Додано повільне завдання: {task['name']}")
# # Виконання завдань
# while task_queue:
#     task = task_queue.popleft()
#     print(f"Виконується завдання: {task['name']}")
#
# print(0.1 + 0.2 == 0.3)
# print(0.1 + 0.2)
#
# from decimal import Decimal, ROUND_DOWN
# # Вихідне число Decimal
# number = Decimal('3.14159')
# # Встановлення точності до двох знаків після коми
# rounded_number = number.quantize(Decimal('0.00'), rounding=ROUND_DOWN)
# print(rounded_number)
#
# import decimal
# from decimal import Decimal
# number = Decimal("1.45")
# # Округлення за замовчуванням до одного десяткового знаку
# print("Округлення за замовчуванням ROUND_HALF_EVEN:", number.quantize(Decimal("0.0")))
# # Округлення вверх при нічиї (ROUND_HALF_UP)
# print("Округлення вгору ROUND_HALF_UP:", number.quantize(Decimal("0.0"), rounding=decimal.ROUND_HALF_UP))
# # Округлення вниз (ROUND_FLOOR)
# print("Округлення вниз ROUND_FLOOR:", number.quantize(Decimal("0.0"), rounding=decimal.ROUND_FLOOR))
# # Округлення вверх (ROUND_CEILING)
# print("Округлення вгору ROUND_CEILING:", number.quantize(Decimal("0.0"), rounding=decimal.ROUND_CEILING))
# # Округлення до трьох десяткових знаків за замовчуванням
# print("Округлення до трьох десяткових знаків:", Decimal("3.14159").quantize(Decimal("0.000")))
#
# def read_lines(file_path):
#     with open(file_path, 'r', encoding="utf-8") as file:
#         for line in file:
#             yield line.strip()
# # Використання генератора для читання рядків з файлу
# for line in read_lines("test.txt"):
#     print(line)
#
# from typing import Callable
#
# def power(exponent: int) -> Callable[[int], int]:
#     def inner(base: int) -> int:
#         return base ** exponent
#     return inner
#
# # Використання
# square = power(2)
# cube = power(3)
#
# print(square(4))
# print(cube(4))
#
# def outer_function(msg):
#     message = msg
#     def inner_function():
#         print(message)
#     return inner_function
# # Створення замикання
# my_func = outer_function("Hello, world!")
# my_func()
#
# def add(a):
#     def add_b(b):
#         return a + b
#     return add_b
# # Використання:
# add_5 = add(5)
# result = add_5(10)
# print(result)

numbers = [1, 4, 1, 3, 2, 5, 2, 6]
sq = {i ** 2 for i in numbers}
print(sq)
