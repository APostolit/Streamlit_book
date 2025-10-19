import streamlit as st

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Обложка",   # Текст на вкладке браузера
    page_icon="📘",         # Иконка на вкладке браузера
    layout="wide",          # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Свернуть боковую панель
)

# Текст по центру
# st.columns(3)[1].header("Главная страница")
st.markdown('## 📖 Интерактивная цифровая книга 🖥')

# Текст с начала страницы
st.markdown('#### Введение в веб программирование на Python с фреймворком Streamlit')

# Контейнер
cont = st.container(border=True, width=500)

# Создание колонок
with cont:
    st.image('static/Stream_Book.jpg')
