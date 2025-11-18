import streamlit as st

# Скрыть боковую панель
st.set_page_config(initial_sidebar_state="collapsed")

st.markdown("## Элемент st.help")
st.text('Справка об элементе st.title')
st.help(st.title)