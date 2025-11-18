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
g_1 = st.Page(page="pages/glava_1/g_1.py", title="📕Листинги главы 1")
pg_1_1 = st.Page('pages/glava_1/listing_1_1.py', title="🚀Выполнить 1.1")

# Глава 2
g_2 = st.Page(page="pages/glava_2/g_2.py", title="📕Листинги главы 2")
pg_2_1 = st.Page('pages/glava_2/listing_2_1.py', title="🚀Выполнить 2.1")
pg_2_2 = st.Page('pages/glava_2/listing_2_2.py', title="🚀Выполнить 2.2")
pg_2_3 = st.Page('pages/glava_2/listing_2_3.py', title="🚀Выполнить 2.3")
pg_2_4 = st.Page('pages/glava_2/listing_2_4.py', title="🚀Выполнить 2.4")
pg_2_5 = st.Page('pages/glava_2/listing_2_5.py', title="🚀Выполнить 2.5")
pg_2_6 = st.Page('pages/glava_2/listing_2_6.py', title="🚀Выполнить 2.6")
pg_2_7 = st.Page('pages/glava_2/listing_2_7.py', title="🚀Выполнить 2.7")
pg_2_8 = st.Page('pages/glava_2/listing_2_8.py', title="🚀Выполнить 2.8")

# Глава 3
g_3 = st.Page(page="pages/glava_3/g_3.py", title="📕Листинги Главы 3")
pg_3_1 = st.Page('pages/glava_3/listing_3_1.py', title="🚀Выполнить 3.1")
pg_3_2 = st.Page('pages/glava_3/listing_3_2.py', title="🚀Выполнить 3.2")
pg_3_3 = st.Page('pages/glava_3/listing_3_3.py', title="🚀Выполнить 3.3")
pg_3_4 = st.Page('pages/glava_3/listing_3_4.py', title="🚀Выполнить 3.4")
# pg_3_5 = st.Page('pages/glava_3/list_3_5.py', title="🚀Выполнить 3.5")
pg_list_3_5 = st.Page(page='pages/glava_3/list_3_5.py', title="🚀Выполнить 3.5")
pg_3_6 = st.Page('pages/glava_3/listing_3_6.py', title="🚀Выполнить 3.6")
pg_3_7 = st.Page('pages/glava_3/listing_3_7.py', title="🚀Выполнить 3.7")
pg_3_8 = st.Page('pages/glava_3/listing_3_8.py', title="🚀Выполнить 3.8")
pg_3_9 = st.Page('pages/glava_3/listing_3_9.py', title="🚀Выполнить 3.9")
pg_3_10 = st.Page('pages/glava_3/listing_3_10.py', title="🚀Выполнить 3.10")
pg_3_11 = st.Page('pages/glava_3/listing_3_11.py', title="🚀Выполнить 3.11")
pg_3_12 = st.Page('pages/glava_3/listing_3_12.py', title="🚀Выполнить 3.12")
pg_3_13 = st.Page('pages/glava_3/listing_3_13.py', title="🚀Выполнить 3.13")
pg_3_14 = st.Page('pages/glava_3/listing_3_14.py', title="🚀Выполнить 3.14")
pg_3_15 = st.Page('pages/glava_3/listing_3_15.py', title="🚀Выполнить 3.15")
pg_3_16 = st.Page('pages/glava_3/listing_3_16.py', title="🚀Выполнить 3.16")
pg_3_17 = st.Page('pages/glava_3/listing_3_17.py', title="🚀Выполнить 3.17")
pg_3_18 = st.Page('pages/glava_3/listing_3_18.py', title="🚀Выполнить 3.18")
pg_3_19 = st.Page('pages/glava_3/listing_3_19.py', title="🚀Выполнить 3.19")
pg_3_20 = st.Page('pages/glava_3/listing_3_20.py', title="🚀Выполнить 3.20")
pg_3_21 = st.Page('pages/glava_3/listing_3_21.py', title="🚀Выполнить 3.21")
pg_3_22 = st.Page('pages/glava_3/listing_3_22.py', title="🚀Выполнить 3.22")
pg_3_23 = st.Page('pages/glava_3/listing_3_23.py', title="🚀Выполнить 3.23")
pg_3_24 = st.Page('pages/glava_3/listing_3_24.py', title="🚀Выполнить 3.24")

pg_page1 = st.Page(page='pages/glava_3/page1.py', title="Страница page1.py")
pg_about = st.Page(page='pages/glava_3/about.py', title="Страница about.py")

