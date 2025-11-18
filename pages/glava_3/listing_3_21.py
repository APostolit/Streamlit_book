import streamlit as st

# Заголовок страницы
st.text('Виджеты для ввода текста st.text_input')

# Поле ввода однострочного текста
txt = st.text_input(label="Поле для вода однострочного текста")
if txt:
    st.write("Введен следующий текст:", txt)