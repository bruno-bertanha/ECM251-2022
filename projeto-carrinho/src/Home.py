import streamlit as st

col1, col2 = st.columns(2)

with col1: 
    st.markdown("# Quokka Store")
    st.markdown("### Welcome to the Quokka Store!")
with col2:
    st.image("media/quokka.png", width=150) 

st.write("")
st.write("")
st.write("")
st.markdown("## Our Quokka Products")

# Defining the products into expanders

# Product 1
st.markdown("### Funny Quokka T-Shirt")
st.image("media/tshirt.jpg", width=250)
st.markdown("### Investment: R$ 79,90")
tshirt = st.expander("More Info")

tshirt.write("This is a funny t-shirt with a quokkazilla on it.")
tshirt.write("It is made of 100% cotton and is machine washable.")
tshirt.write("It is available in sizes Quokka, S, M, L, XL, XXL and XXXL.")
st.button("Add to cart")

# Product 2
st.markdown("### Funny Quokka T-Shirt")
st.image("media/tshirt.jpg", width=250)
st.markdown("### Investment: R$ 79,90")
tshirt = st.expander("More Info")

tshirt.write("This is a funny t-shirt with a quokkazilla on it.")
tshirt.write("It is made of 100% cotton and is machine washable.")
tshirt.write("It is available in sizes Quokka, S, M, L, XL, XXL and XXXL.")
st.button("Add to cart")