import streamlit as st

class Cart:
    def __init__(self):
        self._itens = []
    
    def get_total_value(self):
        return float(sum([item[0].get_price()*item[1] for item in st.session_state.cart]))
    
    def get_length(self):
        return len(self._itens)
    
    def add_iten(self, product):
        fadp = True
        for p in st.session_state.cart:
            if p[0].get_name() == product.get_name():
                p[1] += 1
                fadp = False
                break
        if fadp:
            st.session_state.cart.append([product, 1])
            st.write("Added to cart!")
    
    def remove_iten(self, item):
        self._itens.remove(item)