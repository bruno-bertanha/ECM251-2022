import streamlit as st
from models.usuarios.user import User
from controllers.user_controller import UserController

# Login Page

st.set_page_config(page_title="Quokka Store", page_icon=":moneybag:")


# Hardcoded user database

# Login page inputs
phu = st.text_input("Username", placeholder="Enter your username")
php = st.text_input("Password", placeholder="Enter your password", type="password")

# Login button to validate the inputs
if st.button("Login"):
    UserController().validate_user(phu, php)
        


