"""
10. Даний розмір файла в байтах. Використовуючи операцію ділення без залишку, 
знайти кількість повних кілобайтів, які займає даний файл(1 кілобайт=1024 байта)
"""


def bite_to_kilobytes():
    print("Enter a positive number")
    a = int(input("a = "))
    return print(int(a / 1024))


bite_to_kilobytes()
