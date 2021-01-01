import mysql.connector
import os
from Manager import Manager
from PetugasKasir import PetugasKasir
from Toko import Toko
from Sembako import Sembako

# connection & cursor database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pbo_sembako"
)
curs = connection.cursor()


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

<<<<<<< Updated upstream
    try:
        clear()
        return data[0]
    except:
        clear()
        print("username atau password yang anda masukan salah")
=======
    if(username == "pemilik" and password == "123213") :
        return "pemilik"
    else :
        try :
            clear()
            return data[0]
        except :
            print("username atau password yang anda masukan salah")
>>>>>>> Stashed changes


def main():
    id = login()
<<<<<<< Updated upstream
    if(id[1] == "manager"):
        print("[1] lihat data sembako")
        print("[2] tambah data sembako")
        print("[3] ubah data sembako")
        print("[4] hapus data sembako")
        print("[5] lihat data kasir")
        print("[6] tambah data kasir")
        print("[7] ubah data kasir")
        print("[8] hapus data kasir")
        print("[0] keluar")

        masukan = input("Masukkan pilihan >")
        clear()

        sembako = Sembako()
        if masukan == 1:
            sembako.lihatSembako()
        elif masukan == 2:
            sembako.tambahSembako()
        # elif masukan == 3 :
        # elif masukan == 4 :
        # elif masukan == 5 :
        # elif masukan == 6 :
        # elif masukan == 7 :
        # elif masukan == 8 :
        elif masukan == 0:
            clear()

    elif(id[1] == "petugas kasir"):
        print("kasir")
    return False


main()
=======
    if(id[1] == "manager") :
        while True:
            print("[1] lihat data sembako")
            print("[2] tambah data sembako")
            print("[3] ubah data sembako")
            print("[4] hapus data sembako")
            print("[5] lihat data kasir")
            print("[6] tambah data kasir")
            print("[7] hapus data kasir")
            print("[0] keluar")

            menu = input("Masukkan pilihan>")
            clear()

            sembako = Sembako
            kasir = PetugasKasir
            if menu == 1 :
                return sembako.lihat()
            elif menu == 2 :
                return sembako.tambah()
            elif menu == 3 :
                return sembako.ubah()
            elif menu == 4 :
                return sembako.hapus()
            elif menu == 5 :
                return kasir.lihat()
            elif menu == 6 :
                return kasir.tambah()
            elif menu == 7 :
                return kasir.hapus()
            elif menu == 0 :
                break
            else :
                print("==input tidak valid!==")

    elif(id[1] == "petugas kasir") :
        while True:
            print("[1] lihat data sembako")
            print("[2] tambah data sembako")
            print("[3] ubah data sembako")
            print("[4] hapus data sembako")
            print("[5] lihat data kasir")
            print("[6] tambah data kasir")
            print("[7] hapus data kasir")
            print("[0] keluar")

            menu = input("Masukkan pilihan>")
            clear()

            sembako = Sembako
            kasir = PetugasKasir
            if menu == 1 :
                return sembako.lihat()
            elif menu == 2 :
                return sembako.tambah()
            elif menu == 3 :
                return sembako.ubah()
            elif menu == 4 :
                return sembako.hapus()
            elif menu == 5 :
                return kasir.lihat()
            elif menu == 6 :
                return kasir.tambah()
            elif menu == 7 :
                return kasir.hapus()
            elif menu == 0 :
                break
            else :
                print("==input tidak valid!==")

    elif(id == "pemilik") :
        while True:
            print("[1] lihat data toko")
            print("[2] tambah data toko")
            print("[3] ubah data toko")
            print("[4] hapus data toko")
            print("[5] lihat data manager")
            print("[6] tambah data manager")
            print("[7] hapus data manager")
            print("[0] keluar")

            menu = input("Masukkan pilihan>")
            clear()

            toko = Toko
            manager = Manager
            if menu == 1 :
                return toko.lihat()
            elif menu == 2 :
                return toko.tambah()
            elif menu == 3 :
                return toko.ubah()
            elif menu == 4 :
                return toko.hapus()
            elif menu == 5 :
                return manager.lihat()
            elif menu == 6 :
                return manager.tambah()
            elif menu == 7 :
                return manager.hapus()
            elif menu == 0 :
                break
            else :
                print("==input tidak valid!==")
    return False

main()
>>>>>>> Stashed changes
