"""15. Дано ціле число N (> 0). Послідовність дійсних чисел AK визначається
наступним чином:A0 = 1, AK = (AK-1 + 1) / K, K = 1, 2, ....
Вивести елементи A1, A2, ..., AN"""


def culcul(z: float, i: int):
    a = 1
    while a <= i:
        temp = z
        z = (temp + 1) / a
        a += 1
        print(z)
    return z


def check(x: int):
    while True:
        if x > 0:
            break
        else:
            x = int(input("N = "))
    return x


def lop():
    k = int(input("N = "))
    return k


def lopoper():
    b = lop()
    b = check(b)
    ai = 1
    res = culcul(ai, b)
    return res, b


result, zx = lopoper()
print("A" + str(zx) + "=" + str(result))
