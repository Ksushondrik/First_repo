'''Lesson 1'''
'''a = int(input("1st number: "))
b = int(input("2nd number: "))
if b != 0:
    print(f"a/b={a/b}")
else:
    print("Division by zero!")'''

'''a = int(input("Numer: "))
if a > 0:
    print("positive")
elif a == 0:
    print("zero")
else:
    print("negative")'''

'''a = int(input("Numer: "))
match a:
    case a % 2 == 0:
        print("Кратне 2")
    case a % 3 == 0:
        print("Кратне 3")
    case a % 2 == 0:
        print("Кратне 2")
    case a % 2 == 0:
        print("Кратне 2")'''

'''a = int(input("Numer: "))
if a % 2==0 or a % 3 == 0 and a % 5 == 0 :
    print(True)
else:
    print(False)

b = a % 2 == 0 or a % 3 == 0 and a % 5 == 0
if b:
    print(True)
else:
    print(False)'''

'''a = int(input("Numer: "))
while (a<5):
    print(a)
    a += 1

b = 0
while (b == 0):
    b = int(input("2nd number: "))'''

'''list={1:'a', 2:'b', 3:'c'}
for k,v in list.items():
    print(f"{k}  ->  {v}")'''

'''for i in range(101):
    if i%5==0:
        continue
    print(f"{i}")
    pass'''

'''list=[1,2,3,3.0,5.0,'a','b']
for i in list:
    if type(i)==float:
        continue
    print(f"{i}")
    pass

for i in list:
    if type(i)!=float:
        continue
    print(f"{i}")
    pass'''

'''list=[1,2,3,3.0,5]
sum=0
list1=list
list2=list[::]
list1[0]=10
list2[1]=10
print(list)
print(list1)
print(list2)
print(list1 is list)
print(list2 is list)'''

'''a=None
...
#modify a wiyh conditions
...
if a is None:
    pass
'''

'''a=5
b=0
try:
    print(f"a/b={a/b}")
except ZeroDivisionError:
    print ("error")
finally:
    print("done")'''

'''try:
    f=open("d:\\1.txt","r")
except Exception:
    print ("error")
finally:
    print("done")'''

'''try:
    a = float(input("1st number: "))
    b = float(input("2nd number: "))
except Exception as error:
    print (f"Error: {error}")
finally:
    print("done")'''

'''sum=0
list=[1,1,1,1,2,2]
for i in list:
    sum+=i
print(sum)'''

'''Автоперевірка'''

'''def first(size,*args):
    result = len(args)
    return (size + result)

def second(size,**kwargs):
    result = len(kwargs)
    return (size + result)

print(first(5,"first","second","third"))
print(first(1,"Alex","Boris"))
print(second(3, comment_one="first", comment_two="second", comment_third="third"))
print(second(10, comment_one="Alex", comment_two="Boris"))'''

'''def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)

def number_of_groups(n, k):
    return (factorial(n)/(factorial(n-k)*factorial(k)))

print(factorial(5))
print(number_of_groups(10,2))'''

'''Lesson 2'''
'''kahoot'''
'''hello = "Hello"
print(f"Hello {hello}")'''
...
'''age = 18
if int(age) == "18":
    print("String")
else:
    print("Not string")'''
...
'''a = "12.0"
a = int(a)
if a > 0:
    print("Число додатнє")
elif a < 0:
    print("Число від'ємне")
else:
    print("Це число - нуль") #помилка'''
...
'''some_bool = bool("string")
print(some_bool)'''
...
'''money = 0
if money:
    print(f"You have {money} on your bank account")
else:
    print(f"You have no mony and no debts")'''
...
'''is_nice = True
state = "nice" if is_nice else "not nise"
print(state)'''
...
'''x = 0
y = 0
if x >= 0:
    if y >= 0:
        print("Перша чверть")
    else:
        print("Четверта чверть")
else:
    if y >= 0:
        print("Друга чверть")
    else:
        print("Третя чверть")'''
...
'''fruits = "apple peach apricot"
in_a = 0
for char in fruits:
    if char == "a":
        in_a += 1
print(in_a)'''
...
'''a = 1
while a <= 5:
    a = a + 1
    print(a)'''
...
'''a = 0
while True:
    print(a)
    if a >=5:
        break
    a = a + 1'''
...
'''a = 0
while a < 6:
    a = a + 1
    if not a % 2:
        continue
    print(a)'''
'''#Принцип роботи коду вище:
a = 0
while a < 10:
    print(f"{a}<10 -> {a<10}")
    a = a + 1
    print(a)
    print(f"{a} % 2 -> {a % 2}")
    print(f"not {a} % 2 -> {not a % 2}")'''
...
'''sum = 0
a = 1
while a <= 5:
    sum += a
    a = a + 1
print(sum)'''
...
'''a = [2, 4, 6, 8, 3]
k = 0
for b in a:
    if k < b:
        k = b
print(k)'''
...
'''val =  "a"
try:
    val = int(val)
except ValueError:
    print(f"val {val} is not a number")
else:
    print(val>0)'''

'''Vebinar'''
'''def sum2(a,b):
    print(a)
    print(b)
    if a>=b:
        return a+b

print(sum2(2,3))'''
...
def sum2(a:int,b:int,c=True)->int:
    print(f"a={a} b={b}")
    return a+b if c else a-b

'''def add_to_list(el,list=[]):
    list.append(el)
    print(list)

add_to_list(1)
add_to_list(2)
add_to_list(3)'''

