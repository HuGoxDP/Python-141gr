"""20. Присвоїти цілій змінній d першу цифру з дробової частини
позитивного дійсного числа x
"""


def assign1(x: float) -> float:
    temp = int(x)
    x -= temp
    d = x * 10
    return (int(d))


x = float(input("Enter float x = "))

while x <= 0:
    x = float(input("Enter x > 0 " + "\n" + "x = "))

print("d = " + (str(assign1(x))))
