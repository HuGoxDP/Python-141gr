"""20. Дано список чисел. Порахуйте, скільки в ньому пар елементів,
рівних один одному. Вважається,що будь-які два елементи,
рівні один одному, утворюють одну пару, яку необхідно порахувати.
Майданика Олександр"""


def culcul(s: list):
    res = (((s.count(x) - 1 for x in s))//2)
    return(res)


def get_list():
    lst = list(map(float, input("Please enter num list ").split()))
    return (lst)


def main():
    ist = get_list()
    result = culcul(ist)
    return result


result = main()
print(result)
