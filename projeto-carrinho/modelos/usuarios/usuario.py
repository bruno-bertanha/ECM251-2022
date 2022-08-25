from perfil import Perfil
class Usuario:
    def __init__(self, username, password, email):
        self._username = username
        self._password = password
        self._email = email
        self._perfil = Perfil(nome=username)
    
    def get_perfil(self):
        return self._perfil
    
    def get_username(self):
        return self._username
    
    def check_password(self, password):
        return self._password == password