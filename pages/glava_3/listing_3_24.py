import streamlit as st

enable = st.checkbox("Активировать камеру")
video = st.camera_input("Получите видео поток", disabled=not enable)

if video:
    st.image(video)