# Глава 4
g_4 = st.Page(page="pages/glava_4/g_4.py", title="📕Листинги Главы 4")
pg_4_1 = st.Page('pages/glava_4/listing_4_1.py', title="🚀Выполнить 4.1")
pg_4_2 = st.Page('pages/glava_4/listing_4_2.py', title="🚀Выполнить 4.2")
pg_4_3 = st.Page('pages/glava_4/listing_4_3.py', title="🚀Выполнить 4.3")
pg_4_4 = st.Page('pages/glava_4/listing_4_4.py', title="🚀Выполнить 4.4")
pg_4_5 = st.Page('pages/glava_4/listing_4_5.py', title="🚀Выполнить 4.5")

# Глава 5
g_5 = st.Page(page="pages/glava_5/g_5.py", title="📕Листинги главы 5")
pg_5_1 = st.Page('pages/glava_5/listing_5_1.py', title="🚀Выполнить 5.1")
pg_5_2 = st.Page('pages/glava_5/listing_5_2.py', title="🚀Выполнить 5.2")
pg_5_3 = st.Page('pages/glava_5/listing_5_3.py', title="🚀Выполнить 5.3")
pg_5_4 = st.Page('pages/glava_5/listing_5_4.py', title="🚀Выполнить 5.4")
pg_5_5 = st.Page('pages/glava_5/listing_5_5.py', title="🚀Выполнить 5.5")
pg_5_6 = st.Page('pages/glava_5/listing_5_6.py', title="🚀Выполнить 5.6")
pg_5_7 = st.Page('pages/glava_5/listing_5_7.py', title="🚀Выполнить 5.7")
pg_5_8 = st.Page('pages/glava_5/listing_5_8.py', title="🚀Выполнить 5.8")
pg_5_9 = st.Page('pages/glava_5/listing_5_9.py', title="🚀Выполнить 5.9")
pg_5_10 = st.Page('pages/glava_5/listing_5_10.py', title="🚀Выполнить 5.10")
pg_5_11 = st.Page('pages/glava_5/listing_5_11.py', title="🚀Выполнить 5.11")
pg_5_12 = st.Page('pages/glava_5/listing_5_12.py', title="🚀Выполнить 5.12")
pg_5_13 = st.Page('pages/glava_5/listing_5_13.py', title="🚀Выполнить 5.13")
pg_5_14 = st.Page('pages/glava_5/listing_5_14.py', title="🚀Выполнить 5.14")
pg_5_15 = st.Page('pages/glava_5/listing_5_15.py', title="🚀Выполнить 5.15")
pg_5_16 = st.Page('pages/glava_5/listing_5_16.py', title="🚀Выполнить 5.16")

# Глава 6
g_6 = st.Page(page="pages/glava_6/g_6.py", title="📕Листинги главы 6")
pg_6_1 = st.Page('pages/glava_6/listing_6_1.py', title="🚀Выполнить 6.1")
pg_6_2 = st.Page('pages/glava_6/listing_6_2.py', title="🚀Выполнить 6.2")
pg_6_3 = st.Page('pages/glava_6/listing_6_3.py', title="🚀Выполнить 6.3")
pg_6_4 = st.Page('pages/glava_6/listing_6_4.py', title="🚀Выполнить 6.4")
pg_6_5 = st.Page('pages/glava_6/listing_6_5.py', title="🚀Выполнить 6.5")
pg_6_6 = st.Page('pages/glava_6/listing_6_6.py', title="🚀Выполнить 6.6")
pg_6_7 = st.Page('pages/glava_6/listing_6_7.py', title="🚀Выполнить 6.7")

# Глава 7
g_7 = st.Page(page="pages/glava_7/g_7.py", title="📕Примеры Главы 7")

