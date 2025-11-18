import streamlit as st
import time
import numpy as np
from numpy.random import default_rng as rng

# Первый элемент st.status
st_1 =  st.status("Ждите, идет формирование графика...")
with st_1:
    time.sleep(3)
    st.line_chart(np.random.randn(20, 3))
    st_1.update(
        label="Формирование графика завершено!",
        state="complete",
        expanded=False)

# Второй элемент st.status
with st.status("Ждите, идет загрузка данных...", expanded=True) as status:
    # Набор данных DataFrame
    df = rng(0).standard_normal((5, 1))
    time.sleep(2)

    status.update(label="Ждите, идет формирование таблицы...!")
    time.sleep(5)

    # Две колонки с указанием ширины
    col1, col2 = st.columns([1, 3], border=True)
    # Вставить график в 1-ю колонку
    col1.subheader("Таблица с данными")
    col1.write(df)

    # Вставить данные во 2-ю колонку
    status.update(label="Ждите, идет формирование графика...!")
    time.sleep(5)
    col2.subheader("График")
    col2.line_chart(df)
    status.update(label="Все элементы загружены!")
    time.sleep(5)

    status.update(
        label="Загрузка данных завершена!",
        state="complete",
        expanded=True
    )

st.button("Обновить")