"""10. Описати функцію IsLeapYear(Y) логічного типу, яка повертає True,
якщо рік Y (ціле додатне число) є високосним, і False в іншому випадку.
Вивести значення функції IsLeapYear для п'яти даних значень параметра Y.
Високосним є рік, який ділиться на 4, за виключенням тих років,
які діляться на 100 і не діляться на 400.
Майданика Олександр"""


def check(k: int) -> int:
    if k > 0:
        return k
    else:
        return print("Введите целое положительное число")


def culcul(a) -> bool:
    if (a % 4 == 0 and a % 100 != 0 or a % 400 == 0):
        return True
    else:
        return False


def IsLeapYear(a: int):
    a = check(a)
    res = culcul(a)
    return res


for i in range(5):
    a = int(input("Введите K = "))
    result = IsLeapYear(a)
    print("""Високосним є рік = {}
""".format(result))
