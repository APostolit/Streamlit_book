import streamlit as st

# Заголовок страницы
st.text('Виджеты для ввода времени st.time_input')

# Поле для ввода времени с шагом 15 мин
t = st.time_input(label="Назначить время встречи",
                  value='now')
st.write("Время встречи:", t)

# Поле для ввода времени с шагом 1 мин
t1 = st.time_input("Установить время будильник",
                   value=None,
                   step=60)
st.write("Будильник установлен на время:", t1)