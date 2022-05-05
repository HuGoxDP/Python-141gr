"""10. Описати функцію Swap (X, Y), яка міняє вміст змінних X і Y
(X і Y - дійсні параметри, які є одночасно вхідними та вихідними)
З її допомогою для даних змінних A, B, C, D послідовно поміняти вміст
наступних пар: A і B, C і D, B і C і вивести нові значення A, B, C, D.
Майданика Олександр
"""


def culcul(a, b, c, d) -> float:
    a, b, c, d = b, a, d, c
    b, c = c, b
    return a, b, c, d


def get_abcd():
    a = float(input("Введите A = "))
    b = float(input("Введите B = "))
    c = float(input("Введите C = "))
    d = float(input("Введите D = "))
    return a, b, c, d


def swap():
    a, b, c, d = get_abcd()
    a, b, c, d = culcul(a, b, c, d)
    return a, b, c, d


a, b, c, d = swap()
print("A = {}, B = {}, C = {}, D = {}".format(a, b, c, d))
