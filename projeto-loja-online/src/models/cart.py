import streamlit as st

class Cart:
    def __init__(self):
        self._itens = []
    
    def get_total_value(self):
        return float(sum([product[0].get_price()*product[1] for product in self._itens]))
    
    def get_length(self):
        return len(self._itens)
    
    def add_product(self, product):
        fadp = True
        for p in self._itens:
            if p[0].get_name() == product.get_name():
                fadp = False
                st.write("Product already in cart!")
                break
        if fadp:
            self._itens.append([product, int(1)])
            st.write("Added to cart!")
"""
    def remove_product(self, product):
        for p in self._itens:
            if p[0].get_name() == product.get_name():
                self._itens.remove()
"""  