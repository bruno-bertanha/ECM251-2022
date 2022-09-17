import streamlit as st
from modelos.item import Item


st.markdown("# Quokka Store")
st.markdown("## Your Cart:")

if len(st.session_state.cart) == 0:
    st.markdown("### Your cart is empty!")
else:
    st.markdown("### Your cart has " + str(len(st.session_state.cart)) + " item(s).")
    st.write("")
    st.write("")

    for item in st.session_state.cart:
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("#### " + item.get_name())
                st.markdown("#### Price: " + str(item.get_price()))
                if st.button("Remove", key=item.get_name()):
                    st.session_state.cart.remove(item)
            with col2:
                st.image(item.get_image(), width=100)
        st.markdown("### ________________________________________________ ")
    
    
    total = float(sum([item.get_price() for item in st.session_state.cart]))
    
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
            st.session_state.cart.clear()
            st.success("Thank you for your purchase! 🦘")
            st.balloons()
        else:
            st.error("Please login to checkout!")