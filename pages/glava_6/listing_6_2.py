import streamlit as st
import time

bt = st.button("Старт загрузки данных")
if bt:
    progress_text = "Данные загружаются. Ждите..."
    # Индикатор процесса
    my_bar = st.progress(0, text=progress_text)
    for percent in range(100):
        time.sleep(0.04)
        my_bar.progress(percent + 1, text=progress_text + str(percent))
    time.sleep(1)
    my_bar.empty()