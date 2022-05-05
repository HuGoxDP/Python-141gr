"""10. Описати функцію GCD2 (A, B) цілого типу, яка знаходить найбільший
спільний дільник (НСД, greatest common divisor)
двох цілих позитивних чисел A і B, використовуючи алгоритм Евкліда:
НСД (A, B) = НСД (B, A mod B), якщо B ≠ 0; НСД (A, 0) = A,
де «mod» позначає операцію взяття залишку від ділення. За допомогою GCD2 знайти
найбільші спільні дільники пар (A, B), (A, C), (A, D), якщо дано числа A,
B, C, D.
Майданика Олександр"""


def check(a: int, b: int) -> int:
    if (a and b) > 0:
        return a, b
    else:
        return (print("Все числа должны быть положительные"))


def culcul(a: int, b: int) -> int:
    while a != b:
        if (b == 0) or (a == 0):
            if a > b:
                return a
            else:
                return b
        elif a > b:
            a = a % b
        else:
            b = b % a
    return a


def GCD2(a: int, b: int):
    a, b = check(a, b)
    res = culcul(a, b)
    return res


a = int(input("Введите А = "))
b = int(input("Введите B = "))
c = int(input("Введите C = "))
d = int(input("Введите D = "))
res1 = GCD2(a, b)
res2 = GCD2(a, c)
res3 = GCD2(a, d)
print("""НСД A і B = {}
НСД A і С = {}
НСД A і D = {}""".format(res1, res2, res3))
