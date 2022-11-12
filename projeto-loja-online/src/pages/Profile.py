import streamlit as st
from models.product import Product
from models.cart import Cart

st.set_page_config(page_title="Quokka Store", page_icon=":moneybag:")

if st.session_state.logged_in:
    st.write("You are logged in as " + st.session_state.user.get_username())

    st.write("Your current e-mail is " + st.session_state.user.get_email())
    ne = st.text_input("Type your new E-mail", placeholder="Your e-mail")
    if st.button("Change E-mail"):
        st.session_state.user.set_email(ne)
    
    np = st.text_input("Type your new Password", placeholder="Your password", type="password") 
    if st.button("Change Password"):
        st.session_state.user.set_password(np)

else:
    st.error("Login to access your profile!")