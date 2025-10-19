import streamlit as st

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 1", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

# Текст по центру страницы
st.columns(3)[1].header("👩🏻‍💻Примеры главы 1")

# Контейнер
cont_1 = st.container(width=300)
with cont_1:
    # Раскрывающийся список
    options = st.selectbox(
        "Листинги главы 1",
        ("Листинг 1.1", ),
        index=None,
        placeholder="Выберите листинг..."
    )

# Элемент st.code - загрузить код листинга
# path_file = 'pages/glava_1/first_app.py'
# file = open(path_file, 'r')
# code = file.read()

# Контейнер
cont_2 = st.container()
with cont_2:
    if options is None:
        st.write('Листинг не выбран')
    else:
        st.write('Листинг 1.1 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st
            st.title('Первое приложение на Streamlit')
