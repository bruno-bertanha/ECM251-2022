import streamlit as st

col1, col2 = st.columns(2)

with col1: 
    st.title("Quokka Store")
    st.subheader("Welcome to the Quokka Store!")
with col2:
    st.image("quokka.png", width=150) 

