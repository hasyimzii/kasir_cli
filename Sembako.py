import mysql.connector
import os

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


class Sembako:
    def __init__(self):
        pass

    def lihat(self):
        query = "select * from sembako"
        curs.execute(query)
        sembako = curs.fetchall()

        print("| id | jenis | merk | harga | stok |")
        for i in sembako:
            print(i)
        input()
        clear()

    def tambah(self):
        print("tambah sembako")
        jenis = input("jenis : ")
        merk = input("merk : ")
        harga = input("harga : ")
        stok = input("stok : ")

        query = "insert into sembako values(Null,'{}','{}','{}','{}')".format(
            jenis, merk, harga, stok)
        curs.execute(query)
        conn.commit()
        print("Berhasil Menambah")
        input()
        clear()

    def ubah(self):
        print("ubah sembako")
        query = "select * from sembako"
        curs.execute(query)
        sembako = curs.fetchall()

        print("| id | jenis | merk | harga | stok |")
        for i in sembako:
            print(i)
        idSembako = input("id sembako yang mau diubah : ")
        query = "select * from sembako where idSembako = '{}'".format(
            idSembako)
        curs.execute(query)
        sembako = curs.fetchall()

        print("id : " + str(sembako[0][0]))
        print("jenis : " + str(sembako[0][1]))
        print("merk : " + str(sembako[0][2]))
        print("harga : " + str(sembako[0][3]))
        print("stok : " + str(sembako[0][4]))
        print()

        harga = input("harga baru : ")
        stok = input("stok baru : ")

        query1 = "update sembako set harga = '{}', stok = '{}' where idSembako = '{}'".format(
            harga, stok, idSembako)
        curs.execute(query1)
        conn.commit()
        print("Berhasil Mengubah")
        input()
        clear()

    def hapus(self):
        print("hapus sembako")
        idSembako = input("id Sembako : ")

        query = "delete from sembako where idSembako = {}".format(idSembako)
        curs.execute(query)
        conn.commit()
        print("Berhasil Menghapus")
        input()
        clear()
