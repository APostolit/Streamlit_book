import streamlit as st

prompt = st.chat_input("Введите сообщение")
if prompt:
    st.write(f"Пользователь отправил следующее сообщение: {prompt}")