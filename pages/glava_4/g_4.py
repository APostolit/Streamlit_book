import streamlit as st

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 4", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

# Текст по центру страницы
st.columns(3)[1].header("👩🏻‍💻Примеры главы 4")

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
    elif options == "Листинг 4.1":
        st.write('Код листинга 4.1 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st

            st.text('Элемент аудио проигрыватель st.audio')
            st.audio("gaiti.mp3",
                     format="audio/mpeg",
                     loop=False)
    elif options == "Листинг 4.2":
        st.write('Код листинга 4.2 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st

            st.text("Контейнер для вывода изображения")
            st.image("AP_400.png",
                     caption="Академия Python")
    elif options == "Листинг 4.3":
        st.write('Код листинга 4.3 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st

            with st.sidebar:
                st.text('Логотип, элемент st.logo')
                st.logo(image='favicon.ico',
                        link='https://apython.ru')
    elif options == "Листинг 4.4":
        st.write('Код листинга 4.4 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st

            # Скрыть боковую панель
            st.set_page_config(initial_sidebar_state="collapsed")

            st.markdown("## Элемент для вывода pdf файлов st.pdf")

            # Показать локальный pdf- файл
            st.pdf("pdf/Python_vsem.pdf", height=400)

            #  Показать загруженный pdf- файл
            uploaded_file = st.file_uploader("Выберите PDF файл", type="pdf")
            if uploaded_file is not None:
                st.pdf(uploaded_file)
    elif options == "Листинг 4.5":
        st.write('Код листинга 4.5 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st

            st.text('Элемент st.video')
            st.video("Pingvin.mp4", format='mp4')
