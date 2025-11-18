import streamlit as st

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 2", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

# Текст по центру страницы
st.header("👩🏻‍💻Листинги главы 2")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=300)

# Контейнер
with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги главы 2",
        ("Листинг 2.1", "Листинг 2.2", "Листинг 2.3", "Листинг 2.4",
         "Листинг 2.5", "Листинг 2.6", "Листинг 2.7", "Листинг 2.8"),
        index=None,
        placeholder="Выберите листинг..."
    )

# Контейнер
cont_2 = st.container()
with cont_2:
    if options is None:
        st.write('Листинг не выбран')
        st.image("Stream_Book.jpg", width=350)
    elif options == "Листинг 2.1":
        st.write('Код листинга 2.1')
        path = 'pages/glava_2/listing_2_1.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_2/listing_2_1.py', label='🚀Выполнить код')
    elif options == "Листинг 2.2":
        st.write('Код листинга 2.2')
        path = 'pages/glava_2/listing_2_2.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_2/listing_2_2.py', label='🚀Выполнить код')
    elif options == "Листинг 2.3":
        st.write('Код листинга 2.3')
        path = 'pages/glava_2/listing_2_3.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_2/listing_2_3.py', label='🚀Выполнить код')
    elif options == "Листинг 2.4":
        st.write('Код листинга 2.4')
        path = 'pages/glava_2/listing_2_4.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_2/listing_2_4.py', label='🚀Выполнить код')
    elif options == "Листинг 2.5":
        st.write('Код листинга 2.5')
        path = 'pages/glava_2/listing_2_5.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_2/listing_2_5.py', label='🚀Выполнить код')
    elif options == "Листинг 2.6":
        st.write('Код листинга 2.6')
        path = 'pages/glava_2/listing_2_6.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_2/listing_2_6.py', label='🚀Выполнить код')
    elif options == "Листинг 2.7":
        st.write('Код листинга 2.7')
        path = 'pages/glava_2/listing_2_7.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_2/listing_2_7.py', label='🚀Выполнить код')
    elif options == "Листинг 2.8":
        st.write('Код листинга 2.8')
        path = 'pages/glava_2/listing_2_8.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_2/listing_2_8.py', label='🚀Выполнить код')
