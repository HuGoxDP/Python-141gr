"""5. Обчислити дробову частину середнього геометричного
трьох заданих позитивних чисел."""


def geometric():
    print("Enter a positive numbers")
    x = int(input("x = "))
    y = int(input("y = "))
    z = int(input("z = "))
    temp = (z * x * y) ** (1/3)
    return print("Geometric mean = " + str(temp) + "\n" + "Fractional part = " + str(temp - int(temp)))


geometric()
