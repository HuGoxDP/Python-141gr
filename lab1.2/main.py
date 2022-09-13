import csv
import requests


def print_h1():
    req = requests.get("https://ksu24.kspu.edu/info")
    print(req.status_code)
    print(req.encoding)
    universities: list = req.json() 
    fl_dt2 = [
        {k: row[k] for k in []} for row in
        list]

    with open('address_index.csv', mode='w', encoding='CP1251') as fw:
        writer = csv.DictWriter(fw, fieldnames=fl_dt2[0].keys())
        writer.writeheader()
        writer.writerows(fl_dt2)
        
        
print_h1();