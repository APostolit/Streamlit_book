import streamlit as st

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 3", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

# Текст по центру страницы
st.header("👩🏻‍💻Листинги главы 3")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=300)

with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги главы 3",
        ("Листинг 3.1", "Листинг 3.2", "Листинг 3.3", "Листинг 3.4",
         "Листинг 3.5", "Листинг 3.6", "Листинг 3.7", "Листинг 3.8",
         "Листинг 3.9", "Листинг 3.10", "Листинг 3.11", "Листинг 3.12",
         "Листинг 3.13", "Листинг 3.14", "Листинг 3.15", "Листинг 3.16",
         "Листинг 3.17", "Листинг 3.18", "Листинг 3.19", "Листинг 3.20",
         "Листинг 3.21", "Листинг 3.22", "Листинг 3.23", "Листинг 3.24"
         ),
        index=None,
        placeholder="Выберите листинг..."
    )

# Контейнер
cont_2 = st.container()
with cont_2:
    if options is None:
        st.write('Листинг не выбран')
        st.image("Stream_Book.jpg", width=350)
    elif options == "Листинг 3.1":
        st.write('Код листинга 3.1')
        path = 'pages/glava_3/listing_3_1.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_3/listing_3_1.py', label='🚀Выполнить код')
    elif options == "Листинг 3.2":
        st.write('Код листинга 3.2')
        path = 'pages/glava_3/listing_3_2.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_3/listing_3_2.py', label='🚀Выполнить код')
    elif options == "Листинг 3.3":
        st.write('Код листинга 3.3')
        path = 'pages/glava_3/listing_3_3.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_3/listing_3_3.py', label='🚀Выполнить код')
    elif options == "Листинг 3.4":
        st.write('Код листинга 3.4')
        path = 'pages/glava_3/listing_3_4.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_3/listing_3_4.py', label='🚀Выполнить код')
    elif options == "Листинг 3.5":
        st.write('Код листинга 3.5')
        path = 'pages/glava_3/listing_3_5.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        # st.page_link('pages/glava_3/list_3_5.py', label='🚀Выполнить код')
    elif options == "Листинг 3.6":
        st.write('Код листинга 3.6')
        path = 'pages/glava_3/listing_3_6.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_3/listing_3_6.py', label='🚀Выполнить код')
    elif options == "Листинг 3.7":
        st.write('Код листинга 3.7')
        path = 'pages/glava_3/listing_3_7.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_3/listing_3_7.py', label='🚀Выполнить код')
    elif options == "Листинг 3.8":
        st.write('Код листинга 3.8')
        path = 'pages/glava_3/listing_3_8.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_3/listing_3_8.py', label='🚀Выполнить код')
    elif options == "Листинг 3.9":
        st.write('Код листинга 3.9')
        path = 'pages/glava_3/listing_3_9.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_3/listing_3_9.py', label='🚀Выполнить код')
    elif options == "Листинг 3.10":
        st.write('Код листинга 3.10')
        path = 'pages/glava_3/listing_3_10.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_3/listing_3_10.py', label='🚀Выполнить код')
    elif options == "Листинг 3.11":
        st.write('Код листинга 3.11')
        path = 'pages/glava_3/listing_3_11.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_3/listing_3_11.py', label='🚀Выполнить код')
    elif options == "Листинг 3.12":
        st.write('Код листинга 3.12')
        path = 'pages/glava_3/listing_3_21.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_3/listing_3_12.py', label='🚀Выполнить код')
    elif options == "Листинг 3.13":
        st.write('Код листинга 3.13')
        path = 'pages/glava_3/listing_3_13.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_3/listing_3_13.py', label='🚀Выполнить код')
    elif options == "Листинг 3.14":
        st.write('Код листинга 3.14')
        path = 'pages/glava_3/listing_3_14.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_3/listing_3_14.py', label='🚀Выполнить код')
    elif options == "Листинг 3.15":
        st.write('Код листинга 3.15')
        path = 'pages/glava_3/listing_3_15.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_3/listing_3_15.py', label='🚀Выполнить код')
    elif options == "Листинг 3.16":
        st.write('Код листинга 3.16')
        path = 'pages/glava_3/listing_3_16.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_3/listing_3_16.py', label='🚀Выполнить код')
    elif options == "Листинг 3.17":
        st.write('Код листинга 3.17')
        path = 'pages/glava_3/listing_3_17.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_3/listing_3_17.py', label='🚀Выполнить код')
    elif options == "Листинг 3.18":
        st.write('Код листинга 3.18')
        path = 'pages/glava_3/listing_3_18.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_3/listing_3_18.py', label='🚀Выполнить код')
    elif options == "Листинг 3.19":
        st.write('Код листинга 3.19')
        path = 'pages/glava_3/listing_3_19.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_3/listing_3_19.py', label='🚀Выполнить код')
    elif options == "Листинг 3.20":
        st.write('Код листинга 3.20')
        path = 'pages/glava_3/listing_3_20.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_3/listing_3_20.py', label='🚀Выполнить код')
    elif options == "Листинг 3.21":
        st.write('Код листинга 3.21')
        path = 'pages/glava_3/listing_3_21.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_3/listing_3_21.py', label='🚀Выполнить код')
    elif options == "Листинг 3.22":
        st.write('Код листинга 3.22')
        path = 'pages/glava_3/listing_3_22.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_3/listing_3_22.py', label='🚀Выполнить код')
    elif options == "Листинг 3.23":
        st.write('Код листинга 3.23')
        path = 'pages/glava_3/listing_3_23.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_3/listing_3_23.py', label='🚀Выполнить код')
    elif options == "Листинг 3.24":
        st.write('Код листинга 3.24')
        path = 'pages/glava_3/listing_3_24.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        st.page_link('pages/glava_3/listing_3_24.py', label='🚀Выполнить код')