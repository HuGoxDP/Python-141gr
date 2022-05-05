"""10. Описати функцію IsDistance(X, Y) дійсного типу,
яка обчислює відстань між двома точками, заданими своїми координатами.
За допомогою цієї функції знайти
периметр десятикутника, вершини якого мають відповідно координати
(x1, y1),(x2,y2), …, (x10, y10)
    a = sqrt(((x1 - x2)**2) + ((y1 - y2)**2))
    b = sqrt(((x2 - x3)**2) + ((y2 - y3)**2))
    c = sqrt(((x3 - x4)**2) + ((y3 - y4)**2))
    d = sqrt(((x4 - x5)**2) + ((y4 - y5)**2))
    f = sqrt(((x5 - x6)**2) + ((y5 - y6)**2))
    g = sqrt(((x6 - x7)**2) + ((y6 - y7)**2))
    h = sqrt(((x7 - x8)**2) + ((y7 - y8)**2))
    j = sqrt(((x8 - x9)**2) + ((y8 - y9)**2))
    r = sqrt(((x9 - x10)**2) + ((y9 - y10)**2))
    e = sqrt(((x10 - x1)**2) + ((y10 - y1)**2))
    p = a + b + c + d + f + g + h + e + r + j
    Майданика Олександр"""


from math import sqrt


def culcul(x1, y1, x2, y2) -> float:
    p=0
    p += sqrt(((x1-x2)**2) + ((y2 - y1)**2))
    return p


def isdistance(x1: float,x2: float,y1: float,y2: float) -> float:
    res = culcul(x1, y1, x2, y2)
    return res


i = int(input("""Если хотите ввести самому координаты вершин 10-угольника
введите 1 или же 2 если хортите использовать предложаный  = """))
x = []
y = []
result = 0
if i == 1:
    for i in range(10):
        x.append(float(input("Введите x{} = ". format(i+1))))
        y.append(float(input("Введите y{} = ". format(i+1))))
else:
    x = [3, 2, 1, 2, 3, 5.1, 6, 7, 6.3, 5]
    y = [1, 2.2, 4, 6, 7, 7, 6, 4, 2, 1]
for i in range(len(x)):
    print("x{} = ".format(i+1) + str(x[i]))
    print("y{} = ".format(i+1) + str(y[i]))
for i in range(len(x)):
    if i == len(x)-1:
        result += isdistance(x[i], x[0], y[i], y[0])
    else:
        result += isdistance(x[i], x[i+1], y[i], y[i+1])

print("периметр десятикутника = " + str(result))
