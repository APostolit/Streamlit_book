import streamlit as st

# Код страница в стартовом файле в виде функции
def page2():
    st.title("Это страница - page2")
    st.write("Это страница реализована в виде функции,")
    st.write("которая находится в стартовом модуле - start_app_1.py")

# Создание навигатора страниц
pg = st.navigation(["pages/page1.py", page2])
# Запуск навигатора страниц
pg.run()
