"""11. Знайти значення функції y=3x^6+6x^2+7 при даному значенні x"""
import math


def fn():
    print("Enter a number")
    x = input("x = ")
    y = 3 * pow(int(x), 6) + 6 * pow(int(x), 2) + 7
    return print(int(y))


fn()
