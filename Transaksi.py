import mysql.connector
import os
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
        transaksi = curs.fetchall()

        print("| id | tanggal | waktu | id user |")
        for i in transaksi:
            print("("+ str(i[0]) +", "+ str(i[1].strftime("%d/%m/%Y, %H:%M:%S")) +", "+ str(i[2]) +")")
        input()

    def tambah(self, idKasir):
        print("tambah transaksi")
        tanggal = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        idUser = idKasir

        query = "insert into transaksi values(Null,'{}','{}')".format(tanggal, idUser)
        curs.execute(query)
        conn.commit()