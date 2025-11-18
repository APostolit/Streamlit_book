import streamlit as st
import pandas as pd

# Функция формирования набора данных df
@st.cache_data
def get_data():
    data = {'Имя': ['Сергей', 'Михаил', 'Антон', 'Степан'],
            'Возраст': [32, 28, 41, 37],
            'Город': ['Москва', 'Казань', 'Сочи', 'Омск']}
    data = pd.DataFrame(data)
    return data

# Функция конвертирования df в CSV (в памяти)
@st.cache_data
def convert_for_download(df):
    return df.to_csv().encode("utf-8")

# Создание набора данных
df = get_data()
st.write('Набор данных, сформированный в программе')
st.write(df)
# конвертирования df в CSV
csv = convert_for_download(df)

# Кнопка загрузки данных из df
st.download_button(
    label="Скачать DataFrame📈",
    data=csv,
    file_name="data.csv",
    mime="text/csv",
    icon=":material/download:",
)

st.write('Файл с изображением')
st.image('AP_400.png')
# Кнопка загрузки изображения
with open("AP_400.png", "rb") as file:
    st.download_button(
        label="Скачать изображение🌄",
        data=file,
        file_name="my_image.png",
        mime="image/png",
        icon=":material/download:"
    )

st.write('Данные в CSV файле')
data =  spectra_df = pd.read_csv('passengers.csv')
st.write(data)
# Кнопка загрузки данных из df
st.download_button(
    label="Скачать CSV файл⬇️",
    data=csv,
    file_name="passengers.csv",
    mime="text/csv",
    icon=":material/download:",
)