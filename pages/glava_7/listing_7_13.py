import streamlit as st
import pandas as pd

@st.cache_data  # caching декоратор
def load_data(url):
    data = pd.read_csv(url)
    return data

# Вызов функции загрузки данных
df = load_data("https://github.com/plotly/datasets/raw/master/uber-rides-data1.csv")
# Отображение данных
st.dataframe(df)
# Кнопка перезагрузки приложения
st.button("Обновить")