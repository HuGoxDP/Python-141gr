"""20. Дано ціле число, яке лежить в діапазоні 1-999. Вивести його
рядок-опис виду «парне двозначне число», «непарне тризначне число» і т. Д"""


def getnum():
    digits = int(input("Enter any number from 1 - 999\n"))
    return digits


def check(digits: int) -> int:
    while True:
        if 0 < digits < 1000:
            break
        else:
            digits = int(input("Enter any number from 1 - 999\n x = "))
    return digits


def calcs(digits: int) -> str:
    prtext = "Це "
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
    return prtext


def pr():
    x = getnum()
    digits = check(x)
    prtext = calcs(digits)
    return prtext


results = pr()
print(results)
