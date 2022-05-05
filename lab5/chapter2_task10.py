""""10. Описати функцію IsSquare (K) логічного типу, яка повертає True,
якщо цілий параметр K (> 0) є квадратом деякого цілого числа,
і False в іншому випадку.З її
допомогою знайти кількість квадратів в наборі з 10 цілих позитивних чисел.
Майданика Олександр"""


from math import sqrt


def check(k: int) -> int:
    if k > 0:
        return k
    else:
        return get_k()


def culcul(a) -> bool:
    a = sqrt(a)
    if a == int(a):
        return True
    else:
        return False


def get_k():
    a = int(input("Введите K = "))
    return check(a)


def swap():
    a = get_k()
    res = culcul(a)
    return res


a = 0
for i in range(10):
    result = swap()
    if result is True:
        a += 1
print("""кількість квадратів в наборі з 10 цілих позитивних чисел = {}
""".format(a))
