"""20. Дано ціле число, яке лежить в діапазоні 1-999. Вивести його
рядок-опис виду «парне двозначне число», «непарне тризначне число» і т. Д"""


def pr():
    print("enter any number from 1 - 999")
    digits = int(input())
    prtext = "Це "

    while digits < 1 or digits > 999:
        print("Enter any number from 1 - 999")
        digits = int(input())

    if digits % 2 == 0:
        prtext += "парне "
    else:
        prtext += "непарне "
    if digits < 10:
        prtext += "однозначне число"
    elif digits < 100:
        prtext += "двозначне число"
    elif digits <= 999:
        prtext += "тризначне число"

    return print(prtext)


pr()