# Глава 8
g_8 = st.Page(page="pages/glava_8/g_8.py", title="📕Листинги Главы 8")
pg_8_1 = st.Page('pages/glava_8/listing_8_1.py', title="🚀Выполнить 8.1")
pg_8_2 = st.Page('pages/glava_8/listing_8_2.py', title="🚀Выполнить 8.2")
pg_8_3 = st.Page('pages/glava_8/listing_8_3.py', title="🚀Выполнить 8.3")
pg_8_4 = st.Page('pages/glava_8/listing_8_4.py', title="🚀Выполнить 8.4")
pg_8_5 = st.Page('pages/glava_8/listing_8_5.py', title="🚀Выполнить 8.5")
pg_8_6 = st.Page('pages/glava_8/listing_8_6.py', title="🚀Выполнить 8.6")
pg_8_7 = st.Page('pages/glava_8/listing_8_7.py', title="🚀Выполнить 8.7")
pg_8_8 = st.Page('pages/glava_8/listing_8_8.py', title="🚀Выполнить 8.8")
pg_8_9 = st.Page('pages/glava_8/listing_8_9.py', title="🚀Выполнить 8.9")
pg_8_10 = st.Page('pages/glava_8/listing_8_10.py', title="🚀Выполнить 8.10")
pg_8_11 = st.Page('pages/glava_8/listing_8_11.py', title="🚀Выполнить 8.11")
pg_8_12 = st.Page('pages/glava_8/listing_8_12.py', title="🚀Выполнить 8.12")

# Глава 9
g_9 = st.Page(page="pages/glava_9/g_9.py", title="📕Листинги главы 9")
pg_9_1 = st.Page('pages/glava_9/listing_9_1.py', title="🚀Выполнить 9.1")
pg_9_2 = st.Page('pages/glava_9/listing_9_2.py', title="🚀Выполнить 9.2")
pg_9_3 = st.Page('pages/glava_9/listing_9_3.py', title="🚀Выполнить 9.3")
pg_9_4 = st.Page('pages/glava_9/listing_9_4.py', title="🚀Выполнить 9.4")
pg_9_5 = st.Page('pages/glava_9/listing_9_5.py', title="🚀Выполнить 9.5")
pg_9_6 = st.Page('pages/glava_9/listing_9_6.py', title="🚀Выполнить 9.6")
pg_9_7 = st.Page('pages/glava_9/listing_9_7.py', title="🚀Выполнить 9.7")
pg_9_8 = st.Page('pages/glava_9/listing_9_8.py', title="🚀Выполнить 9.8")
pg_9_9 = st.Page('pages/glava_9/listing_9_9.py', title="🚀Выполнить 9.9")
pg_9_10 = st.Page('pages/glava_9/listing_9_10.py', title="🚀Выполнить 9.10")

# Глава 10
g_10 = st.Page(page="pages/glava_10/g_10.py", title="📕Листинги Главы 10")

# Глава 11
g_11 = st.Page(page="pages/glava_11/g_11.py", title="📕Листинги Главы 11")

# Создание навигатора страниц (главное меню)
pages = {
    "Глава 1": [g_1, pg_1_1],
    "Глава 2": [g_2, pg_2_1, pg_2_2, pg_2_3, pg_2_4, pg_2_5, pg_2_6, pg_2_7, pg_2_8],
    "Глава 3": [g_3, pg_3_1, pg_3_2, pg_3_3, pg_3_4, pg_list_3_5, pg_3_6, pg_3_7, pg_3_8,
                pg_3_9, pg_3_10, pg_3_11, pg_3_12, pg_3_13, pg_3_14, pg_3_15,
                pg_3_16, pg_3_17, pg_3_18, pg_3_19, pg_3_20, pg_3_21, pg_3_22,
                pg_3_23, pg_3_24, pg_page1, pg_about],
    "Глава 4": [g_4, pg_4_1, pg_4_2, pg_4_3, pg_4_4, pg_4_5],
    "Глава 5": [g_5,  pg_5_1,  pg_5_2,  pg_5_3,  pg_5_4,  pg_5_5,  pg_5_6,  pg_5_7,  pg_5_8,
                pg_5_9,  pg_5_10,  pg_5_11,  pg_5_12,  pg_5_13,  pg_5_14,  pg_5_15,  pg_5_16],
    "Глава 6": [g_6, pg_6_1, pg_6_2, pg_6_3, pg_6_4, pg_6_5, pg_6_6, pg_6_7],
    "Глава 7": [g_7],
    "Глава 8": [g_8, pg_8_1, pg_8_2, pg_8_3, pg_8_4, pg_8_5, pg_8_6, pg_8_7, pg_8_8,
                pg_8_9, pg_8_10, pg_8_11, pg_8_12],
    "Глава 9": [g_9, pg_9_1, pg_9_2, pg_9_3, pg_9_4, pg_9_5, pg_9_6, pg_9_7, pg_9_8,
                pg_9_9, pg_9_10],
    "Глава 10": [g_10],
    "Глава 11": [g_11],
    # "О компании": [pg_company],
    # "Контакты": [pg_adr],
}
pg = st.navigation(pages=pages, position="top", expanded=False)

# Запуск навигатора страниц
pg.run()