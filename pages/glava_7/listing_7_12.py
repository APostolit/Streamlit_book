import streamlit as st

if st.button("Домашняя"):
    st.switch_page("pages/page1.py")
if st.button("О компании"):
    st.switch_page("pages/info.py")
if st.button("Контакты"):
    st.switch_page("pages/address.py")