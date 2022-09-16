import streamlit as st
from modelos.item import Item

col1, col2 = st.columns(2)

with col1: 
    st.markdown("# Quokka Store")
    st.markdown("### Welcome to the Quokka Store! 🦘")
with col2:
    st.image("media/quokka.png", width=200) 

st.write("")
st.write("")
st.write("")
st.markdown("## Our Quokka Products")

# Defining the products 

prod1 = Item(   
            79.99,
            "Funny Quokka T-Shirt",
            "media/tshirt.jpg",
            """
            This is a funny t-shirt with a quokkazilla on it.
            It is made of 100% cotton and is machine washable.
            It is available in the sizes: Quokka, S, M, L, XL, XXL and XXXL.
            """,
            )
prod2 = Item(
            49.99,
            "Quokka Socks",
            "media/socks.jpg",
            """
            These are comfy socks with a quokka on it.
            It is made of 100% cotton and is machine washable.
            """,
            )

prod3 = Item(
            129.99,
            "Quokka Plushie",
            "media/plushie.jpg",
            """
            This is a cute plushie of a quokka.
            It's perfect to comfort you during your most troubled nights.
            """,
            )

prod4 = Item(
            59.99,
            "Quokka Mug",
            "media/mug.jpg",
            """
            A perfect mug to drink your coffee or tea. Since it's made of ceramic, it's safe to put it in the microwave and also the quokka will keep your liquid warm.
            """,
            )

def pack_product(product):
    st.markdown(f"### {product.get_name()}")
    st.image(f"{product.get_image()}", width=250)
    st.markdown(f"### Investment: R$ {product.get_price()}")
    
    clp = st.expander("More Info")
    clp.markdown(f"{product.get_description()}")
    
    st.button("Add to cart", key=product.get_name())
    st.write("")

pack_product(prod1)
pack_product(prod2)
pack_product(prod3)
pack_product(prod4)

