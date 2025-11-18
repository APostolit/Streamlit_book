import streamlit as st

st.badge("Элемент st_color_picker")
color = st.color_picker("Выберите цвет", "#00f900")
st.write("Выбран цвет -", color)