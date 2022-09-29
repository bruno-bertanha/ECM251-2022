import streamlit as st
from models.product import Product
from models.cart import Cart

st.set_page_config(page_title="Quokka Store", page_icon=":moneybag:")


if st.session_state.logged_in:
    st.markdown("# Quokka Store")
    st.markdown("## Your Cart:")

    if st.session_state.cart.get_length() == 0:
        st.markdown("### Your cart is empty!")
    else:
        st.markdown("### Your cart has " + str(st.session_state.cart.get_length()) + " product(s).")
        st.write("")
        st.write("")

        for product in st.session_state.cart._itens:
            with st.container():
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("#### " + product[0].get_name())
                    st.markdown("#### Price: " + str(product[0].get_price()))
                    product[1] = st.number_input("Qty", min_value=1, max_value=10, value=int(product[1]), step=1)
                    if st.button("Remove", key=product[0].get_name()):
                        st.session_state.cart._itens.remove(product)
                with col2:
                    st.image(product[0].get_image(), width=100)
            st.markdown("### ________________________________________________ ")
        
        
        total = st.session_state.cart.get_total_value()
        
        st.write("")
        st.write("")
        st.markdown("#### Select your shipping method:")
        shipping = st.radio("", ("Standard Shipping (5-7 business days)", "Express Shipping (2-4 business days)", "Quokka Shipping (Same day)"))
        if shipping == "Standard Shipping (5-7 business days)":
            shipping = 5.00
            total += shipping
        elif shipping == "Express Shipping (2-4 business days)": 
            shipping = 8.00
            total += shipping
        elif shipping == "Quokka Shipping (Same day)":
            shipping = 14.00
            total += shipping
        st.write(f"Shipping: R$ {shipping:.2f}")
            
        st.markdown("#### Select your payment method:")
        payment = st.selectbox("",
                            ("Credit Card", "Debit Card", "PayPal", "Bitcoin"))


        st.write("")
        st.markdown(f"### Total: R$ {total:.2f}")

        st.write("")
        if st.button("Checkout"):
            if st.session_state.logged_in:
                st.session_state.cart._itens.clear()
                st.success("Thank you for your purchase! 🦘")
                st.balloons()
            else:
                st.error("Please login to checkout!")
else:
    st.error("Please login to access your cart!")