"""11. Дано три змінні: X, Y, Z. Якщо їх значення впорядковані за спаданням,то
подвоїти їх; в іншому випадку замінити значення кожної змінної на протилежне.
"""


def three_digits(x: float, y: float, z: float):
    if x > y and y > z:
        x *= 2
        y *= 2
        z *= 2
        return print("x = " + str(x) + " y = " + str(y) + " z = " + str(z))
    else:
        x *= -1
        y *= -1
        z *= -1
        return print("x = " + str(x) + " y = " + str(y) + " z = " + str(z))


x = float(input('x = '))
y = float(input('y = '))
z = float(input('z = '))
three_digits(x, y, z)
