"""11. Дано цілі числа K і N (N> 0). Вивести N раз число K.
"""

def culcul(a, b):
    for i in range(b):
        print(a)


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
    culcul(a, b)



lopoper()
