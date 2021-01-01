import mysql.connector
import os
from User import User

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


class PetugasKasir(User):
    def __init__(self):
        pass

    def lihat(self):
        print("lihat manager")
        query = "select * from user where jabatan = 'petugas kasir'"
        curs.execute(query)
        user = curs.fetchall()

        print("| id | username | password | id toko |")
        for i in user:
            print(i)
        input()
        clear()

    def tambah(self):
        print("tambah kasir")
        username = input("username : ")
        password = input("password : ")
        idToko = input("idToko : ")

        query = "insert into user values('','{}','{}','petugas kasir', '{}')".format(username, password, idToko)
        curs.execute(query)
        conn.commit()
        print("Berhasil Menambah")
        input()
        clear()

    def hapus(self):
        print("hapus kasir")
        idUser = str(input("id petugas kasir : "))

        query = "delete from user where idUser = {}".format(idUser)
        curs.execute(query)
        conn.commit()
        print("Berhasil Menghapus")
        input()
        clear()
