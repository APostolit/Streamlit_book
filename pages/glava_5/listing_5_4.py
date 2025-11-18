import streamlit as st
import time

st.text('Таймер с элементом st.empty')
with st.empty():
    for seconds in range(10):
        st.write(f"⏳ Прошло {seconds} секунд")
        time.sleep(1)
    st.write(":material/check: Прошло 10 секунд!")

bt = st.button("Перезапустить таймер")
if bt:
    st.empty()