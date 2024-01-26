# import datetime
# now = datetime.datetime.now()
# print(now)

# #Створення об'єктів date i time
# date_part = datetime.date(2024, 1, 17)
# time_part = datetime.time(18, 00, 00)
# #Комбінування дати і часу в один об'єкт datetime
# combined_datetime = datetime.datetime.combine(date_part,time_part)
# print(combined_datetime)
# date_a = datetime.datetime(2015, 8, 29, 15, 00, 00)
# print(date_a)
# specific_date = datetime.datetime(year=2017, month=8, day=25)
# print(specific_date)

# from datetime import datetime
# current_datetime = datetime.now()
# print(current_datetime.year)
# print(current_datetime.month)
# print(current_datetime.day)
# print(current_datetime.hour)
# print(current_datetime.minute)
# print(current_datetime.second)
# print(current_datetime.microsecond)
# print(current_datetime.tzinfo)
# print(current_datetime.date())
# print(current_datetime.time())

# now = datetime.now()
# day_of_week = now.weekday()
# if day_of_week == 0:
#     print(f"Сьогодні понеділок")
# elif day_of_week == 1:
#     print(f"Сьогодні вівторок")
# elif day_of_week == 2:
#     print(f"Сьогодні середа")
# elif day_of_week == 3:
#     print(f"Сьогодні четвер")
# elif day_of_week == 4:
#     print(f"Сьогодні п'ятниця")
# elif day_of_week == 5:
#     print(f"Сьогодні субота")
# else:
#     print(f"Сьогодні неділя")

# datetime1 = datetime(2023, 3, 14, 12, 0)
# datetime2 = datetime(2023, 3, 15, 12, 0)
# print(datetime1 == datetime2)
# print(datetime1 != datetime2)
# print(datetime1 < datetime2)
# print(datetime1 > datetime2)

# seventh_day_2019 = datetime(year=2019, month=1, day=7, hour=14)
# seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
# difference = seventh_day_2020 - seventh_day_2019
# print(difference)
# print(difference.total_seconds())

# from datetime import timedelta
# delta = timedelta(
#     days=50,
#     seconds=27,
#     microseconds=10,
#     milliseconds=29000,
#     minutes=5,
#     hours=8,
#     weeks=2
# )
# print(delta)

# from datetime import datetime, timedelta
# now = datetime.now()
# future_date = now + timedelta(days=10) #додаємо 10 днів до поточної дати
# print(future_date)
# seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
# four_weeks_interval = timedelta (weeks=4)
# print(seventh_day_2020 + four_weeks_interval)
# print(seventh_day_2020 - four_weeks_interval)
...
# date = datetime(year=2023, month=12, day=18) #Створення об'єкта datetime
# ordinal_number = date.toordinal() #Отримання порядкового номера
# print(f"Порядковий номер дати {date} становить {ordinal_number}")
...
# napoleon_burns_moscow = datetime(year=1812, month=9, day=14) #Встановлення дати спалення москви Наполеоном (14 вересня 1812 року)
# current_date = datetime.now() #Поточна дата
# days_since = current_date.toordinal() - napoleon_burns_moscow.toordinal()
# print(days_since)
...
# from datetime import datetime
# now = datetime.now()
# timestamp = datetime.timestamp(now)
# print(timestamp)
# timestamp = 1679654123
# dt_object = datetime.fromtimestamp(timestamp)
# print(dt_object)
# date_time = now.strftime("%Y-%m-%d %H:%M:%S") #форматування дати і часу
# print(date_time)
# date = now.strftime("%A, %d %B %Y") #форматування лише дати
# print(date)
# time = now.strftime("%I:%M %p") #форматування лише часу
# print(time)
# only_date = now.strftime("%d.%m.%Y") #форматування лише дати
# print(only_date)
# print(10*"-")
# date_string = input() #дата певного формату
# datetime_object = datetime.strptime(date_string, "%Y-%m-%d") #перетворення рядка в об'єкт datetime
# print(datetime_object)
# print(10*"=")
# iso_format = now.isoformat()
# print(iso_format)
# print(10*"-=-")
# iso_string = "2023-03-14T12:39:29.992996"
# date_from_iso = datetime.fromisoformat(iso_string)
# print(date_from_iso)
# print(10*"*/")
# day_of_week = now.isoweekday()
# print(day_of_week)
# iso_calendar = now.isocalendar()
# print(f"ISO рік: {iso_calendar[0]}, ISO тиждень: {iso_calendar[1]}, ISO день тижня: {iso_calendar[2]}")
# print(10*"--")
...
# from datetime import datetime, timezone
# local_now = datetime.now()
# utc_now = datetime.now(timezone.utc)
# print(local_now)
# print(utc_now)
...
# from datetime import datetime, timezone, timedelta
# utc_time = datetime.now(timezone.utc)
# eastern_time = utc_time.astimezone(timezone(timedelta(hours=-5)))
# print(eastern_time)
...
# from datetime import datetime, timezone, timedelta
# # Припустимо, місцевий час належить до часової зони UTC+2
# local_timezone = timezone(timedelta(hours=2))
# local_time = datetime(year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=local_timezone)
# # Конвертація локального часу в UTC
# utc_time = local_time.astimezone(timezone.utc)
# print(utc_time)  # Виведе час в UTC
...
# from datetime import date, datetime
# today = datetime.now()
# print(today)
# print(25*"-*")
# print(today.year)
# print(today.month)
# print(today.day)
# print(10*"-")
# print(today.hour)
# print(today.minute)
# print(today.second)
# print(today.microsecond)
# print(10*"-")
# print(today.tzinfo)
# print(25*"-*")
# print(today.date())
# print(today.time())
...
# import datetime
# date = datetime.date(2024,11,24)
# time =datetime.time(12,00)
# date_time = datetime.datetime.combine(date,time)
# print(date_time)
# a = datetime.datetime(year=2020, month=1, day=7)
# print(a)
# b = datetime.datetime(year=2023, month=5, day=13, hour=13, minute=30, second=15)
# print(b)
...
# from datetime import datetime
# todey = datetime.now()
# d_w = todey.weekday()
# print(d_w)
...
# from datetime import timedelta, datetime
# delta = timedelta(
#     days=50,
#     seconds=27,
#     microseconds=10,
#     milliseconds=29000,
#     minutes=5,
#     hours=8,
#     weeks=2
# )
# print(delta)

