"""
10. Даний розмір файла в байтах. Використовуючи операцію ділення без залишку, 
знайти кількість повних кілобайтів, які займає даний файл(1 кілобайт=1024 байта)
"""


def byte_to_kilobytes():
    print("Enter number of bytes")
    a = int(input("bytes = "))
    return print("kilobyte = " + str(int(a / 1024)))


byte_to_kilobytes()
