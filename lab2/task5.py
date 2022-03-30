"""5. Дано ціле число. Вивести його рядок-опис виду «від'ємне парне число»,
«нульове число», «додатне непарне число» і т. д."""


def digits_description(x: int):
    result = str(x)
    if x == 0:
        return result + " = нульове число "
    elif x > 0 and x % 2 != 0:
        return result + " = додатне непарне число "
    elif x > 0 and (x % 2) == 0:
        return result + " = додатне парне число "
    elif x < 0 and (x % 2) != 0:
        return result + " = від'ємне непарне число "
    elif x < 0 and x % 2 == 0:
        return result + " = від'ємне парне число "


num = int(input("x = "))
results = digits_description(num)
print(results)
