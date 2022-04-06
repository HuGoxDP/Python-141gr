"""11. Дано цілі числа K і N (N> 0). Вивести N раз число K.
Майданика Олександр"""


def culcul(a, b):
    s = ""
    for i in range(b):
        s += str(a) + " "
    return s


def check(x: int):
    while True:
        if x > 0:
            break
        else:
            x = int(input("N = "))
    return x


def lop():
    k = int(input("K = "))
    n = int(input("N = "))
    return k, n


def lopoper():
    a, b = lop()
    b = check(b)
    res = culcul(a, b)
    return res


rusult = lopoper()
print(rusult)
