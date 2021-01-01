import mysql.connector
import os
from Manager import *
from Sembako import *

#connection & cursor database
connection = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="pbo_sembako"
)
curs = connection.cursor()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def login() :
    print("Login")
    username = str(input("Masukkan Username : "))
    password = str(input("Masukkan Password : "))

    query = "select idUser, jabatan from user where username = '{}' and password = '{}'".format(username,password)
    curs.execute(query)   
    data = curs.fetchall()

    try :
        clear()
        return data[0]
    except :
        clear()
        print("username atau password yang anda masukan salah")

def main() :
    id = login()
    if(id[1] == "manager") :
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
        if masukan == 1 :
            sembako.lihatSembako()
        elif masukan == 2 :
            sembako.tambahSembako()
        # elif masukan == 3 :
        # elif masukan == 4 :
        # elif masukan == 5 :
        # elif masukan == 6 :
        # elif masukan == 7 :
        # elif masukan == 8 :
        elif masukan == 0 :
            pass

    elif(id[1] == "petugas kasir") :
        print("kasir")

main()