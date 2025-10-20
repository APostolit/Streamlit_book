import streamlit as st

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Домашняя", # Текст на вкладке браузера
    page_icon='👨',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="expanded",  # Раскрыть боковую панель
)

# Создать объект - страница
pg_company = st.Page(page="pages/about.py", title="👨‍💼О компании")

pg_3_1 = st.Page(page='pages/glava_3/page1.py', title="Страница page1.py")
# Создать боковую панель
sb = st.sidebar
with sb:
    # Создать ссылки на страницы
    st.page_link(pg_3_1, label="Страница 1", icon="1️⃣")
    st.page_link(pg_company, label="О компании", icon="👷🏼")
    st.page_link("https://dzen.ru", label="Яндекс", icon="🌎")

pg_3_1 = st.Page(page='pages/glava_3/page1.py', title="Страница page1.py")
pg_3_2 = st.Page(page='pages/glava_3/about.py', title="Страница about.py")
# pg_3_3 = st.Page(page='https://dzen.ru', title="Яндекс")
pages = {"Страница page1.py": [pg_3_1],
         "Страница about.py": [pg_3_2],
         }
pg = st.navigation(pages=pages, position="top", expanded=False)

# Запуск навигатора страниц
pg.run()