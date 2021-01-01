import mysql.connector

# connection & cursor database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pbo_sembako"
)
curs = connection.cursor()


class Manager:
    def __init__(self):
        pass

    def lihat(self):
        print("lihat manager")
        query = "select * from user where jabatan = 'manager'"
        curs.execute(query)
        user = curs.fetchall()
        for i in user:
            print(i)

    def tambah(self):
        print("tambah manager")
        username = str(input("nama : "))
        password = str(input("nama : "))

        query = "insert into user values('','{}','{}','manager')".format(
            username, password)
        curs.execute(query)
        curs.commit()
        print("Berhasil Menambah")

    def hapus(self):
        print("hapus Manager")
        username = str(input("username : "))

        query = "delete from user where username = {}".format(username)
        cursor.execute(query)
        conn.commit()
        print("Berhasil Menghapus")
