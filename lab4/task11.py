"""11. Дано список. Вивести спочатку всі негативні елементи,
потім всі інші
Майданика Олександр"""


def culcul(s: list):
    newlist = [i for i in s if i < 0] + [i for i in s if i >= 0]
    return newlist


def get_list():
    lst = list(map(float, input("Please enter list ").split()))
    return (lst)


def main():
    ist = get_list()
    result = culcul(ist)
    return result


result = main()
print(result)
