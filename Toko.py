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

class Toko:
    def __init__(self):
        pass

    def lihat(self):
        print("lihat toko")
        query = "select * from toko"
        curs.execute(query)
        toko = curs.fetchall()
        for i in toko:
            print(i)

    def tambah(self):
        print("tambah toko")
        alamat = str(input("alamat : "))

        query = "insert into toko values('','{}')".format(alamat)
        curs.execute(query)
        curs.commit()
        print("Berhasil Menambah")

    def hapus(self):
        print("hapus toko")
        idToko = input("ID Toko : ")

        query = "delete from toko where idToko = {}".format(idToko)
        curs.execute(query)
        curs.commit()
        print("Berhasil Menghapus")
