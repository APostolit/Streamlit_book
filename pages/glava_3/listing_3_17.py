import streamlit as st
from datetime import time
from datetime import datetime

# Заголовок страницы
st.text('Виджет для ввода данных st.slider')

# Слайдер для выбора числа
age = st.slider(label="Сколько вам лет?",
                min_value=0,
                max_value=120,
                value=25)
st.write("Мой возраст- ", age)
st.divider()  # Горизонтальная линия

# Слайдер для выбора диапазона чисел
values = st.slider(label="Выберите диапазон чисел",
                   min_value=0.0,
                   max_value=100.0,
                   value=(25.0, 75.0))
st.write("Выбран диапазон:", values)
st.divider()  # Горизонтальная линия

# Слайдер для выбора диапазона времени
appointment = st.slider(label="Запишитесь на прием:",
                        value=(time(11, 30), time(12, 45)),
                        format="hh:mm"
                        )
st.write("Ваше время приема:", appointment)
st.divider()  # Горизонтальная линия

# Слайдер для выбора даты и времени
start_time = st.slider(label="Когда нужно выехать в аэропорт",
                       value=datetime(2025, 1, 1, 9, 30),
                       format="MM/DD/YY - hh:mm",
                       )
st.write("Дата и время выезда:", start_time)
st.divider()  # Горизонтальная линия