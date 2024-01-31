def sum():
    print("sum")
def f1():
    print("f1")
def f2():
    print("f2")
def f3():
    print("f3")
def f4():
    print("f4")

print(f"__name__ == {__name__}")

if __name__ == "Lab2":
    PI = 3.14
    G = 9.8

if __name__ == "__main__":
    sum()
    f2()
    import Lab
    Lab.f1()