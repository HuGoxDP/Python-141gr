"""15. Дано координати (x; y) точки і радіус кола (r). Визначити чи належить
дана точка колі, якщо його центр знаходиться на початку координат."""


def main(x, y, r):
    if r**2 >= x**2 + y**2:
        result = "Дана точка належить колі"
        return result
    else:
        result = "Дана точка не належить колі"
        return result


print("введіть координати ")
x = float(input("x = "))
y = float(input("y = "))
r = float(input("введіть радіус кола r = "))
result = main(x, y, r)
print (result)
