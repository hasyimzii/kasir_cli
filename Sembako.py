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


class Sembako:
    def __init__(self):
        pass

    def lihat(self):
        query = "select * from sembako"
        curs.execute(query)
        sembako = curs.fetchall()
        for i in sembako:
            print(i)

    def tambah(self):
        print("tambah data sembako")
        jenis = str(input("jenis : "))
        merk = str(input("merk : "))
        harga = str(input("harga : "))
        stok = str(input("stok : "))

        query = "insert into sembako values(Null,'{}','{}','{}','{}')".format(
            jenis, merk, harga, stok)
        curs.execute(query)
        conn.commit()
        print("Berhasil!")

    def hapus(self):
        print("hapus toko")
        idSembako = input("ID Sembako : ")

        query = "delete from sembako where idSembako = {}".format(idSembako)
        curs.execute(query)
        conn.commit()
        print("Berhasil Menghapus")
