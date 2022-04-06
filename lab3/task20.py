"""20. Дано дійсне число ε (> 0). Послідовність дійсних чисел AK визначається
наступним чином:A1 = 1,A2 = 2, AK = (AK-2 + 2 • AK-1) / 3, K = 3, 4, ....
Знайти перший з номерів K,для яких виконується умова | AK - AK-1 | <Ε,
і вивести цей номер, а також числа AK-1 і AK
Майданика Олександр"""


from math import fabs


def culcul(z: float, s: float):
    a = 3
    i = s
    temp1 = 2
    temp = 0
    while fabs(z - temp) > i:
        if a == 3:
            temp = z
            z = (temp1 + 2 * temp) / a
            a += 1
        else:
            temp1 = temp
            temp = z
            z = (temp1 + 2 * temp) / a
            a += 1
    return a, temp, z


def check(x: float):
    while True:
        if 0 <= x <= 1:
            break
        else:
            x = float(input("E = "))
    return x


def lop():
    k = float(input("E = "))
    return k


def lopoper():
    b = lop()
    b = check(b)
    ai = 1
    res, a, z = culcul(ai, b)
    return res, a, z


iz, result, temps = lopoper()
print("A" + str(iz - 1) + "=" + str(result))
print("A" + str(iz) + "=" + str(temps))
print("k = " + str(iz))
