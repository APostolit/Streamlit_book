import streamlit as st
import numpy as np

st.text('Элементы st.container')

# Контейнер 1
ct_1 = st.container(border=True)
with ct_1:
    st.write("Этот график находится внутри контейнера - ct-1")
    st.bar_chart(np.random.randn(20, 3))
st.write("Этот текст за пределами контейнера")

# Контейнер 2
ct_2 = st.container(border=True)
ct_2.write("Этот текст внутри контейнера ct-2")
ct_2.write("Этот текст тоже внутри контейнера ct-2")

# Группа контейнеров
st.write("Группа контейнеров с иконками")
row1 = st.columns(3)
row2 = st.columns(3)
for col in row1 + row2:
    tile = col.container(height=120)
    tile.title(":balloon:")

# Контейнер с вертикальной прокруткой
st.write("Контейнер с вертикальной прокруткой")
long_text = "Это текст. " * 100
with st.container(height=200):
    st.markdown(long_text)

# Контейнер с кнопками
st.write("Контейнер ct-3 с кнопками")
ct_3 = st.container(border=True,
                    horizontal=True,
                    horizontal_alignment="right")
for i in range(3):
    ct_3.button(f"Кнопка {i + 1}")