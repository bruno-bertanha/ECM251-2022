#from perfil import Perfil
class User:
    def __init__(self, username, password, email):
        self._username = username
        self._password = password
        self._email = email
        #self._perfil = Perfil(nome=username)
    
    
    def get_username(self):
        return self._username

    def get_password(self):
        return self._password
    
    def get_email(self):
        return self._email
    
    def set_email(self, email):
        self._email = email
    
    def set_password(self, password):
        self._password = password