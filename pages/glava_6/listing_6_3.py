import streamlit as st
import time

bt = st.button("Загрузка данных")
if bt:
    with st.spinner("Ждите ...", show_time=True, width=400):
        time.sleep(5)
    st.success("Загрузка данных выполнена успешно!", width=400)