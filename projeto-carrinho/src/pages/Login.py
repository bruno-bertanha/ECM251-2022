import streamlit as st
from modelos.usuarios.usuario import User

# Login Page

# Hardcoded user database
users = [
            User('Bruno', 'senha'), 
            User('Quokka', 'quokka'), 
            User('admin', 'admin'),
        ]

# Login page inputs
phu = st.text_input("Username", placeholder="Enter your username")
php = st.text_input("Password", placeholder="Enter your password", type="password")

# Login button to validate the inputs
if st.button("Login"):
    if st.session_state.logged_in == False:
        for user in users:
            if user.get_username() == phu and user.get_password() == php:
                st.session_state.logged_in = True
                st.session_state.user = user
                st.success("Logged in successfully!")
                break
        if st.session_state.logged_in == False:
            st.error("Invalid username or password!")
    else: 
        st.write("You are already logged in as " + st.session_state.user.get_username())
        


