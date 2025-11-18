import streamlit as st

st.text('Элемент st.forma')

with st.form("my_form"):
    # Элементы формы
    st.write("Текст в пределах формы")
    slider_val = st.slider("Выберите значение слайдера")
    checkbox_val = st.checkbox("Переключатель")
    # Кнопка
    submitted = st.form_submit_button("Отправить")

st.write("Текст за пределами формы")
# Обработчик события нажатия кнопки "Отправить"
if submitted:
    st.write("Значение слайдера:", slider_val,
             "Состояние переключателя", checkbox_val)