# РОБОТА З ФАЙЛАМИ

# fh = open('test.txt', 'w')
# symbols_written = fh.write("hello!")
# print(symbols_written)
# fh.close()

# fh = open('test.txt', 'w+')
# fh.write("hello!")
# fh.seek(0)
# first_two_symbols = fh.read(2)
# print(first_two_symbols)
# fh.close()

# fh = open('test.txt', 'r')
# all_file = fh.read()    #прочитає весь файл
# print(all_file)
# fh.close()

# fh = open('test.txt', 'r')
# while True:
#     symbol = fh.read(1)
#     if len(symbol) == 0 :
#         break
#     print(symbol)
# fh.close()

# fh = open('test.txt', 'w')
# fh.write("first line\nsecond line\nthird line")
# fh.close()
# fh = open('test.txt', 'r')
# while True:
#     line = fh.readline()
#     if not line:
#         break
#     print(line)
# fh.close()

# fh = open('test.txt', 'r')
# lines = fh.readlines()
# print(lines)
# fh.close()

# fh = open('test.txt', 'r')
# lines = [el.strip() for el in fh.readlines()]
# print(lines)
# fh.close()

# fh = open('test.txt', 'w+')
# fh.write("hello!")
# position = fh.tell()
# print(position)
# fh.seek(1)
# position = fh.tell()
# print(position)
# fh.read(2)
# position = fh.tell()
# print(position)
# # fh.close()
...
#МЕНЕДЖЕР КОНТЕКСТУ

# fh = open('text.txt', 'w')
# try:
#     fh.write("Some data")
# finally:
#     fh.close()

# with open('text.txt', 'w') as fh:
#     fh.write("Some data")

# with open('test.txt', 'w') as fh :
#     fh.write("first line\nsecond line\nthird line")
# with open('test.txt', 'r') as fh :
#     lines = [el.strip() for el in fh.readlines()]
# print(lines)
...
#РОБОТА З НЕ ТЕКСТОВИМИ ФАЙЛАМИ У PYTHON

# with open('raw_data.bin', 'wb') as fh :
#     fh.write(b"Hello world!")

# s = b'Hello!'
# print(s[1])
# byte_string = b'Hello world!'
# print(byte_string)
# byte_str = 'some text'.encode()
# print(byte_str)

# numbers = [0, 128, 255]
# byte_numbers = bytes(numbers)
# print(byte_numbers)

# for num in [127, 255, 156] :
#     print(hex(num))

# print(ord('a')) #код символу 'a' в UTF-8

# s = "Привіт!"
# utf8 = s.encode()
# print(f"UTF-8: {utf8}")
# utf16 = s.encode("utf-16")
# print(f"UTF-16: {utf16}")
# cp1251 = s.encode("cp1251")
# print(f"CP-1251: {cp1251}")
# s_from_utf16 = utf16.decode("utf-16")
# print(s_from_utf16 == s)

# print(b'Hello world!'.decode('utf-16'))

# # Відкриття текстового файлу з явним вказівкам UTF-8 кодування
# with open('test.txt', 'r', encoding='utf-8') as file:
#     content = file.read()
#     print(content)

# byte_array = bytearray(b'Kill Bill')
# print(byte_array)
# byte_array[0] = ord('B')
# byte_array[5] = ord('K')
# print(byte_array)

# byte_array = bytearray(b"Hello")
# byte_array.append(ord("!"))  
# print(byte_array)

# byte_array = bytearray(b"Hello World")
# string = byte_array.decode("utf-8")
# print(string)  # Виведе: 'Hello World'

# string1 = "Hello World"
# string2 = "hello world"
# if string1.lower() == string2.lower():
#     print("Рядки однакові")
# else:
#     print("Рядки різні")

# german_word = 'straße'  # В нижньому регістрі
# search_word = 'STRASSE'  # В верхньому регістрі

# # Порівняння за допомогою lower()
# lower_comparison = german_word.lower() == search_word.lower()

# # Порівняння за допомогою casefold()
# casefold_comparison = german_word.casefold() == search_word.casefold()

# print(f"Порівняння з lower(): {lower_comparison}")
# print(f"Порівняння з casefold(): {casefold_comparison}")
...

#РОБОТА З АРХІВАМИ  ?????????

# import shutil

# # Створення ZIP-архіву з вмістом директорії 'my_folder'
# shutil.make_archive('example', 'zip', root_dir='my_folder') 

...

#ОСНОВИ МОДУЛЯ PATHLIB

# from pathlib import Path
# p = Path("text.txt")
# p.write_text("Hello, world!")
# print(p.read_text())
# print("Exists:", p.exists())

# from pathlib import Path
# #створення об'єкту Path для файлу
# file_path = Path("text.txt")
# #запис тексту у файл
# file_path.write_text("Привіт світ!", encoding="utf-8")
# #читання тексту з файлу
# text = file_path.read_text(encoding="utf-8")
# print(text)

# # створення об'єкту Path для бінарного файлу
# file_path = Path("raw_data.bin")
# #бінарні дані для запису
# data = b"Python is great!"
# #запис байтів у файл
# file_path.write_bytes(data)
# #читання байтів з файлу
# binary_data = file_path.read_bytes()
# print(binary_data)

# #Робота з директоріями
# from pathlib import Path
# #створення обйєкту Path для директорії
# directory = Path("C:/Users/Ksushondrik/Documents/GitHub/First_repo")
# #виведення переліку всіх файлів та піддиректорій
# for path in directory.iterdir() :
#     print(path)