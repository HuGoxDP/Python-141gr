"""По варіантах - завдання #1
3 Назви, адреси та поштові індекси в файл address_index.csv
По варіантах - завдання #2
1 З формою фінансування Державна (собрал много фильтров в один, чтобы выполнить
это задание надо выбрать 1 З формою фінансування Державна, 1 = Державна )
Майданика Олександр"""


import csv
import requests


def check(reg, cd):
    a = reg in cd
    if a is False:
        print('enter another code')
        return get_reg()
    else:
        return reg


def get_reg():
    cd = ["01", "05", "07", "12", "14", "18", "21", "23", "26", "32",
          "35", "44", "46", "48", "51", "53", "56", "59", "61", "63",
          "65", "68", "71", "73", "74", "80", "85"]
    print("Коди регіонів: " + str(cd))
    reg = str(input('enter region code = '))
    return check(reg, cd)


def requir(reg):
    req = requests.get(
        'https://registry.edbo.gov.ua/api/universities/?ut=1&lc='+reg+'&exp=json')
    try:
        universities: list = req.json()
    except Exception as ex:
        return print("Не вдалося отримати доступ к закладам регіона {}".format(reg)), exit(0)
    return universities


def various():
    var = int(input("""
1 З формою фінансування
2 З посадою керівника
3 З роком заснування
"""))
    while var != 1 and var != 2 and var != 3:
        var = int(input("нет такого варианта, выберете другой "))
    if var == 1:  # финансирование
        return fin()
    elif var == 2:  # посада
        return pos()
    elif var == 3:  # Год
        return years()


def fin():
    var2 = 0
    while var2 != 1 and var2 != 2 and var2 != 3:
        var2 = int(input("""
1 = Державна
2 = Приватна
3 = Комунальна
"""))
    if var2 == 1:
        filt = "Державна"
    elif var2 == 2:
        filt = "Приватна"
    elif var2 == 3:
        filt = "Комунальна"
    fl_fill = 'university_financing_type_name'
    flt = "з формою  фінансування " + filt
    var3 = 0
    return filt, fl_fill, flt, var3


def pos():
    var2 = 0
    while var2 != 1 and var2 != 2 and var2 != 3 and var2 != 4 and var2 != 5 and var2 != 6 and var2 != 7:
        var2 = int(input("""
1 = Керівник
2 = декан
3 = директор
4 = начальник
5 = Ректор
6 = В.о. ректора
7 = В.о. директора
"""))
    if var2 == 1:
        filt = "Керівник"
    elif var2 == 2:
        filt = "декан"
    elif var2 == 3:
        filt = "директор"
    elif var2 == 4:
        filt = "начальник"
    elif var2 == 5:
        filt = "Ректор"
    elif var2 == 6:
        filt = "В.о. ректора"
    elif var2 == 7:
        filt = "В.о. директора"
    fl_fill = 'university_director_post'
    flt = " З посадою " + filt
    var3 = 0
    return filt, fl_fill, flt, var3


def years():
    var2 = 0
    while var2 != 1 and var2 != 2:
        var2 = int(input("""
1 - промежуток
2 - 1 год
"""))
        if var2 == 1:
            while True:
                print("Введите границы 1615-2022")
                ydown = int(input("Введите нижнююю границу "))
                yup = int(input("Введите верхнию границу "))
                if 1615 <= ydown <= 2022 and 1615 <= yup <= 2022 and ydown < yup:
                    filt = [ydown, yup]
                    flt = " З роком заснування " + str(filt[0]) + "-" + str(filt[1])
                    var3 = 1
                    break
                else:
                    print("Чиcла должно находиться в диапазоне 1615-2022")
        elif var2 == 2:
            while True:
                year = int(input("Введите год 1615-2022: "))
                if 1615 <= year <= 2022:
                    filt = year
                    flt = " З роком заснування " + str(filt)
                    var3 = 2
                    break
    fl_fill = 'registration_year'
    return filt, fl_fill, flt, var3


def filt1(universities, reg, filt, fl_fill, flt, var):
    if var == 1 or var == 2:
        try:
            if var == 1:
                fl_dt2 = [
                    {k: row[k] for k in ['university_name', 'university_name_en', 'university_address', 'post_index', fl_fill]} for row in
                    list(filter(lambda x: filt[1] >= int(x[fl_fill]) >= filt[0], universities))]
            elif var == 2:
                fl_dt2 = [
                    {k: row[k] for k in ['university_name', 'university_name_en', 'university_address', 'post_index', fl_fill]} for row in
                    list(filter(lambda x: int(x[fl_fill]) == filt, universities))]
        except Exception as ex:
            return print("цей регіон {} не має університетів " + str(flt).format(reg)), 0
    if var == 0:
        try:
            fl_dt2 = [{k: row[k] for k in ['university_name', 'university_name_en', 'university_address', 'post_index', fl_fill]}for row in
                      list(filter(lambda x: x[fl_fill].casefold() == filt.casefold(), universities))]
        except Exception as ex:
            return print("цей регіон {} не має університетів " + str(flt).format(reg)), 0
    if len(fl_dt2) == 0:
        return print("цей регіон {} не має університетів " + str(flt).format(reg)), 0
    return fl_dt2, 1


def writ_er(reg, fl_dt, fl_dt2, a):
    with open('universities_'+reg+'.csv', mode='w', encoding='CP1251') as f:
        writer = csv.DictWriter(f, fieldnames=fl_dt[0].keys())
        writer.writeheader()
        writer.writerows(fl_dt)
    if a == 1:
        with open('address_index.csv', mode='w', encoding='CP1251') as fw:
            writer = csv.DictWriter(fw, fieldnames=fl_dt2[0].keys())
            writer.writeheader()
            writer.writerows(fl_dt2)


def main():
    region = get_reg()
    lst = requir(region)
    filt, fl_fill, flt, var3 = various()
    fis, a = filt1(lst, region, filt, fl_fill, flt, var3)
    writ_er(region, lst, fis, a)


main()
