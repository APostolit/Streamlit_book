import streamlit as st

st.text('Элемент аудио проигрыватель st.audio')
st.audio("gaiti.mp3",
         format="audio/mpeg",
         loop=False)