class Usuario:
    def __init__(self, username, password, email):
        self._username = username
        self._password = password
        self._email = email
    
    def get_username(self):
        return self._username
    
    def check_password(self, password):
        return self._password == password