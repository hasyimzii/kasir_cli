from User import User
class Pemilik(User) :
    def __init__(self, username, password) :
        self.username = username
        self.password = password
    
    def getUser(self) :
        return self.username

    def getPass(self) :
        return self.password