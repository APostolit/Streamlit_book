import streamlit as st

st.badge("Элемент st_checkbox")
agree = st.checkbox("Печатать", value=False)
finger = st.checkbox("Подтвердить согласие", value=False)

if agree:
    st.write("Да, печатать")
else:
    st.write("Нет, не печатать")

if finger:
    st.write("Да, согласен")
else:
    st.write("Нет, не согласен")