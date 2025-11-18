import streamlit as st
import pandas as pd
from io import StringIO

uploaded_img = st.file_uploader("Загрузить изображение",
                                 type=['png','jpeg'])
if uploaded_img is not None:
    file_details = {"Имя файла - ":uploaded_img.name,
                    "Тип файла - ":uploaded_img.type,
                    "Размер - ":uploaded_img.size}
    st.write(file_details)

uploaded_file = st.file_uploader("Загрузка CSV файлов",
                                 type='csv')
if uploaded_file is not None:
    # Преобразовать в строку с кодировкой utf-8
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # Использовать как "файловый" объект
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)