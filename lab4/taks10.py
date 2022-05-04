"""10. Дано рядки S, S1 і S2. Замінити в рядку
S останнє входження рядка S1 на рядок S2
Майданика Олександр"""


def get_s_s1_s2():
    s = str(input("S = "))
    s1 = str(input("S1 = "))
    s2 = str(input("S2 = "))
    return s, s1, s2


def culcul(s, s1, s2):
    res = s.replace(s1, s2)
    return res


def replc():
    s, s1, s2 = get_s_s1_s2()
    result = culcul(s, s1, s2)
    return result


result = replc()
print(result)
