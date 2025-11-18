import streamlit as st
from numpy.random import default_rng as rng

# Три объекта - колонки
col1, col2, col3 = st.columns(3)

# Содержание 1-й колонки
with col1:
    st.header("Кошка")
    st.image("https://static.streamlit.io/examples/cat.jpg")

# Содержание 2-й колонки
with col2:
    st.header("Собака")
    st.image("https://static.streamlit.io/examples/dog.jpg")

# Содержание 3-й колонки
with col3:
    st.header("Сова")
    st.image("https://static.streamlit.io/examples/owl.jpg")

# Набор данных DataFrame
df = rng(0).standard_normal((5, 1))
# Две колонки с указанием ширины
col1, col2 = st.columns([3, 1], border=True)

# Вставить график в 1-ю колонку
col1.subheader("Широкая колонка с графиком")
col1.line_chart(df)

# Вставить данные во 1-ю колонку
col2.subheader("Узкая колонка с данными")
col2.write(df)