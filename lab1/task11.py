"""11. Знайти значення функції y=3x^6+6x^2+7 при даному значенні x"""
import math


def fn(x: int) -> int:
    y = 3 * pow(int(x), 6) + 6 * pow(int(x), 2) + 7
    return int(y)


print("Enter a number")
x = input("x = ")
print(fn(x))
