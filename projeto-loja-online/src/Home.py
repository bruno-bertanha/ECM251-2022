import streamlit as st
from models.product import Product
from models.cart import Cart
from controllers.product_controller import ProductController

# This is the home page for the site

st.set_page_config(page_title="Quokka Store", page_icon=":moneybag:", layout="wide")

# Initializing the session state variables to support the multipage structure
if 'user' not in st.session_state:
    st.session_state.user = None
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'cart' not in st.session_state:
    st.session_state.cart = Cart()

# Top of the homepage
col1, col2, col3 = st.columns(3)

with col1: 
    st.markdown("# Quokka Store")
    st.markdown("### Welcome to the Quokka Store! 🦘")
with col2:
    st.image("https://i.ibb.co/yW9fm7k/quokka.png", width=200)
with col3:
    if st.session_state.logged_in:
        st.markdown("### Hello, " + st.session_state.user.get_username() + "!")
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.user = None
    else:
        st.markdown("### Please Login! Use the sidebar to the left.")

# Displaying the products
if st.session_state.logged_in:
    st.write("")
    st.write("")
    st.write("")
    st.markdown("## Our Quokka Products")
    for product in ProductController()._products:
        ProductController.pack_product(product)
else:
    st.error("Please login to show our products!")