import sqlite3

baglanti = sqlite3.connect('veritabani.db')
cursor = baglanti.cursor()

cursor.execute("SELECT * FROM tablo_adi")
veriler = cursor.fetchall()

for veri in veriler:
    print(veri)
baglanti.close()

