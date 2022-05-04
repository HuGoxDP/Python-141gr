"""5. Дано рядок. Виведіть третій символ цього рядка,
перші п'ять символів цього рядка, всі символи у зворотному порядку
Майданика Олександр"""


def check(s: str) -> str:
    i = len(s)
    if i < 5:
        return get_s()
    else:
        return s


def get_s():
    s = str(input("""Введите текс, должно быть больше 5 символов
S = """))

    return check(s)


def culcul(s,):
    third_ymm = s[2]
    fir_five = s[0:5]
    reversesym = s[::-1]
    return third_ymm, fir_five, reversesym


def replc():
    s = get_s()
    result1, result2, result3 = culcul(s)
    return result1, result2, result3


result1, result2, result3 = replc()
print(result1, result2, result3)
