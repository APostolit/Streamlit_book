import streamlit as st

st.text("Элементы st.toggle")

tog_1 = st.toggle("Открыть доступ")
if tog_1:
    st.write("Состояние переключателя", tog_1)

toggle_value = st.toggle("Состояние переключателя", value=False)
# Отобразить сообщение на основе состояния переключателя
if toggle_value:
    st.write("Переключатель включен -", toggle_value)
else:
    st.write("Переключатель выключен -", toggle_value)