"""5. Обчислити дробову частину середнього геометричного
трьох заданих позитивних чисел."""


def geometric(x, y, z):
    temp = (z * x * y) ** (1/3)
    return temp


x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))
print(geometric(x, y, z))
