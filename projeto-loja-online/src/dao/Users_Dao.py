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
        self.conn = sqlite3.connect('./database/sqlite.db', check_same_thread=False)