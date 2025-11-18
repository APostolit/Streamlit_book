import time
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image

txt = """
Функция st.write_stream в библиотеке Streamlit позволяет писать данные 
в приложение в режиме потоковой передачи. 
Это позволяет динамически обновлять отображаемый контент 
по мере поступления новых данных.
"""

def stream_data():
    # Вывод текста
    for word in txt.split(" "):
        yield word + " "
        time.sleep(0.10)

    # Вывод набора данных
    yield pd.DataFrame(
        np.random.randn(5, 10),
        columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
    )

    # Вывод изображения
    yield Image.open('AP_400.png')


if st.button("Загрузить элементы"):
    st.write_stream(stream_data)