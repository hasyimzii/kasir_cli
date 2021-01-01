import mysql.connector

#connection & cursor database
connection = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="pbo_sembako"
)
curs = connection.cursor()

class Sembako :
    def __init__(self) :
        pass
    
    def lihatSembako(self) :
        query = "select * from sembako"
        curs.execute(query)
        sembako = curs.fetchall()
        for i in sembako:
            print(i)

    def tambahSembako(self) :
        print("tambah data sembako")
        jenis = str(input("jenis : "))
        merk = str(input("merk : "))
        harga = str(input("harga : "))
        stok = str(input("stok : "))

        query = "insert into jenis_sembako values('','{}')".format(jenis)
        curs.execute(query)
        curs.commit()

        idJenis = "select idJenis from jenis_sembako where jenis = '{}'".format(jenis)

        query1 = "insert into sembako values('','{}','{}','{}','{}')".format(idJenis, merk, harga, stok)
        curs.execute(query1)
        curs.commit()
        print("Berhasil!")