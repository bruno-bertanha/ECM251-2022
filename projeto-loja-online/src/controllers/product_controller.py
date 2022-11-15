from models.product import Product
import streamlit as st
from dao.Products_Dao import ProductDAO

class ProductController():
    def __init__(self):
        pass
    

    def pack_product(product):
        st.markdown(f"### {product.get_name()}")
        st.image(f"{product.get_image()}", width=250)
        st.markdown(f"### Investment: R$ {product.get_price()}")
        
        clp = st.expander("More Info")
        clp.markdown(f"{product.get_description()}")
        
        add_cart = st.button("Add to cart", key=product.get_name())

        if add_cart:
            st.session_state.cart.add_product(product)
        
        st.write("")
    
    def add_product(self, product):
        try:
            ProductDAO.get_instance().add_product(product)
            st.success("Product added successfully!")
        except Exception as e:
            st.error("Product could not be added!") 
            st.error(e)

    def get_product(self, name):
        try:
            return ProductDAO.get_instance().get_product(name)
        except Exception as e:
            st.error("Product could not be retrieved!")
            st.error(e)
    
    def get_all_products(self):
        try:
            return ProductDAO.get_instance().get_all_products()
        except Exception as e:
            st.error("Products could not be retrieved!")
            st.error(e)