import mysql.connector

# connection & cursor database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pbo_sembako"
)
curs = connection.cursor()

class PetugasKasir(User):
    def __init__(self):
        pass

    def lihat(self):
        print("lihat manager")
        query = "select * from user where jabatan = 'petugas kasir'"
        curs.execute(query)
        user = curs.fetchall()
        for i in user:
            print(i)

    def tambah(self):
        print("tambah kasir")
        username = str(input("nama : "))
        password = str(input("nama : "))

        query = "insert into user values('','{}','{}','petugas kasir')".format(
            username, password)
        curs.execute(query)
        curs.commit()
        print("Berhasil Menambah")

    def hapus(self):
        print("hapus kasir")
        username = str(input("username : "))

        query = "delete from user where username = {}".format(username)
        curs.execute(query)
        curs.commit()
        print("Berhasil Menghapus")
