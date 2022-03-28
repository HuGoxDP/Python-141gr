"""20. Присвоїти цілій змінній d першу цифру з дробової частини
позитивного дійсного числа x
"""


def assign1():
    x = float(input("Enter a positive float x = "))
    
    while x <= 0:
        x = float(input("Enter x > 0 " + "\n" + "x = "))

    temp = int(x)
    x -= temp
    d = int (x * 10)
    return print("d = " + (str(d)))


assign1()
