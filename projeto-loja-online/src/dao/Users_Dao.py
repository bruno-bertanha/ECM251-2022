import sqlite3
from models.usuarios.user import User

class UserDAO:
    _instance = None
    
    def __init__(self) -> None:
        self._connect()
        
    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = UserDAO()
        return cls._instance
    
    def _connect(self):
        self.conn = sqlite3.connect('C:\\Users\\bruno\\OneDrive - Instituto Maua de Tecnologia\\Prog\\ECM251-2022\\projeto-loja-online\\database\\sqlite.db', check_same_thread=False)

    def sign_up(self, user):
        cursor = self.conn.cursor()
        cursor.execute(
            'INSERT INTO Users (name, email, password) VALUES (?, ?, ?)', 
            (user.get_username(), user.get_email(), user.get_password()))
        self.conn.commit()
        cursor.close()
    
    def get_user(self, username):
        cursor = self.conn.cursor()
        cursor.execute(
            'SELECT * FROM Users WHERE name = ?', 
            (username,))
        user = cursor.fetchone()
        cursor.close()
        return User(username= user[0], password= user[2], email= user[1])
    
    def update_user_email(self, user, ne):
        cursor = self.conn.cursor()
        cursor.execute(
            'UPDATE Users SET email = ? WHERE name = ?',
            (ne, user.get_username()))
        self.conn.commit()
        cursor.close()

    def update_user_password(self, user, np):
        cursor = self.conn.cursor()
        cursor.execute(
            'UPDATE Users SET password = ? WHERE name = ?',
            (np, user.get_username()))
        self.conn.commit()
        cursor.close()
    
    def get_all_users(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM Users')
        users = cursor.fetchall()
        cursor.close()
        return users