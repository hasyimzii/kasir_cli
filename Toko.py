import mysql.connector

# connection & cursor database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pbo_sembako"
)
curs = connection.cursor()


class Toko:
    def __init__(self):
        pass

    def lihat(self):
        print("lihat toko")
        query = "select * from toko"
        curs.execute(query)
        Toko = curs.fetchall()
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
        cursor.execute(query)
        conn.commit()
        print("Berhasil Menghapus")
