import streamlit as st

st.page_link("pages/page1.py", label="Домашняя", icon="🏠")
st.page_link("pages/info.py", label="О компании", icon="1️⃣")
st.page_link("pages/cr_acc.py", label="Аккаунт", icon="2️⃣", disabled=True)
st.page_link("https://dzen.ru/", label="Яндекс", icon="🌎")
st.page_link("https://rumnik.ru/", label="УМНИК", icon="🌎")