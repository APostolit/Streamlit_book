import streamlit as st
from datetime import datetime

# Заголовок страницы
st.text('Виджеты для ввода даты st.date_input')

# Поле для ввода даты
d = st.date_input(label="Дата вашего рождения?",
                  value=datetime(2019, 7, 6),
                  format='DD/MM/YYYY')
st.write("Вы родились:", d)
st.divider()  # Горизонтальная линия

# Текущая дата
today = datetime.now()
# следующий год
next_year = today.year + 1
# 1 января следующего года
jan_1 = datetime(next_year, 1, 1)
# 31 декабря января следующего года
dec_31 = datetime(next_year, 12, 31)
# Поле для ввода интервала дат
d1 = st.date_input(label="Выберите дату поездки в отпуск",
                   value=(jan_1, datetime(next_year, 1, 14)),
                   min_value=jan_1,
                   max_value=dec_31,
                   format="MM.DD.YYYY",)
st.write("Выбран интервал дат:", d1)