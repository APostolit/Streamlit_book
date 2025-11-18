import streamlit as st

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 10", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

# Текст по центру страницы
st.header("👩🏻‍💻Листинги главы 11")

# Контейнер
cont_1 = st.container(width=300)
with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги главы 11",
        ("Листинг 11.1", "Листинг 11.2", "Листинг 11.3", "Листинг 11.4",
         "Листинг 11.5", "Листинг 11.6", "Листинг 11.7", "Листинг 11.8",
         "Листинг 11.9", "Листинг 11.10", "Листинг 11.11",
         "Пример главы 11"),
        index=None,
        placeholder="Выберите листинг..."
    )

# Контейнер
cont_2 = st.container()
with cont_2:
    if options is None:
        st.write('Листинг не выбран')
        st.image("Stream_Book.jpg", width=350)
    elif options == "Листинг 11.1":
        st.write('Код листинга 11.1')
        path = 'pages/glava_11/Class_SQL.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
    elif options == "Листинг 11.2":
        st.write('Код листинга 11.2')
        code = '''
        [connections]
        url = "my-test.db"file.read()
        '''
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
    elif options == "Листинг 11.3":
        st.write('Код листинга 11.3')
        path = 'pages/glava_11/sqlite.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
    elif options == "Листинг 11.4":
        st.write('Код листинга 11.4')
        code = '''
        [client]
        showSidebarNavigation = false

        [theme]
        primaryColor="#6eb52f"
        backgroundColor="#f0f0f5"
        secondaryBackgroundColor="#e0e0ef"
        textColor="#262730"
        font="sans serif"
        '''
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
    elif options == "Листинг 11.5":
        st.write('Код листинга 11.5')
        code = '''
        [connections]
        url_login = "data.db"
        '''
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
    elif options == "Листинг 11.6":
        st.write('Код листинга 11.6')
        path = 'pages/glava_11/login_app.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
    elif options == "Листинг 11.7":
        st.write('Код листинга 11.7')
        path = 'pages/glava_11/home_reg.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
    elif options == "Листинг 11.8":
        st.write('Код листинга 11.8')
        path = 'pages/glava_11/user_reg.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
    elif options == "Листинг 11.9":
        st.write('Код листинга 11.9')
        path = 'pages/glava_11/user_login.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
    elif options == "Листинг 11.10":
        st.write('Код листинга 11.10')
        path = 'pages/glava_11/user_logaut.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
    elif options == "Листинг 11.11":
        st.write('Код листинга 11.11')
        path = 'pages/glava_11/cabinet.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
    elif options == "Пример главы 11":
        st.page_link("https://app11-jauzeeacnac2tp6skqhsfs.streamlit.app/", label="Выполнить", icon="🚀")