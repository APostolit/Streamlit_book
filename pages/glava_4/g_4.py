import streamlit as st

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 4", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

# Текст по центру страницы
st.header("👩🏻‍💻Листинги главы 4")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=300)

with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги главы 4",
        ("Листинг 4.1", "Листинг 4.2", "Листинг 4.3", "Листинг 4.4",
         "Листинг 4.5"),
        index=None,
        placeholder="Выберите листинг..."
    )

# Контейнер
cont_2 = st.container()
with cont_2:
    if options is None:
        st.write('Листинг не выбран')
        st.image("Stream_Book.jpg", width=350)
    elif options == "Листинг 4.1":
        st.write('Код листинга 4.1')
        path = 'pages/glava_4/listing_4_1.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_4/listing_4_1.py', label='🚀Выполнить код')
    elif options == "Листинг 4.2":
        st.write('Код листинга 4.2')
        path = 'pages/glava_4/listing_4_2.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_4/listing_4_2.py', label='🚀Выполнить код')
    elif options == "Листинг 4.3":
        st.write('Код листинга 4.3')
        path = 'pages/glava_4/listing_4_3.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_4/listing_4_3.py', label='🚀Выполнить код')
    elif options == "Листинг 4.4":
        st.write('Код листинга 4.4')
        path = 'pages/glava_4/listing_4_4.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_4/listing_4_4.py', label='🚀Выполнить код')
    elif options == "Листинг 4.5":
        st.write('Код листинга 4.5')
        path = 'pages/glava_4/listing_4_5.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_4/listing_4_5.py', label='🚀Выполнить код')
