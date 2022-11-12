from models.usuarios.user import User
import streamlit as st

class UserController():
    def __init__(self):
        self._users = [
            User('Bruno', 'senha', 'bruno@gmail.com'), 
            User('Quokka', 'quokka', 'quokka@gmail.com'), 
            User('admin', 'admin', 'admin@gmail.com'),
        ]
    
    def validate_user(self, phu, php):
        if st.session_state.logged_in == False:
            for user in self._users:
                if user.get_username() == phu and user.get_password() == php:
                    st.session_state.logged_in = True
                    st.session_state.user = user
                    st.success("Logged in successfully!")
                    break
            if st.session_state.logged_in == False:
                st.error("Invalid username or password!")
        else: 
            st.write("You are already logged in as " + st.session_state.user.get_username())