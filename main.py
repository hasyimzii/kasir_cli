import sqlite3

#connection & cursor database
connection = sqlite3.connect('db-sembako.db')
cursor = connection.cursor()

def main() :
    print("Login")
    username = input("Masukkan Username : ")
    password = input("Masukkan Password : ")

    return User.login(username, password)

while True :
    main()

