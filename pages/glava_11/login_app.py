import streamlit as st
from Class_SQL import Sql_meneg

# Получить имя БД через st.secrets["connections"]
name_bd = st.secrets["connections"]["url_login"]
# Создать объект БД (если он еще не создан)
sql_bd = Sql_meneg(name_bd, sql='')
# Сохранить объект БД в сессии
st.session_state['sql_bd'] = sql_bd

# Открыть соединение с БД
con_bd = sql_bd.connect_to_db()
# Создать таблицу в БД с пользователями, если она еще не создана
sql_cr_tab = 'CREATE TABLE IF NOT EXISTS Users(username TEXT,password TEXT, email TEXT)'
sql_bd.create_table(con_bd, sql_cr_tab)
# Закрыть соединение с БД
con_bd.close()

# Закрыть доступ к секретным страницам приложения
if 'legal' not in st.session_state:
    st.session_state.legal = False

# Извлечь признак доступа к секретным страницам приложения
st.session_state.role = st.session_state.legal

# Настройка параметров стартовой страницы
st.set_page_config(
    page_title="Домашняя", # Текст на вкладке браузера
    page_icon='🏠',        # Иконка на вкладке браузера
    layout="wide",         # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Свернуть боковую панель
)

# Создание страниц приложения в виде объектов
home_reg = st.Page(page="pages/home_reg.py", title="🏠Домашняя")
user_reg = st.Page(page="pages/user_reg.py", title="👨‍💼‍Регистрация")
user_login = st.Page(page="pages/user_login.py", title="🏃‍♂️‍➡️🚪Вход")
user_logaut = st.Page(page="pages/user_logaut.py", title="Выход‍🚪🏃‍♂️‍➡️")
cabinet = st.Page(page="pages/cabinet.py", title="👨‍💼Кабинет")

# Иконка приложения
with st.sidebar:
    st.logo(image='favicon.ico', icon_image='favicon.ico', size="large")

# Получить признак доступа к секретным страницам
reg_user = st.session_state.role

# Варианты меню для пользователей разных категорий
if reg_user:
    # Меню для зарегистрированных пользователей
    pg = st.navigation(pages=[home_reg, cabinet, user_logaut], position="top")
else:
    # Меню для всех пользователей
    pg = st.navigation(pages=[home_reg, user_reg, user_login], position="top")

# Запуск навигатора страниц
pg.run()