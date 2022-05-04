"""15. У списку чисел перевірити, чи всі елементи є унікальними,
тобто кожне число зустрічається тільки один раз.
Майданика Олександр"""


def culcul(s: list) -> bool:
    s.sort()
    q = len(s)
    for i in range(q):
        a = s.count(s[i])
        if a > 1:
            return False
    return True


def get_list():
    lst = list(map(float, input("Please enter num list ").split()))
    return (lst)


def main():
    ist = get_list()
    result = culcul(ist)
    return result


result = main()
print("чи всі елементи є унікальними " + str(result))
