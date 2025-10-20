import streamlit as st

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Контакты", # Текст на вкладке браузера
    page_icon="☎️",          # Иконка на вкладке браузера
    layout="wide",           # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Свернуть боковую панель
)

st.markdown("## 🏙️ Контакты")
st.markdown("#### 📬 Адрес: Город Мытищи, ул. Кропоткина, д. 17")
st.markdown("#### 📧 e-mail: info-iis@mail.ru")
st.markdown('#### ☎️ Тел.: +7 915-222-22-22')
st.markdown('#### 🌍 Карта')
st.image('static/adres.jpg')
