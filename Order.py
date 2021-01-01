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


class Order :
    def __init__(self):
        pass

    def lihat(self, idTransaksi):
        print("=============")
        print("detail order")
        query = "select * from order_transaksi where idTransaksi = '{}'".format(idTransaksi)
        curs.execute(query)
        order = curs.fetchall()

        total = 0

        for i in order:
            query1 = "select merk, harga from sembako where idSembako = '{}'".format(i[2])
            curs.execute(query1)
            sembako = curs.fetchall()

            print("merk :", sembako[0][0])
            print("harga :", sembako[0][1])
            print("jumlah :", i[3])

            total += (sembako[0][1] * i[3])

        print("total harga :", total)
        print("=============")
        input()
        clear()
    
    def tambah(self, idTransaksi):
        print("Masukkan detail order (ketik -1 untuk selesai)")
        print(idTransaksi)
        while True :
            idSembako = int(input("id sembako : "))
            jumlah = int(input("jumlah : "))

            if(idSembako > 0 or jumlah == 0) :
                query = "insert into order_transaksi values(Null,'{}','{}','{}')".format(idTransaksi, idSembako, jumlah)
                curs.execute(query)
                conn.commit()
            else:
                break
        print("Berhasil Menambah")