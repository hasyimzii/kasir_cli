import mysql.connector
import os
from Sembako import Sembako
from Manager import Manager
from PetugasKasir import PetugasKasir
from Toko import Toko
from Transaksi import Transaksi

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


def login():
    print("Login")
    username = str(input("Masukkan Username : "))
    password = str(input("Masukkan Password : "))

    query = "select idUser, jabatan from user where username = '{}' and password = '{}'".format(
        username, password)
    curs.execute(query)
    data = curs.fetchall()

    if(username == "pemilik" and password == "123123"):
        clear()
        return "pemilik"
    else:
        try:
            clear()
            return data[0]
        except:
            print("username atau password yang anda masukan salah")


def main():
    id = login()
    if(id[1] == "manager"):
        while True:
            print("[1] lihat data sembako")
            print("[2] tambah data sembako")
            print("[3] ubah data sembako")
            print("[4] hapus data sembako")
            print("[5] lihat data kasir")
            print("[6] tambah data kasir")
            print("[7] hapus data kasir")
            print("[0] keluar")

            menu = int(input("Masukkan pilihan>"))
            clear()

            sembako = Sembako
            kasir = PetugasKasir
            if menu == 1:
                sembako.lihat("lihat")
            elif menu == 2:
                sembako.tambah("tambah")
            elif menu == 3:
                sembako.ubah("ubah")
            elif menu == 4:
                sembako.hapus("hapus")
            elif menu == 5:
                kasir.lihat("lihat")
            elif menu == 6:
                kasir.tambah("tambah")
            elif menu == 7:
                kasir.hapus("hapus")
            elif menu == 0:
                main()
            else:
                print("==input tidak valid!==")

    elif(id[1] == "petugas kasir"):
        while True:
            print("[1] lihat data transaksi")
            print("[2] tambah data transaksi")
            print("[0] keluar")

            menu = int(input("Masukkan pilihan>"))
            clear()

            transaksi = Transaksi
            if menu == 1:
                transaksi.lihat("lihat")
            elif menu == 2:
                transaksi.tambah("tambah", id[0])
            elif menu == 0:
                main()
            else:
                print("==input tidak valid!==")

    elif(id == "pemilik"):
        while True:
            print("[1] lihat data toko")
            print("[2] tambah data toko")
            print("[3] hapus data toko")
            print("[4] lihat data manager")
            print("[5] tambah data manager")
            print("[6] hapus data manager")
            print("[0] keluar")

            menu = int(input("Masukkan pilihan>"))
            clear()

            toko = Toko
            manager = Manager
            if menu == 1:
                toko.lihat("lihat")
            elif menu == 2:
                toko.tambah("tambah")
            elif menu == 3:
                toko.hapus("hapus")
            elif menu == 4:
                manager.lihat("lihat")
            elif menu == 5:
                manager.tambah("tambah")
            elif menu == 6:
                manager.hapus("hapus")
            elif menu == 0:
                main()
            else:
                print("==input tidak valid!==")
    return False


main()
