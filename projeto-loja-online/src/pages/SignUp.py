import streamlit as st
from models.product import Product
from models.cart import Cart
from controllers.user_controller import UserController
from models.usuarios.user import User

st.set_page_config(page_title="Quokka Store", page_icon=":moneybag:")

# Login page inputs
sue = st.text_input("E-mail", placeholder="Your e-mail")
suu = st.text_input("Username", placeholder="Your username")
sup = st.text_input("Password", placeholder="Your password", type="password")

# Login button to validate the inputs
if st.button("Sign Up"):
    if sue == "" or suu == "" or sup == "":
        st.error("Please, fill all the fields!")
    else:
        user = User(suu, sup, sue)
        UserController().sign_up(user)
        
