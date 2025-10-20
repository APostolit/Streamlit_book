import streamlit as st

# Сделать доступной всю ширину страницы
st.set_page_config(layout="wide")

# Иконка приложения
with st.sidebar:
    st.logo(image='favicon.ico', icon_image='favicon.ico', size="large")

# Создание страниц в виде объектов
home = st.Page(page="pages/home_page.py", title="🏠Домашняя")
pg_cat = st.Page(page="pages/catalog.py", title="🛒Каталог")
pg_company = st.Page(page="pages/about.py", title="👨‍💼О компании")
pg_adr = st.Page(page="pages/address.py", title="📞Контакты")

# Создание навигатора страниц (главное меню)
pg = st.navigation(pages=[home, pg_cat, pg_company, pg_adr], position="top")

# Запуск навигатора страниц
pg.run()