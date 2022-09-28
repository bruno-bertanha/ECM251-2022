from perfil import Perfil
class User:
    def __init__(self, username, password, email=None):
        self._username = username
        self._password = password
        self._email = email
        self._perfil = Perfil(nome=username)
    
    
    def get_username(self):
        return self._username

    def get_password(self):
        return self._password