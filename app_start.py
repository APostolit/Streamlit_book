import streamlit as st

# Сделать доступной всю ширину страницы
st.set_page_config(layout="wide")
st.set_page_config(initial_sidebar_state="collapsed")

# Иконка приложения
with st.sidebar:
    st.logo(image='favicon.ico', icon_image='favicon.ico', size="large")


# Создание страниц в виде объектов
home = st.Page(page="pages/home_page.py", title="📘Обложка")
pg_cat = st.Page(page="pages/catalog.py", title="🛒Каталог")
pg_company = st.Page(page="pages/about.py", title="👨‍💼О компании")
pg_adr = st.Page(page="pages/address.py", title="📞Контакты")

# Глава 1
g_1 = st.Page(page="pages/glava_1/g_1.py", title="📕Примеры Главы 1")
# pg_1_1 = st.Page('pages/glava_1/first_app.py', title="📞Пример 1.1")

# Глава 2
g_2 = st.Page(page="pages/glava_2/g_2.py", title="📕Примеры Главы 2")
# pg_1_1 = st.Page('pages/glava_1/first_app.py', title="📞Пример 1.1")

# Глава 3
g_3 = st.Page(page="pages/glava_3/g_3.py", title="📕Примеры Главы 3")
pg_3_0 = st.Page(page='pages/glava_3/list_3_5.py', title="Листинг 3.5")
pg_3_1 = st.Page(page='pages/glava_3/page1.py', title="Страница page1.py")
pg_3_2 = st.Page(page='pages/glava_3/about.py', title="Страница about.py")

# Глава 4
g_4 = st.Page(page="pages/glava_4/g_4.py", title="📕Примеры Главы 4")

# Глава 5
g_5 = st.Page(page="pages/glava_5/g_5.py", title="📕Примеры Главы 5")

# Глава 6
g_6 = st.Page(page="pages/glava_6/g_6.py", title="📕Примеры Главы 6")

# Глава 7
g_7 = st.Page(page="pages/glava_7/g_7.py", title="📕Примеры Главы 7")

# Глава 8
g_8 = st.Page(page="pages/glava_8/g_8.py", title="📕Примеры Главы 8")

# Глава 9
g_9 = st.Page(page="pages/glava_9/g_9.py", title="📕Примеры Главы 9")

# Глава 10
g_10 = st.Page(page="pages/glava_10/g_10.py", title="📕Листинги Главы 10")

# Глава 11
g_11 = st.Page(page="pages/glava_11/g_11.py", title="📕Листинги Главы 11")

# Создание навигатора страниц (главное меню)
pages = {
    "Глава 1": [g_1],
    "Глава 2": [g_2],
    "Глава 3": [g_3, pg_3_0, pg_3_1, pg_3_2],
    "Глава 4": [g_4],
    "Глава 5": [g_5],
    "Глава 6": [g_6],
    "Глава 7": [g_7],
    "Глава 8": [g_8],
    "Глава 9": [g_9],
    "Глава 10": [g_10],
    "Глава 11": [g_11],
    # "О компании": [pg_company],
    # "Контакты": [pg_adr],
}
pg = st.navigation(pages=pages, position="sidebar", expanded=False)

# Запуск навигатора страниц
pg.run()