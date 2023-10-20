import csv

with open('veriler.csv', 'r') as dosya:
    veriler = csv.reader(dosya)
    for satir in veriler:
        print(satir)