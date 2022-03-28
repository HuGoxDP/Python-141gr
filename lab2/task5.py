"""5. Дано ціле число. Вивести його рядок-опис виду «від'ємне парне число»,
«нульове число», «додатне непарне число» і т. д."""


def digits_description(x: int):
    if x == 0:
        return print(str(x) + " = нульове число ")
    elif x > 0 and x % 2 != 0:
        return print(str(x) + " = додатне непарне число ")
    elif x > 0 and (x % 2) == 0:
        return print(str(x) + " = додатне парне число ")
    elif x < 0 and (x % 2) != 0:
        return print(str(x) + " = від'ємне непарне число ")
    elif x < 0 and x % 2 == 0:
        return print(str(x) + " = від'ємне парне число ")


x = int(input("x = "))
digits_description(x)
