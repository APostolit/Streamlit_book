import streamlit as st

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Кабинет🪑", # Текст на вкладке браузера
    page_icon='👨',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="expanded",  # Свернуть боковую панель
)

st.subheader("👨‍💼Личный кабинет🪑")
bd_user = st.session_state['user_name']
st.write("Это личный кабинет пользователя - ", '👨‍', bd_user)

with st.sidebar:
    st.write('Кабинет-', bd_user)
    # Выпадающий список для выбора роли
    sb = st.selectbox(
        "Ваш выбор",
        ["Данные", "Графики", "Изображения"]
    )
    st.write('Выбрано-', sb)