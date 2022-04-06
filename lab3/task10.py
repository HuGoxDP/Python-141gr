"""
10. Дано ціле число N (> 0). Знайти значення виразу 1.1 - 1.2 + 1.3 - ...
(N доданків, знаки чергуються). Умовний оператор не використовувати.
Майданика Олександр
"""


def new_n():
    n = int(input("x = "))
    return n


def main():
    n = new_n()
    temp = (1.0 + float(1 / 10))
    i = 1
    while i < n:
        a = (1.0 + (float(i + 1) / 10))
        b1 = i % 2 == 0
        b2 = i % 2 != 0
        while b1:
            temp = temp + a
            i += 1
            b1 = i % 2 == 0
        while b2:
            temp = temp - a
            i += 1
            b2 = i % 2 != 0
    return round(temp, 3)


result = main()
print(result)
