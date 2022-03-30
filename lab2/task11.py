"""11. Дано три змінні: X, Y, Z. Якщо їх значення впорядковані за спаданням,то
подвоїти їх; в іншому випадку замінити значення кожної змінної на протилежне.
"""


def three_digits(x, y, z) -> float:
    
    if x > y > z:
        x *= 2
        y *= 2
        z *= 2
        result = "x = " + str(x) + " y = " + str(y) + " z = " + str(z)
        return result
    else:
        x *= -1
        y *= -1
        z *= -1
        result = "x = " + str(x) + " y = " + str(y) + " z = " + str(z)
        return result


x1 = float(input('x = '))
y1 = float(input('y = '))
z1 = float(input('z = '))
results = three_digits(x1, y1, z1)
print (results)
