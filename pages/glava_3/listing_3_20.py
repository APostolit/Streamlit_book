import streamlit as st

# Заголовок страницы
st.text('Виджеты для ввода многострочного текста st.text_area')

# Поле ввода многострочного текста
txt_ar = st.text_area(label="Введите текст")
if txt_ar:
    st.write("Введен следующий текст:", txt_ar)