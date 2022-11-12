import streamlit as st
from models.product import Product
from models.cart import Cart

st.set_page_config(page_title="Quokka Store", page_icon=":moneybag:")

# Login page inputs
sue = st.text_input("E-mail", placeholder="Your e-mail")
suu = st.text_input("Username", placeholder="Your username")
sup = st.text_input("Password", placeholder="Your password", type="password")

# Login button to validate the inputs
if st.button("Sign Up"):
    pass
