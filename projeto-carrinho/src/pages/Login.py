import streamlit as st
from modelos.usuarios.usuario import User
from Home import *

users = [
            User('Bruno', 'senha'), 
            User('Quokka', 'quokka'), 
            User('admin', 'admin'),
        ]

phu = st.text_input("Username", placeholder="Enter your username")
php = st.text_input("Password", placeholder="Enter your password", type="password")

if st.button("Login"):
    if st.session_state.logged_in == False:
        for user in users:
            if user.get_username() == phu and user.get_password() == php:
                st.session_state.logged_in = True
                st.session_state.user = user
                st.success("Logged in successfully!")
                break
            else:
                st.error("Incorrect username or password!")
                break
    else: 
        st.write("You are already logged in as " + st.session_state.user.get_username())
        


