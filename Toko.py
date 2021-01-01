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


class Toko:
    def __init__(self):
        pass

    def lihat(self):
        print("lihat toko")
        query = "select * from toko"
        curs.execute(query)
        toko = curs.fetchall()

        print("| id | alamat |")
        for i in toko:
            print(i)
        input()
        clear()

    def tambah(self):
        print("tambah toko")
        alamat = str(input("alamat : "))

        query = "insert into toko values('','{}')".format(alamat)
        curs.execute(query)
        conn.commit()
        print("Berhasil Menambah")
        input()
        clear()

    def hapus(self):
        print("hapus toko")
        idToko = input("id Toko : ")

        query = "delete from toko where idToko = {}".format(idToko)
        curs.execute(query)
        conn.commit()
        print("Berhasil Menghapus")
        input()
        clear()
