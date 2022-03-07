"""15. Дано змінні A, B, C. Змінити їх значення, перемістивши вміст A в B,
B - в C, C - в A, і вивести нові значення змінних A, B, C.
"""


def swap(a, b, c):
    temp = b
    b = a
    a = c
    c = temp
    return print("A = " + a + "\n" + "B = " + b + "\n" + "C = " + c)


a = input("A = ")
b = input("B = ")
c = input("C = ")
print(swap(a, b, c))
