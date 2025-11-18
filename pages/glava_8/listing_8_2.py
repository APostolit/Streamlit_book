import streamlit as st
import pandas as pd

# Скрыть боковую панель
st.set_page_config(initial_sidebar_state="collapsed")

# Создать набор данных
data = pd.DataFrame({
    'Фрукты': ['Яблоки', 'Груши', 'Бананы', 'Апельсины'],
    'Количество': [15, 35, 25, 45]
})

st.write('Столбчатая диаграмма st.bar_chart')
st.bar_chart(data, x='Фрукты', y='Количество')