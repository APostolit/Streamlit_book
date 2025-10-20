import streamlit as st

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 3", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

# Текст по центру страницы
st.columns(3)[1].header("👩🏻‍💻Примеры главы 3")

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
    elif options == "Листинг 3.1":
        st.write('Код листинга 3.1 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st

            # Создание простой кнопки primary
            bt_1 = st.button("Привет", type="primary")
            if bt_1:
                st.write("Нажата кнопка 'Привет'")

            # Создание простой кнопки secondary
            bt_2 = st.button("Выход")
            if bt_2:
                st.write("Нажата кнопка 'Выход'")
            else:
                st.write("Приложение загружено")

            # Создание простой кнопки tertiary
            bt_3 = st.button("Текстовая кнопка", type="tertiary")
            if bt_3:
                st.write("Нажата текстовая кнопка")

            # Создание колонок
            left, middle, right = st.columns(3)
            # Создание кнопок в колонках
            if left.button("Простая кнопка", width="stretch"):
                left.markdown("Нажата простая кнопка")
            if middle.button("Кнопка с эмодзи", icon="😃", width="stretch"):
                middle.markdown("Нажата кнопка с эмодзи")
            if right.button("Кнопка с иконкой", icon=":material/mood:", width="stretch"):
                right.markdown("Нажата кнопка с иконкой")
    elif options == "Листинг 3.2":
        st.write('Код листинга 3.2 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st
            import pandas as pd


            # Функция формирования набора данных df
            @st.cache_data
            def get_data():
                data = {'Имя': ['Сергей', 'Михаил', 'Антон', 'Степан'],
                        'Возраст': [32, 28, 41, 37],
                        'Город': ['Москва', 'Казань', 'Сочи', 'Омск']}
                data = pd.DataFrame(data)
                return data


            # Функция конвертирования df в CSV (в памяти)
            @st.cache_data
            def convert_for_download(df):
                return df.to_csv().encode("utf-8")

            # Создание набора данных
            df = get_data()
            st.write('Набор данных, сформированный в программе')
            st.write(df)
            # конвертирования df в CSV
            csv = convert_for_download(df)

            # Кнопка загрузки данных из df
            st.download_button(
                label="Скачать DataFrame📈",
                data=csv,
                file_name="data.csv",
                mime="text/csv",
                icon=":material/download:",
            )

            st.write('Файл с изображением')
            st.image('static/AP_400.png')
            # Кнопка загрузки изображения
            with open("static/AP_400.png", "rb") as file:
                st.download_button(
                    label="Скачать изображение🌄",
                    data=file,
                    file_name="my_image.png",
                    mime="image/png",
                    icon=":material/download:"
                )

            st.write('Данные в CSV файле')
            data = spectra_df = pd.read_csv('passengers.csv')
            st.write(data)
            # Кнопка загрузки данных из df
            st.download_button(
                label="Скачать CSV файл⬇️",
                data=csv,
                file_name="passengers.csv",
                mime="text/csv",
                icon=":material/download:",
            )
    elif options == "Листинг 3.3":
        st.write('Код листинга 3.3 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st

            # Создать форму
            with st.form(key='my_form'):
                # Поля для ввода
                name = st.text_input(label='Имя')
                age = st.number_input(label='Возраст', min_value=0)
                submit_button = st.form_submit_button(label='Отправить')

            # Отображение результатов
            if submit_button:
                st.write(f'Ведено имя- {name}, введен возраст {age}')
    elif options == "Листинг 3.4":
        st.write('Код листинга 3.4 и результаты ее выполнения')
        with st.echo(code_location="above"):
            import streamlit as st

            st.write('Кнопка - ссылка')
            st.link_button("Открыть сайт 'Академия Python'",
                           "https://apython.ru")
    elif options == "Листинг 3.5":
        st.write('Код листинга 3.5 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st

            # Настройка параметров данной страницы
            st.set_page_config(
                page_title="Домашняя",  # Текст на вкладке браузера
                page_icon='👨',  # Иконка на вкладке браузера
                layout="wide",  # Использовать всю ширину страницы
                initial_sidebar_state="expanded",  # Раскрыть боковую панель
            )

            # Создать объект - страница
            pg_company = st.Page(page="pages/about.py", title="👨‍💼О компании")

            # Создать боковую панель
            sb = st.sidebar
            with sb:
                # Создать ссылки на страницы
                st.page_link("pages/glava_3/page1.py", label="Страница 1", icon="1️⃣")
                st.page_link(pg_company, label="О компании", icon="👷🏼")
                st.page_link("https://dzen.ru", label="Яндекс", icon="🌎")

        # Показать код страницы page1.py
        st.write('Код страницы page1.py')
        path_file = 'pages/glava_3/page1.py'
        file = open(path_file, 'r')
        code = file.read()
        st.code(body=code, language="python")

        # Показать код страницы about.py
        st.write('Код страницы about.py')
        path_file = 'pages/about.py'
        file = open(path_file, 'r')
        code = file.read()
        st.code(body=code, language="python")

    elif options == "Листинг 3.6":
        st.write('Код листинга 3.6 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st

            st.badge("Элемент st_checkbox")
            agree = st.checkbox("Печатать", value=False)
            finger = st.checkbox("Подтвердить согласие", value=False)

            if agree:
                st.write("Да, печатать")
            else:
                st.write("Нет, не печатать")

            if finger:
                st.write("Да, согласен")
            else:
                st.write("Нет, не согласен")
    elif options == "Листинг 3.7":
        st.write('Код листинга 3.7 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st

            st.badge("Элемент st_color_picker")
            color = st.color_picker("Выберите цвет", "#00f900")
            st.write("Выбран цвет -", color)
    elif options == "Листинг 3.8":
        st.write('Код листинга 3.8 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st

            st.text("Элементы st.feedback")
            # Палец
            st.badge("Палец")
            sent_1 = [":material/thumb_down:", ":material/thumb_up:"]
            selected_1 = st.feedback("thumbs")
            if selected_1 is not None:
                st.markdown(f"Ваш выбор: {sent_1[selected_1]}")
            st.divider()  # Разделитель

            # Звезды
            st.badge("Звезды")
            sent_2 = ["1", "2", "3", "4", "5"]
            selected_2 = st.feedback("stars")
            if selected_2 is not None:
                st.markdown(f"Количество выбранных звезд {sent_2[selected_2]}")
            st.divider()  # Разделитель

            # Лица
            st.badge("Лица")
            sent_3 = ["1", "2", "3", "4", "5"]
            selected_3 = st.feedback("faces")
            if selected_3 is not None:
                st.markdown(f"Оценка пользователя {sent_3[selected_3]}")
            st.divider()  # Разделитель
    elif options == "Листинг 3.9":
        st.write('Код листинга 3.9 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st

            st.badge("Элемент st_multiselect")

            st.divider()  # Разделитель
            options = st.multiselect(
                "Подбор овощей для салата",
                ["Огурцы", "Помидоры", "Лук", "Морковь", "Капуста"],
                help="Выберите овощи в любом сочетании",
                placeholder='Набор овощей для салата'
            )
            st.divider()  # Разделитель
            if options:
                st.write("Сделан выбор:", options)
            st.divider()  # Разделитель
    elif options == "Листинг 3.10":
        st.write('Код листинга 3.10 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st

            st.text("Элементы st.pills")

            st.divider()  # Разделитель
            st.badge("Множественный выбор")
            options = ["Яблоки", "Груши", "Апельсины", "Мандарины"]
            select_1 = st.pills("Фрукты ", options, selection_mode="multi")
            if select_1:
                st.markdown(f"Вы выбрали: {select_1}.")
            st.divider()  # Разделитель

            st.badge("Простой выбор")
            option_map = {
                1: ":material/add:",
                2: ":material/zoom_in:",
                3: ":material/zoom_out:",
                4: ":material/zoom_out_map:",
            }
            select_2 = st.pills(
                "Инструменты масштабирования",
                options=option_map.keys(),
                format_func=lambda option: option_map[option],
                selection_mode="single",
            )
            if select_2:
                st.write(
                    "Ваш выбор: "
                    f"{None if select_2 is None else option_map[select_2]}"
                )
            st.divider()  # Разделитель
    elif options == "Листинг 3.11":
        st.write('Код листинга 3.11 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st

            st.badge("Радио кнопки")
            genre = st.radio(
                label="Выберите категорию фильма",
                options=[":rainbow[Комедия]", "***Детектив***", "Историческое кино :movie_camera:"],
                index=0,
                captions=[
                    "Отдохнуть и повеселится.",
                    "Провести расследование.",
                    "Окунуться в историю",
                ],
            )

            if genre == ":rainbow[Комедия]":
                st.write("Вы выбрали комедию")
            elif genre == "***Детектив***":
                st.write("Вы выбрали детектив")
            elif genre == "Историческое кино :movie_camera:":
                st.write("Вы выбрали Историческое кино")
            else:
                st.write("Жанр не выбран")

            st.divider()  # Разделитель

            st.badge("Флажки и радиокнопки")
            # Начальное значение виджетов в текущем сеансе
            if "visibility" not in st.session_state:
                st.session_state.visibility = "visible"
                st.session_state.disabled = False
                st.session_state.horizontal = False

            # Разбивка страницы на колонки
            col1, col2 = st.columns(2)

            # Левая колонка с флажками
            with col1:
                st.checkbox("Блокировать радиокнопки", key="disabled")
                st.checkbox("Радиокнопки в линию", key="horizontal")

            # Правая колонка с радио кнопами
            with col2:
                st.radio(
                    label="Сделать метку видимой 👇",
                    options=["visible", "hidden"],
                    key="visibility",
                    label_visibility=st.session_state.visibility,
                    disabled=st.session_state.disabled,
                    horizontal=st.session_state.horizontal,
                )
    elif options == "Листинг 3.12":
        st.write('Код листинга 3.12 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st

            st.text("Элементы st_segmented_control")

            st.divider()  # Разделитель
            st.badge("Множественный выбор")
            options = ["Север", "Восток", "Юг", "Запад"]
            select_1 = st.segmented_control(
                "Направление", options, selection_mode="multi"
            )
            if select_1:
                st.markdown(f"Выбрано: {select_1}.")

            st.divider()  # Разделитель

            st.badge("Выбор одного элемента")
            option_map = {
                0: ":material/add:",
                1: ":material/zoom_in:",
                2: ":material/zoom_out:",
                3: ":material/zoom_out_map:",
            }
            select_2 = st.segmented_control(
                "Инструменты масштабирования",
                options=option_map.keys(),
                format_func=lambda option: option_map[option],
                selection_mode="single",
            )

            st.write(
                "Выбрано: "
                f"{None if select_2 is None else option_map[select_2]}"
            )
    elif options == "Листинг 3.13":
        st.write('Код листинга 3.13 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st

            st.badge("Виджет st.selectbox с начальным значением элемента выбора")
            option = st.selectbox(
                "Выберите способ связи",
                ("E-mail", "Стационарный телефон", "Мобильный телефон"),
            )
            if option:
                st.write("Сделан выбор-", option)
            st.divider()  # Горизонтальная линия

            st.badge("Виджет st.selectbox без начального значения элемента выбора")
            option = st.selectbox(
                "Выберите способ связи",
                ("E-mail", "Стационарный телефон", "Мобильный телефон"),
                index=None,
                placeholder="Выберите способ связи..."
            )
            if option:
                st.write("Сделан выбор-", option)
            st.divider()  # Горизонтальная линия

            st.badge("Виджет st.selectbox с возможностью ввода элемента выбора")
            option = st.selectbox(
                "Электронная почта",
                ["victor@mail.ru", "oleg@mail.ru", "maxim@mail.ru"],
                index=None,
                placeholder="Выберите или введите e-mail",
                accept_new_options=True,
            )
            st.write("Сделан выбор-", option)
            st.divider()  # Горизонтальная линия

            # Инициализация значений виджетов в состоянии сессии
            if "visibility" not in st.session_state:
                st.session_state.visibility = "visible"
                st.session_state.disabled = False

            st.badge("Управление состоянием виджет st.selectbox")
            # Создание контейнера
            cont = st.container(border=True)

            # Создание колонок в контейнере
            with cont:
                col1, col2 = st.columns(2)

            with col1:
                st.checkbox("Сделать виджет недоступным", key="disabled")
                radio = st.radio(
                    "Изменить видимость метки 👉",
                    options=["Показать", "Скрыть", "Свернуть"],
                )
                if radio:
                    if radio == "Скрыть":
                        st.session_state.visibility = "hidden"
                    elif radio == "Показать":
                        st.session_state.visibility = "visible"
                    elif radio == "Свернуть":
                        st.session_state.visibility = "collapsed"

            with col2:
                option1 = st.selectbox(
                    "Выберите способ связи",
                    ("Email", "Домашний", "Мобильный"),
                    label_visibility=st.session_state.visibility,
                    disabled=st.session_state.disabled,
                )
    elif options == "Листинг 3.14":
        st.write('Код листинга 3.14 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st

            st.text("Элементы st.select_slider")

            st.badge("Выбор одного значения")
            c = st.select_slider(
                "Выберите страну",
                options=["Россия", "Китай", "США", "Великобритания",
                         "Франция", "Германия", "Италия", ], )
            st.write("Выбрана страна:", c)

            st.divider()  # Разделитель

            st.badge("Выбор двух значений")
            start_color, end_color = st.select_slider(
                "Выберите диапазон цветов",
                options=["red", "orange", "yellow", "green",
                         "blue", "indigo", "violet", ],
                value=("red", "blue"),
            )
            st.write("Выбраны цвета:", start_color, "и", end_color)
    elif options == "Листинг 3.15":
        st.write('Код листинга 3.15 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st

            st.text("Элементы st.toggle")

            tog_1 = st.toggle("Открыть доступ")
            if tog_1:
                st.write("Состояние переключателя", tog_1)

            toggle_value = st.toggle("Состояние переключателя", value=False)
            # Отобразить сообщение на основе состояния переключателя
            if toggle_value:
                st.write("Переключатель включен -", toggle_value)
            else:
                st.write("Переключатель выключен -", toggle_value)
    elif options == "Листинг 3.16":
        st.write('Код листинга 3.16 и результаты ее выполнения')
        with st.echo(code_location="above"):
            import streamlit as st

            # Заголовок страницы
            st.text('Виджеты для ввода чисел st.number_input')

            # Поле для ввода чисел
            number = st.number_input("Введите число с плавающей точкой",
                                     )
            if number:
                st.write("Введено число ", number)
            st.divider()  # Разделитель

            # Поле для ввода чисел
            int_number = st.number_input("Введите целое число",
                                         value=0)
            if int_number:
                st.write("Введено число ", int_number)
    elif options == "Листинг 3.17":
        st.write('Код листинга 3.17 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st
            from datetime import time
            from datetime import datetime

            # Заголовок страницы
            st.text('Виджет для ввода данных st.slider')

            # Слайдер для выбора числа
            age = st.slider(label="Сколько вам лет?",
                            min_value=0,
                            max_value=120,
                            value=25)
            st.write("Мой возраст- ", age)
            st.divider()  # Горизонтальная линия

            # Слайдер для выбора диапазона чисел
            values = st.slider(label="Выберите диапазон чисел",
                               min_value=0.0,
                               max_value=100.0,
                               value=(25.0, 75.0))
            st.write("Выбран диапазон:", values)
            st.divider()  # Горизонтальная линия

            # Слайдер для выбора диапазона времени
            appointment = st.slider(label="Запишитесь на прием:",
                                    value=(time(11, 30), time(12, 45)),
                                    format="hh:mm"
                                    )
            st.write("Ваше время приема:", appointment)
            st.divider()  # Горизонтальная линия

            # Слайдер для выбора даты и времени
            start_time = st.slider(label="Когда нужно выехать в аэропорт",
                                   value=datetime(2025, 1, 1, 9, 30),
                                   format="MM/DD/YY - hh:mm",
                                   )
            st.write("Дата и время выезда:", start_time)
            st.divider()  # Горизонтальная линия
    elif options == "Листинг 3.18":
        st.write('Код листинга 3.18 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st
            from datetime import datetime

            # Заголовок страницы
            st.text('Виджеты для ввода даты st.date_input')

            # Поле для ввода даты
            d = st.date_input(label="Дата вашего рождения?",
                              value=datetime(2019, 7, 6),
                              format='DD/MM/YYYY')
            st.write("Вы родились:", d)
            st.divider()  # Горизонтальная линия

            # Текущая дата
            today = datetime.now()
            # следующий год
            next_year = today.year + 1
            # 1 января следующего года
            jan_1 = datetime(next_year, 1, 1)
            # 31 декабря января следующего года
            dec_31 = datetime(next_year, 12, 31)
            # Поле для ввода интервала дат
            d1 = st.date_input(label="Выберите дату поездки в отпуск",
                               value=(jan_1, datetime(next_year, 1, 14)),
                               min_value=jan_1,
                               max_value=dec_31,
                               format="MM.DD.YYYY", )
            st.write("Выбран интервал дат:", d1)
    elif options == "Листинг 3.19":
        st.write('Код листинга 3.19 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st

            # Заголовок страницы
            st.text('Виджеты для ввода времени st.time_input')

            # Поле для ввода времени с шагом 15 мин
            t = st.time_input(label="Назначить время встречи",
                              value='now')
            st.write("Время встречи:", t)

            # Поле для ввода времени с шагом 1 мин
            t1 = st.time_input("Установить время будильник",
                               value=None,
                               step=60)
            st.write("Будильник установлен на время:", t1)
    elif options == "Листинг 3.20":
        st.write('Код листинга 3.20 и результаты ее выполнения')
        with st.echo(code_location="above"):
            import streamlit as st

            # Заголовок страницы
            st.text('Виджеты для ввода многострочного текста st.text_area')

            # Поле ввода многострочного текста
            txt_ar = st.text_area(label="Введите текст")
            if txt_ar:
                st.write("Введен следующий текст:", txt_ar)
    elif options == "Листинг 3.21":
        st.write('Код листинга 3.21 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st

            # Заголовок страницы
            st.text('Виджеты для ввода текста st.text_input')

            # Поле ввода однострочного текста
            txt = st.text_input(label="Поле для вода однострочного текста")
            if txt:
                st.write("Введен следующий текст:", txt)
    elif options == "Листинг 3.22":
        st.write('Код листинга 3.22 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st
            import pandas as pd
            from io import StringIO

            uploaded_img = st.file_uploader("Загрузить изображение",
                                            type=['png', 'jpeg'])
            if uploaded_img is not None:
                file_details = {"Имя файла - ": uploaded_img.name,
                                "Тип файла - ": uploaded_img.type,
                                "Размер - ": uploaded_img.size}
                st.write(file_details)

            uploaded_file = st.file_uploader("Загрузка CSV файлов",
                                             type='csv')
            if uploaded_file is not None:
                # Преобразовать в строку с кодировкой utf-8
                stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
                st.write(stringio)

                # Использовать как "файловый" объект
                dataframe = pd.read_csv(uploaded_file)
                st.write(dataframe)
    elif options == "Листинг 3.23":
        st.write('Код листинга 3.23 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st

            st.text("Виджет для записи аудио данных с микрофона")
            st.write("Нажмите кнопку, чтобы начать запись, а затем остановите ее")

            audio = st.audio_input("Виджет для звукозаписи",
                                   help='Нажмите на значок микрофона для начала записи. '
                                        'Для остановки записи нажмите на значок еще раз')
            if audio:
                with open("audio.wav", "wb") as f:
                    f.write(audio.getbuffer())
                    st.write("Аудио запись успешно сохранена!")
    elif options == "Листинг 3.24":
        st.write('Код листинга 3.24 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st

            enable = st.checkbox("Активировать камеру")
            video = st.camera_input("Получите видео поток", disabled=not enable)

            if video:
                st.image(video)
