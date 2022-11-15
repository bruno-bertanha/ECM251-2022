from models.usuarios.user import User
import streamlit as st
from dao.Users_Dao import UserDAO 

class UserController():
    def __init__(self):
        self._users = [
            User('Bruno', 'senha', 'bruno@gmail.com'), 
            User('Quokka', 'quokka', 'quokka@gmail.com'), 
            User('admin', 'admin', 'admin@gmail.com'),
        ]
    
    def sign_up(self, user):
        try:
            UserDAO.get_instance().sign_up(user)
            st.success("User created successfully!")
        except Exception as e:
            st.error("User could not be created!")
            st.error(e)

    def get_user(self, username):
        try:
            return UserDAO.get_instance().get_user(username)
        except Exception as e:
            st.error("User could not be retrieved!")
            st.error(e)

    def update_user_email(self, user, ne):
        try:
            UserDAO.get_instance().update_user_email(user, ne)
            st.success("Email updated successfully!")
        except Exception as e:
            st.error("Email could not be updated!")
            st.error(e)
    
    def update_user_password(self, user, np):
        try:
            UserDAO.get_instance().update_user_password(user, np)
            st.success("Password updated successfully!")
        except Exception as e:
            st.error("Password could not be updated!")
            st.error(e)
    
    def get_all_users(self):
        try:
            return UserDAO.get_instance().get_all_users()
        except Exception as e:
            st.error("Users could not be retrieved!")
            st.error(e)


    def validate_user(self, phu, php):
        if st.session_state.logged_in == False:
            userDB = UserDAO.get_instance().get_user(phu)
            if userDB.get_password() == php:
                    st.session_state.logged_in = True
                    st.session_state.user = userDB
                    st.success("Logged in successfully!")
            if st.session_state.logged_in == False:
                st.error("Invalid username or password!")
        else: 
            st.write("You are already logged in as " + st.session_state.user.get_username())