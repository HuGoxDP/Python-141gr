"""10. Дано ціле число в діапазоні 100-999. Вивести рядок-опис даного числа,
наприклад: 256 - "двісті п'ятдесят шість", 814 - "вісімсот чотирнадцять»."""


def des_line(x: int):
    description = "x ="

    match(int(x / 100)):
        case 1:
            description += " Сто"
        case 2:
            description += " Двісті"
        case 3:
            description += " Триста"
        case 4:
            description += " Чотириста"
        case 5:
            description += " П'ятсот"
        case 6:
            description += " Шістсот"
        case 7:
            description += " Сімсот"
        case 8:
            description += " Вісімсот"
        case 9:
            description += " Дев'ятсот"
        case _:
            print("error")

    if(int(x % 100) < 20 and (x % 100) > 9):
        match(int(x % 100)):
            case 10:
                description += " Десять"
            case 11:
                description += " Одинадцять"
            case 12:
                description += " Дванадцять"
            case 13:
                description += " Тринадцять"
            case 14:
                description += " Чотирнадцять"
            case 15:
                description += " П'ятнадцять"
            case 16:
                description += " Шістнадцять"
            case 17:
                description += " Сімнадцять"
            case 18:
                description += " Вісімнадцять"
            case 19:
                description += " Дев’ятнадцять"

    elif(int((x % 100) > 19)):
        match(int((x % 100) - (x % 10))):
            case 20:
                description += " Двадцять"
            case 30:
                description += " Тридцять"
            case 40:
                description += " Сорок"
            case 50:
                description += " П’ятдесят"
            case 60:
                description += " Шістдесят"
            case 70:
                description += " Сімдесят"
            case 80:
                description += " Вісімдесят"
            case 90:
                description += " Дев’яносто"

    if(int(x % 100) < 10 or int(x % 100) > 19 and (x % 100) > 0):
        match(int(x % 10)):
            case 1:
                description += " Один"
            case 2:
                description += " Два"
            case 3:
                description += " Три"
            case 4:
                description += " Чотири"
            case 5:
                description += " П’ять"
            case 6:
                description += " Шість"
            case 7:
                description += " Сім"
            case 8:
                description += " Вісім"
            case 9:
                description += " Дев’ять"
    return print(description)


x = int(input("x = "))
print(x % 100)
print(x % 10)
print(x / 100)
des_line(x)
