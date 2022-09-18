import streamlit as st
from modelos.item import Item

st.set_page_config(page_title="Quokka Store", page_icon=":moneybag:")



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
                st.markdown("#### " + item[0].get_name())
                st.markdown("#### Price: " + str(item[0].get_price()))
                item[1] = st.number_input("Qty", min_value=1, max_value=10, value=item[1], step=1)
                if st.button("Remove", key=item[0].get_name()):
                    st.session_state.cart.remove(item)
            with col2:
                st.image(item[0].get_image(), width=100)
        st.markdown("### ________________________________________________ ")
    
    
    total = float(sum([item[0].get_price()*item[1] for item in st.session_state.cart]))
    
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