import mysql.connector
import os
from Order import Order
from datetime import datetime

# connection & cursor database
conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="",
    database="pbo_sembako"
)
curs = conn.cursor()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


class Transaksi :
    def __init__(self):
        pass

    def lihat(self):
        print("lihat transaksi")
        query = "select * from transaksi"
        curs.execute(query)
        user = curs.fetchall()

        print("| id | tanggal | id user | id toko |")
        for i in user:
            print(i)

        input()
        print("[1] lihat detail transaksi")
        print("[2] kembali")
        menu = int(input("Masukkan pilihan>"))

        order = Order
        if menu == 1:
            idTransaksi = int(input("id transaksi : "))
            order.lihat("lihat", idTransaksi)
        elif menu == 2:
            pass
        input()
        clear()

    def tambah(self, idKasir):
        print("tambah transaksi")
        tanggal = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        idUser = idKasir

        query = "insert into transaksi values(Null,'{}','{}')".format(tanggal, idUser)
        curs.execute(query)
        conn.commit()

        idTransaksi = "select idTransaksi from transaksi order by id desc limit 1"
        order = Order
        order.tambah("tambah", idTransaksi)

        print("Berhasil Menambah")
        input()
        clear()