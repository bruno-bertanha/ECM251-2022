import sqlite3
from models.product import Product

class ProductDAO:
    _instance = None
    
    def __init__(self) -> None:
        self._connect()
        
    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = ProductDAO()
        return cls._instance
    
    def _connect(self):
        self.conn = sqlite3.connect('./database/sqlite.db', check_same_thread=False)