# a = datetime(2024,11,24)
# b = datetime(2024,9,28)
# c = a - b #певний відрізок часу між датами
# print(c)
# todey = datetime.now()
# n = todey.toordinal()
# print(n)
# sec_today = datetime.timestamp(todey)
# print(sec_today)
...
# from datetime import datetime, timezone, timedelta
# utc_time = datetime.now(timezone.utc)
# print(utc_time)
# eastern_time = utc_time.astimezone(timezone(timedelta(hours=-5)))
# print(eastern_time)
# local_timezone = timezone(timedelta(hours=2))
# local_time = datetime.now(tz=local_timezone)
# local_in_utc = local_time.astimezone(timezone.utc)
# tz_iso = local_time.isoformat()
# print(f"Локальний час: {local_time}, а за UTC: {local_in_utc}, а за ISO: {tz_iso}")
...
# import time
# start_time = time.perf_counter() #Записуємо час на початку виконання
# today = time.time()
# print(f"Поточний час: {today}")
# time.sleep(3)
# print(45*"*")
# read_today = time.ctime(today)
# print(f"Також поточний час: {read_today}")
# time.sleep(3)
# local_time = time.localtime(today)
# print(local_time)
# end_time = time.perf_counter() #Записуємо час після виконання операцій
# execution_time = end_time - start_time #Розраховуємо час виконання
# print(f"Час виконання: {execution_time} секунд")
...
# import random
# cards = ["Tuz", "Korol'", "Dama", "Valet", "10", "9", "8", "7", "6"]
# print(cards)
# random.shuffle(cards)
# print(cards)
# x = random.choice(cards)
# print(x)
...
# import math
# x = 3.2
# y = 3.5
# z = 3.7
# print(f"{x} -> {math.ceil(x)}; {math.floor(x)}; {math.trunc(x)}")
# print(f"{y} -> {math.ceil(y)}; {math.floor(y)}; {math.trunc(y)}")
# print(f"{z} -> {math.ceil(z)}; {math.floor(z)}; {math.trunc(z)}")
...
# text = """This is first line
# And second line
# Last third line"""

# song = '''Jingle bells, jingle bells
# Jingle all the way
# Oh, what fun it is to ride
# In a one horse open sleigh'''

# print(text)
# print(song)

# one_line_text = ("Textual data in Python is handled with str objects,"
#                 " or strings. Strings are immutable sequences of Unicode"
#                 " code points. String literals are written in a variety "
#                 " of ways: single quotes, double quotes, triple quoted.")
# print(one_line_text)

# result = one_line_text.split()
# print(result)
# print()
# x = ' '.join(result)
# print(x)

# y = one_line_text.replace("tri", "XXX",-1)
# print(y)

# number = "12345d"
# print(number.isdigit())  # Виведе: True

# text = "Number123"
# print(text.isdigit())  # Виведе: False

# width = 5
# for num in range(12):
#     print(f'{num:^10} {num**2:^10} {num**3:^10}')

# name = "Alice"
# formatted = f"{name:>10}"
# print(formatted)  # Виведе: '     Alice' (вирівнювання праворуч)

...

# import re
# pattern = '^a...s'
# test_string = 'abyss'
# result = re.match(pattern, test_string)
# if result:
#     print("Search successful.")
# else:
#     print("Search unsuccessful.")
