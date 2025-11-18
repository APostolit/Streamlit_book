import streamlit as st
import pandas as pd
import altair as alt
from numpy.random import default_rng as rng
from PIL import Image

# Простая строка
st.write("Вывод простой строки")

# Строка с иконкой
st.write("Вас приветствует, *Streamlit!* :sunglasses:")

# Вывод числа
st.write(1234)

# Вывод набора данных Pandas
df = pd.DataFrame(
        {
            "Колонка 1": [1, 2, 3, 4],
            "Колонка 2": [10, 20, 30, 40],
        }
    )
st.write(df)

# Вывод нескольких элементов
st.write("1 + 1 = ", 2)
st.write("Заголовок таблицы:", df, "Текст после таблицы")

# Вывод графика
df = pd.DataFrame(rng(0).standard_normal((200, 3)), columns=["a", "b", "c"])
chart = (
    alt.Chart(df)
    .mark_circle()
    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)
st.write(chart)

# Вывод изображения
img = Image.open('AP_400.png')
st.write(img)