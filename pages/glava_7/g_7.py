import streamlit as st

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 7", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

# Текст по центру страницы
st.columns(3)[1].header("👩🏻‍💻Примеры главы 7")

# Контейнер
cont_1 = st.container(width=300)
with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги главы 7",
        ("Листинг 7.1", "Листинг 7.2", "Листинг 7.3", "Листинг 7.4",
         "Листинг 7.5", "Листинг 7.6", "Листинг 7.7", "Листинг 7.8",
         "Листинг 7.9", "Листинг 7.10", "Листинг 7.11", "Листинг 7.12",
         "Листинг 7.13", "Листинг 7.14","Листинг 7.15", "Листинг 7.16"),
        index=None,
        placeholder="Выберите листинг..."
    )

# Контейнер
cont_2 = st.container()
with cont_2:
    if options is None:
        st.write('Листинг не выбран')
    elif options == "Листинг 7.1":
        st.write('Код листинга 7.1')
        path = 'pages/glava_7/start_app_1.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
    elif options == "Листинг 7.2":
        st.write('Код листинга 7.2')
        path = 'pages/glava_7/page1.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
    elif options == "Листинг 7.3":
        st.write('Код листинга 7.3')
        path = 'pages/glava_7/start_app_2.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
    elif options == "Листинг 7.4":
        st.write('Код листинга 7.4')
        path = 'pages/glava_7/start_app_3.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
    elif options == "Листинг 7.5":
        st.write('Код листинга 7.5')
        path = 'pages/glava_7/cr_acc.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
    elif options == "Листинг 7.6":
        st.write('Код листинга 7.6')
        path = 'pages/glava_7/manage_acc.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
    elif options == "Листинг 7.7":
        st.write('Код листинга 7.7')
        path = 'pages/glava_7/info.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
    elif options == "Листинг 7.8":
        st.write('Код листинга 7.8')
        path = 'pages/glava_7/address.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
    elif options == "Листинг 7.9":
        st.write('Код листинга 7.9')
        path = 'pages/glava_7/start_app_4.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
    elif options == "Листинг 7.10":
        st.write('Код листинга 7.10')
        path = 'pages/glava_7/start_app_5.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
    elif options == "Листинг 7.11":
        st.write('Код листинга 7.11')
        path = 'pages/glava_7/start_app_6.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
    elif options == "Листинг 7.12":
        st.write('Код листинга 7.12')
        path = 'pages/glava_7/start_app_7.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
    elif options == "Листинг 7.13":
        st.write('Код листинга 7.13 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st
            import pandas as pd

            @st.cache_data  # caching декоратор
            def load_data(url):
                data = pd.read_csv(url)
                return data

            # Вызов функции загрузки данных
            df = load_data("https://github.com/plotly/datasets/raw/master/uber-rides-data1.csv")
            # Отображение данных
            st.dataframe(df)

            # Кнопка перезагрузки приложения
            st.button("Обновить")
    elif options == "Листинг 7.14":
        st.write('Код листинга 7.14')
        path = 'pages/glava_7/st_cache_resourse.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
    elif options == "Листинг 7.15":
        st.write('Код листинга 7.15 и результаты ее выполнения')
        with st.echo(code_location="above"):
            import streamlit as st

            st.title('Приложение - счетчик')
            count = 0

            bt_increment = st.button('Увеличить счетчик')
            if bt_increment:
                count += 1

            st.write('Показание счетчика = ', count)
    elif options == "Листинг 7.16":
        st.write('Код листинга 7.16 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st

            st.title('Приложение - счетчик')

            if 'aaa' not in st.session_state:
                st.session_state.aaa = 0

            # Обнуление счетчика
            if 'count' not in st.session_state:
                st.session_state.count = 0

            bt_increment = st.button('Увеличить счетчик')
            # Увеличить счетчик
            if bt_increment:
                st.session_state.count += 1
                st.session_state.aaa += 2

            st.write('Показание счетчика = ', st.session_state.count)
            st.write('Показание счетчика = ', st.session_state.aaa)
