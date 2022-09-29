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
        

# Defining the products 
products = [
            Product(   
                79.99,
                "Funny Quokka T-Shirt",
                "https://i.ibb.co/chLzdt7/tshirt.jpg",
                """
                This is a funny t-shirt with a quokkazilla on it.
                It is made of 100% cotton and is machine washable.
                It is available in the sizes: Quokka, S, M, L, XL, XXL and XXXL.
                """,
                ),
            Product(
                49.99,
                "Quokka Socks",
                "https://i.ibb.co/sP8rDpk/socks.jpg",
                """
                These are comfy socks with a quokka on it.
                It is made of 100% cotton and is machine washable.
                """,
                ),

            Product(
                129.99,
                "Quokka Plushie",
                "https://i.ibb.co/HxB18Jt/plushie.jpg",
                """
                This is a cute plushie of a quokka.
                It's perfect to comfort you during your most troubled nights.
                """,
                ),

            Product(
                59.99,
                "Quokka Mug",
                "https://i.ibb.co/LtmhQ02/mug.jpg",
                """
                A perfect mug to drink your coffee or tea. Since it's made of ceramic, it's safe to put it in the microwave and also the quokka will keep your liquid warm.
                """,
                )
    ]

# Function to display the products and add them to the cart
def pack_product(product):
    st.markdown(f"### {product.get_name()}")
    st.image(f"{product.get_image()}", width=250)
    st.markdown(f"### Investment: R$ {product.get_price()}")
    
    clp = st.expander("More Info")
    clp.markdown(f"{product.get_description()}")
    
    add_cart = st.button("Add to cart", key=product.get_name())

    if add_cart:
        st.session_state.cart.add_product(product)
    
    st.write("")

# Displaying the products
if st.session_state.logged_in:
    st.write("")
    st.write("")
    st.write("")
    st.markdown("## Our Quokka Products")
    for product in products:
        pack_product(product)
else:
    st.error("Please login to to show our products!")