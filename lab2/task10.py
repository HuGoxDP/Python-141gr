"""10. Дано ціле число в діапазоні 100-999. Вивести рядок-опис даного числа,
наприклад: 256 - "двісті п'ятдесят шість", 814 - "вісімсот чотирнадцять»."""


def getnum():
    x = int(input("x = "))
    return x


def check(x):
    while True:
       if 99 < x < 1000:
           break
       else:
           x = int(input("""Error \nplease enter x, which 99 < x < 1000  \nx = """))
    return x


def des_line():
    x = getnum()
    chekedx = check(x)
    description = "x ="
    
    match(int(chekedx / 100)):
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

    if(int(chekedx % 100) < 20 and (chekedx % 100) > 9):
        match(int(chekedx % 100)):
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

    elif(int((chekedx % 100) > 19)):
        match(int((chekedx % 100) - (chekedx % 10))):
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

    if(int(chekedx % 100) < 10 or int(chekedx % 100) > 19 and (chekedx % 100) > 0):
        match(int(chekedx % 10)):
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
    return description


description = des_line()
print(description)
