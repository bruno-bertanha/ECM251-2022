import streamlit as st
from models.product import Product
from models.cart import Cart
from controllers.user_controller import UserController

st.set_page_config(page_title="Quokka Store", page_icon=":moneybag:")

if st.session_state.logged_in:
    st.write("You are logged in as " + st.session_state.user.get_username())

    st.write("Your current e-mail is " + st.session_state.user.get_email())
    ne = st.text_input("Type your new E-mail", placeholder="Your e-mail")
    if st.button("Change E-mail"):
        UserController().update_user_email(st.session_state.user, ne)
    
    np = st.text_input("Type your new Password", placeholder="Your password", type="password") 
    if st.button("Change Password"):
        UserController().update_user_password(st.session_state.user, np)

else:
    st.error("Login to access your profile!")