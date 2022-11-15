import streamlit as st
from models.product import Product
from models.cart import Cart
from controllers.product_controller import ProductController

st.set_page_config(page_title="Quokka Store", page_icon=":moneybag:")

st.markdown("## Add a new product to the store")

# Product inputs
name = st.text_input("Name", placeholder="Product name")
price = st.text_input("Price", placeholder="Product price")
description = st.text_input("Description", placeholder="Product description")
image = st.text_input("Image", placeholder="Product image")

# Add product button
if st.button("Add Product"):
    if name and price and description and image:
        ProductController().add_product(Product(price, name, image, description))
    else:
        st.error("Please fill all the fields")