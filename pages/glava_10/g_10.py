import streamlit as st

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 10", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

# Текст по центру страницы
st.columns(3)[1].header("👩🏻‍💻Примеры главы 9")

# Контейнер
cont_1 = st.container(width=300)
with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги главы 10",
        ("Листинг 10.1", "Листинг 10.2", "Листинг 10.3", "Листинг 10.4",
         "Листинг 10.5", "Листинг 10.6", "Пример главы 10"),
        index=None,
        placeholder="Выберите листинг..."
    )

# Контейнер
cont_2 = st.container()
with cont_2:
    if options is None:
        st.write('Листинг не выбран')
    elif options == "Листинг 10.1":
        st.write('Код листинга 10.1')
        path = '.streamlit/config.toml'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
    elif options == "Листинг 10.2":
        st.write('Код листинга 10.2')
        path = 'pages/glava_10/start_app.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
    elif options == "Листинг 10.3":
        st.write('Код листинга 10.3')
        path = 'pages/glava_10/home_page.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
    elif options == "Листинг 10.4":
        st.write('Код листинга 10.4')
        path = 'pages/glava_10/catalog.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
    elif options == "Листинг 10.5":
        st.write('Код листинга 10.5')
        path = 'pages/glava_10/about.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
    elif options == "Листинг 10.6":
        st.write('Код листинга 10.6')
        path = 'pages/glava_10/address.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
    elif options == "Пример главы 10":
        st.write('Нажмите кнопку для запуска примера')
        st.write('Многостраничное приложение откроется в новой вкладке')
        st.page_link('https://appapp-kn3kvsilrgrfpjp9vzrdyx.streamlit.app/',
                     label='Пример главы 10')
        st.write('Многостраничное приложение откроется в новой вкладке')



