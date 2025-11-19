import streamlit as st

# Создание объектов - страниц
pg_acc = st.Page("pages/cr_acc.py", title="Создать аккаунт")
pg_man = st.Page("pages/manage_acc.py", title="Управление аккаунтом")
pg_inf = st.Page("pages/info.py", title="Информация о фирме")
pg_adr = st.Page("pages/address.py", title="Контакты")

# Создание объекта - вертикальное меню
menu = {
    "Ваш аккаунт": [pg_acc, pg_man],
    "Информация": [pg_inf, pg_adr]
}
# Создание навигатора страниц
pg = st.navigation(menu)
# Запуск навигатора страниц
pg.run()