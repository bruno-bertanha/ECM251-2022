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
        self.conn = sqlite3.connect('C:\\Users\\bruno\\OneDrive - Instituto Maua de Tecnologia\\Prog\\ECM251-2022\\projeto-loja-online\\database\\sqlite.db', check_same_thread=False)

    def add_product(self, product):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO products (name, price, description, image) VALUES (?, ?, ?, ?)", 
            (product.get_name(), product.get_price(), product.get_description(), product.get_image()))
        self.conn.commit()
        cursor.close()
    
    def get_product(self, name):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT * FROM products WHERE name = ?", 
            (name,))
        product = cursor.fetchone()
        cursor.close()
        return Product(product[2], product[1], product[4], product[3])
    
    def get_all_products(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM products")
        products = []
        for p in cursor.fetchall():
            products.append(Product(price=p[2], 
                                    name=p[1], 
                                    image=p[4],
                                    description=p[3]))
        cursor.close()
        return products