"""5. Підрахувати k - кількість тризначних натуральних чисел, сума цифр яких
дорівнює n (1≤n≤27). Операції ділення не використовувати"""


def culcul():
    a = 0
    n = 1
    while True:
        if 99 < n < 1000:
            a += 1
        elif n == 1000:
            break
        n += 1
    return a


def lopoper():
    res = culcul()
    return res


result = lopoper()
print(result)
