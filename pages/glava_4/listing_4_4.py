import streamlit as st

# Скрыть боковую панель
st.set_page_config(initial_sidebar_state="collapsed")

st.markdown("## Элемент для вывода pdf файлов st.pdf")

# Показать локальный pdf- файл
st.pdf("pdf/Python_vsem.pdf", height=400)

#  Показать загруженный pdf- файл
uploaded_file = st.file_uploader("Выберите PDF файл", type="pdf")
if uploaded_file is not None:
    st.pdf(uploaded_file)