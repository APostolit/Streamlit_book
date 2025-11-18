import streamlit as st

# Заголовок страницы
st.text('Виджеты для ввода чисел st.number_input')

# Поле для ввода чисел
number = st.number_input("Введите число с плавающей точкой",
                         )
if number:
    st.write("Введено число ", number)
st.divider()  # Разделитель

# Поле для ввода чисел
int_number = st.number_input("Введите целое число",
                             value=0)
if int_number:
    st.write("Введено число ", int_number)