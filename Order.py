import mysql.connector

# connection & cursor database
conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="",
    database="pbo_sembako"
)
curs = conn.cursor()


class Order :
    def __init__(self):
        pass

    def lihat(self, idTransaksi):
        print("lihat order")
        query = "select * from order_transaksi where idTransaksi = '{}'".format(idTransaksi)
        curs.execute(query)
        user = curs.fetchall()

        print("| id | id sembako | jumlah |")
        for i in user:
            print(i)
    
    def tambah(self, idTransaksi):
        print("Masukkan detail order (ketik -1 untuk selesai)")
        while True :
            idSembako = input("id sembako : ")
            jumlah = input("jumlah : ")

            if(idSembako == -1 or jumlah == -1) :
                break
            else:
                query = "insert into order_transaksi values(Null,'{}','{}','{}')".format(idTransaksi, idSembako, jumlah)
                curs.execute(query)
                conn.commit()
        print("Berhasil Menambah")