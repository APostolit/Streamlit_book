import streamlit as st

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 5", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

# Текст по центру страницы
st.header("👩🏻‍💻Листинги главы 5")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=300)

with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги главы 5",
        ("Листинг 5.1", "Листинг 5.2", "Листинг 5.3", "Листинг 5.4",
         "Листинг 5.5", "Листинг 5.6", "Листинг 5.7", "Листинг 5.8",
         "Листинг 5.9", "Листинг 5.10", "Листинг 5.11", "Листинг 5.12",
         "Листинг 5.13", "Листинг 5.14", "Листинг 5.15", "Листинг 5.16"),
        index=None,
        placeholder="Выберите листинг..."
    )

# Контейнер
cont_2 = st.container()
with cont_2:
    if options is None:
        st.write('Листинг не выбран')
        st.image("Stream_Book.jpg", width=350)
    elif options == "Листинг 5.1":
        st.write('Код листинга 5.1')
        path = 'pages/glava_5/listing_5_1.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_5/listing_5_1.py', label='🚀Выполнить код')
    elif options == "Листинг 5.2":
        st.write('Код листинга 5.2')
        path = 'pages/glava_5/listing_5_2.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_5/listing_5_2.py', label='🚀Выполнить код')
    elif options == "Листинг 5.3":
        st.write('Код листинга 5.3')
        path = 'pages/glava_5/listing_5_3.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_5/listing_5_3.py', label='🚀Выполнить код')
    elif options == "Листинг 5.4":
        st.write('Код листинга 5.4')
        path = 'pages/glava_5/listing_5_4.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_5/listing_5_4.py', label='🚀Выполнить код')
    elif options == "Листинг 5.5":
        st.write('Код листинга 5.5')
        path = 'pages/glava_5/listing_5_5.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_5/listing_5_5.py', label='🚀Выполнить код')
    elif options == "Листинг 5.6":
        st.write('Код листинга 5.6')
        path = 'pages/glava_5/listing_5_6.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_5/listing_5_6.py', label='🚀Выполнить код')
    elif options == "Листинг 5.7":
        st.write('Код листинга 5.7')
        path = 'pages/glava_5/listing_5_7.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_5/listing_5_7.py', label='🚀Выполнить код')
    elif options == "Листинг 5.8":
        st.write('Код листинга 5.8')
        path = 'pages/glava_5/listing_5_8.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_5/listing_5_8.py', label='🚀Выполнить код')
    elif options == "Листинг 5.9":
        st.write('Код листинга 5.9')
        path = 'pages/glava_5/listing_5_9.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_5/listing_5_9.py', label='🚀Выполнить код')
    elif options == "Листинг 5.10":
        st.write('Код листинга 5.10')
        path = 'pages/glava_5/listing_5_10.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_5/listing_5_10.py', label='🚀Выполнить код')
    elif options == "Листинг 5.11":
        st.write('Код листинга 5.11')
        path = 'pages/glava_5/listing_5_11.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_5/listing_5_11.py', label='🚀Выполнить код')
    elif options == "Листинг 5.12":
        st.write('Код листинга 5.12')
        path = 'pages/glava_5/listing_5_12.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_5/listing_5_12.py', label='🚀Выполнить код')
    elif options == "Листинг 5.13":
        st.write('Код листинга 5.13')
        path = 'pages/glava_5/listing_5_13.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_5/listing_5_13.py', label='🚀Выполнить код')
    elif options == "Листинг 5.14":
        st.write('Код листинга 5.14')
        path = 'pages/glava_5/listing_5_14.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_5/listing_5_14.py', label='🚀Выполнить код')
    elif options == "Листинг 5.15":
        st.write('Код листинга 5.15')
        path = 'pages/glava_5/listing_5_15.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_5/listing_5_15.py', label='🚀Выполнить код')
    elif options == "Листинг 5.16":
        st.write('Код листинга 5.16')
        path = 'pages/glava_5/listing_5_16.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_5/listing_5_16.py', label='🚀Выполнить код')
