import math

choice = int(input("Введите количество переменных у вас в разложении:"))
if choice == 1:
    a = int(input("Введите значение a: "))
    f = int(math.factorial(a))
    print("Факториал равен: ", f)
if choice == 2:
    a = int(input("Введите значение a: "))
    b = int(input("Введите значение b: "))
    summ = a + b
    f = int(math.factorial(summ) / (math.factorial(a) * math.factorial(b)))
    print("Факториал равен: ", f)
if choice == 3:
    a = int(input("Введите значение a: "))
    b = int(input("Введите значение b: "))
    c = int(input("Введите значение c: "))
    summ = a + b + c
    f = int(math.factorial(summ) / (math.factorial(a) * math.factorial(b) * math.factorial(c)))
    print("Факториал равен: ", f)
if choice == 4:
    a = int(input("Введите значение a: "))
    b = int(input("Введите значение b: "))
    c = int(input("Введите значение c: "))
    d = int(input("Введите значение d: "))
    summ = a + b + c + d
    f = int(math.factorial(summ) / (math.factorial(a) * math.factorial(b) * math.factorial(c) * math.factorial(d)))
    print("Факториал равен: ", f)