from models.product import Product
import streamlit as st

class ProductController():
    def __init__(self):
        self._products = [
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