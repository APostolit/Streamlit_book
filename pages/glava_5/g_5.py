import streamlit as st

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 5", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

# Текст по центру страницы
st.columns(3)[1].header("👩🏻‍💻Примеры главы 5")

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
    elif options == "Листинг 5.1":
        st.write('Код листинга 5.1 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st
            from numpy.random import default_rng as rng

            # Три объекта - колонки
            col1, col2, col3 = st.columns(3)

            # Содержание 1-й колонки
            with col1:
                st.header("Кошка")
                st.image("https://static.streamlit.io/examples/cat.jpg")

            # Содержание 2-й колонки
            with col2:
                st.header("Собака")
                st.image("https://static.streamlit.io/examples/dog.jpg")

            # Содержание 3-й колонки
            with col3:
                st.header("Сова")
                st.image("https://static.streamlit.io/examples/owl.jpg")

            # Набор данных DataFrame
            df = rng(0).standard_normal((5, 1))
            # Две колонки с указанием ширины
            col1, col2 = st.columns([3, 1], border=True)

            # Вставить график в 1-ю колонку
            col1.subheader("Широкая колонка с графиком")
            col1.line_chart(df)

            # Вставить данные во 1-ю колонку
            col2.subheader("Узкая колонка с данными")
            col2.write(df)
    elif options == "Листинг 5.2":
        st.write('Код листинга 5.2 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st
            import numpy as np

            st.text('Элементы st.container')

            # Контейнер 1
            ct_1 = st.container(border=True)
            with ct_1:
                st.write("Этот график находится внутри контейнера - ct-1")
                st.bar_chart(np.random.randn(20, 3))
            st.write("Этот текст за пределами контейнера")

            # Контейнер 2
            ct_2 = st.container(border=True)
            ct_2.write("Этот текст внутри контейнера ct-2")
            ct_2.write("Этот текст тоже внутри контейнера ct-2")

            # Группа контейнеров
            st.write("Группа контейнеров с иконками")
            row1 = st.columns(3)
            row2 = st.columns(3)
            for col in row1 + row2:
                tile = col.container(height=120)
                tile.title(":balloon:")

            # Контейнер с вертикальной прокруткой
            st.write("Контейнер с вертикальной прокруткой")
            long_text = "Это текст. " * 100
            with st.container(height=200):
                st.markdown(long_text)

            # Контейнер с кнопками
            st.write("Контейнер ct-3 с кнопками")
            ct_3 = st.container(border=True,
                                horizontal=True,
                                horizontal_alignment="right")
            for i in range(3):
                ct_3.button(f"Кнопка {i + 1}")
    elif options == "Листинг 5.3":
        st.write('Код листинга 5.3 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st

            st.text('Элемент st.dialog')


            # функция - диалог
            @st.dialog("Диалог - выбор цвета")
            # Обработка ответа пользователя
            def vote(item):
                st.write(f"Почему вы выбрали {item}?")
                reason = st.text_input("Потому, что...")
                if st.button("Ответить"):
                    st.session_state.vote = {"item": item, "reason": reason}
                    st.rerun()


            # Формирование вопроса к пользователю
            if "vote" not in st.session_state:
                st.write("Какой цвет вам нравится больше всего?")
                if st.button("Красный"):
                    vote("Красный")
                if st.button("Синий"):
                    vote("Синий")
            else:
                st.text(f"Вы выбрали {st.session_state.vote['item']} потому, "
                        f"что {st.session_state.vote['reason']}")
    elif options == "Листинг 5.4":
        st.write('Код листинга 5.4 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st
            import time

            st.text('Таймер с элементом st.empty')
            with st.empty():
                for seconds in range(10):
                    st.write(f"⏳ Прошло {seconds} секунд")
                    time.sleep(1)
                st.write(":material/check: Прошло 10 секунд!")

            bt = st.button("Перезапустить таймер")
            if bt:
                st.empty()
    elif options == "Листинг 5.5":
        st.write('Код листинга 5.5 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st
            import time

            st.text('Функция st.empty с элементом container')

            # Кнопка перезапуска приложения
            st.button("Перезапустить")

            # Создание пустой области страницы
            placeholder = st.empty()

            # Вывод в пустую область текста
            placeholder.markdown("Старт работы программы")
            time.sleep(3)

            # Вывод в пустую область индикатора состояния
            placeholder.progress(0, "Ждите, идет процесс ...")
            time.sleep(2)
            placeholder.progress(50, "Ждите, идет процесс ...")
            time.sleep(2)
            placeholder.progress(100, "Ждите, идет процесс ...")
            time.sleep(2)

            # Создание в пустой области контейнера
            with placeholder.container():
                st.line_chart({"data": [1, 5, 2, 6]})
                time.sleep(1)
                st.markdown("3...")
                time.sleep(1)
                st.markdown("2...")
                time.sleep(1)
                st.markdown("1...")
                time.sleep(1)
                # Вывод в пустую область текста
                st.markdown("Заполнение пустой области завершено!")
                time.sleep(5)

            # Очистка пустой области
            placeholder.empty()
    elif options == "Листинг 5.6":
        st.write('Код листинга 5.6 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st

            st.text('Элемент st.expander')

            with st.expander("График Pandas"):
                st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

            with st.expander("Открыть изображение st.expander"):
                st.write('''
                   Академия Python. Цифровые интерактивные книги, учебники
                    и учебные пособия.
                ''')
                st.image("AP_400.png")

            expander = st.expander("Показать изображение по URL")
            expander.write('Это изображение загружено из сети интернет')
            expander.image("https://static.streamlit.io/examples/dice.jpg")
    elif options == "Листинг 5.7":
        st.write('Код листинга 5.7 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st

            st.text('Элемент st.forma')

            with st.form("my_form"):
                # Элементы формы
                st.write("Текст в пределах формы")
                slider_val = st.slider("Выберите значение слайдера")
                checkbox_val = st.checkbox("Переключатель")
                # Кнопка
                submitted = st.form_submit_button("Отправить")

            st.write("Текст за пределами формы")
            # Обработчик события нажатия кнопки "Отправить"
            if submitted:
                st.write("Значение слайдера:", slider_val,
                         "Состояние переключателя", checkbox_val)
    elif options == "Листинг 5.8":
        st.write('Код листинга 5.8 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st

            st.text('Элемент st.popover')

            # Включение элементов в контейнер через with
            pop = st.popover("Электронный адрес")
            with pop:
                st.markdown("Добрый день 👋")
                email = st.text_input("Введите ваш электронный адрес")

            st.write("Ваша почта:", email)

            # Включение элементов в контейнер через метод объекта
            popover = st.popover("Фильтр цветов шрифта")
            red = popover.checkbox("Включить красный цвет", False)
            blue = popover.checkbox("Включить синий цвет", False)

            if red:
                st.write(":red[Доступен красный цвет.]")
            if blue:
                st.write(":blue[Доступен синий цвет.]")

            # Включение элементов в контейнер через with
            with st.popover("Показать график Pandas", width="stretch"):
                st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})
    elif options == "Листинг 5.9":
        st.write('Код листинга 5.9 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st

            st.sidebar.text('Элемент st.sidebar')

            # Добавление элементов через метод
            add_selectbox = st.sidebar.selectbox(
                "Как поддерживать обратную связь?",
                ("По Email", "По телефону", "По мобильному тел.")
            )

            # Добавление элементов через with
            with st.sidebar:
                add_radio = st.radio(
                    "Выберите способ доставки",
                    ("Стандартная (5-15 дней)", "Быстрая (2-3 дня)")
                )
    elif options == "Листинг 5.10":
        st.write('Код листинга 5.10 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st
            from numpy.random import default_rng as rng

            st.text('Элемент st.tabs')

            st.text('Изображения')
            tab1, tab2, tab3, tab4 = st.tabs(["Кошка", "Собака", "Сова", "Python"])
            # Вкладки созданные с использованием with
            with tab1:
                st.header("Кошка")
                st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
            with tab2:
                st.header("Собака")
                st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
            with tab3:
                st.header("Сова")
                st.image("https://static.streamlit.io/examples/owl.jpg", width=300)
            with tab4:
                st.header("Академия Python")
                st.image("AP_400.png", width=300)

            st.text('Данные Pandas')
            df = rng(0).standard_normal((5, 1))

            tab5, tab6 = st.tabs(["📈 График", "🗃 Данные"], width=400)
            # Вкладки созданные с использованием метода объектов
            tab5.subheader("Вкладка с графиком")
            tab5.line_chart(df)

            tab6.subheader("Вкладка с данными")
            tab6.write(df)
    elif options == "Листинг 5.11":
        st.write('Код листинга 5.11 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st

            prompt = st.chat_input("Введите сообщение")
            if prompt:
                st.write(f"Пользователь отправил следующее сообщение: {prompt}")
    elif options == "Листинг 5.12":
        st.write('Код листинга 5.12 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st
            import numpy as np

            # Отправка сообщения из st.chat_message программы
            with st.chat_message("user"):
                st.write("Вывод графика в блоке with 👋")
                st.line_chart(np.random.randn(20, 3))

            # Отправка сообщения из программы
            message = st.chat_message("assistant")
            message.write("Вывод график с использованием метода объекта")
            message.bar_chart(np.random.randn(20, 3))

            # Отправка сообщения от пользователя
            with st.sidebar:
                st.text('Элемент st.chat_message')
                messages = st.container(height=300)
                if prompt := st.chat_input("Введите сообщение"):
                    messages.chat_message("user").write(f"Введено: {prompt}")
                    messages.chat_message("assistant").write(f"Отправлено: {prompt}")
    elif options == "Листинг 5.13":
        st.write('Код листинга 5.13 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st
            import time

            # Скрыть боковую панель
            st.set_page_config(initial_sidebar_state="collapsed")


            # Функция - фрагмент приложения
            @st.fragment
            def start_balloons():
                # Кнопка выпуска воздушных шаров
                st.button("Выпустить воздушные шары",
                          help="Перезапуск фрагмента")
                st.balloons()


            # Процесс надувания воздушных шаров
            with st.spinner("Ждите...! Идет процесс надувания воздушных шаров."):
                time.sleep(5)

            # Вызов функции выпуска воздушных шаров
            start_balloons()

            # Кнопка перезапуска всего приложения
            st.button("Надуть воздушные шары и выпустить",
                      help="Перезапуск приложения")
    elif options == "Листинг 5.14":
        st.write('Код листинга 5.14 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st

            # Скрыть боковую панель
            st.set_page_config(initial_sidebar_state="collapsed")

            # Задать значения счетчикам при первом запуске приложения
            if "app_runs" not in st.session_state:
                st.session_state.app_runs = 0
                st.session_state.fragment_runs = 0


            # Функция с фрагментом приложения
            @st.fragment
            def my_fragment():
                st.session_state.fragment_runs += 1
                # Кнопка запуска фрагмента приложения
                st.button("Выполнить фрагмент")
                st.write(f"Фрагмент выполнен {st.session_state.fragment_runs} раз.")


            st.session_state.app_runs += 1

            # Вызов функции с декоратором @st.fragment
            my_fragment()

            # Кнопка перезапуска всего приложения
            st.button("Выполнить все приложение")
            st.write(f"Все приложение выполнено {st.session_state.app_runs} раз.")
            st.write(f"Приложение видит, что фрагмент выполнен {st.session_state.fragment_runs} раз.")
    elif options == "Листинг 5.15":
        st.write('Код листинга 5.15 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st

            # Скрыть боковую панель
            st.set_page_config(initial_sidebar_state="collapsed")

            if "value" not in st.session_state:
                st.session_state.value = "Заголовок при загрузке приложения"

            ##### Опция вызова st.rerun #####
            st.header(st.session_state.value)
            if st.button("Сменить заголовок"):
                st.session_state.value = "Новый заголовок"
                st.rerun()

            ##### Опция вызова функции #####
            st.header(st.session_state.value)

            def update_value():
                st.session_state.value = "Нажата кнопка вызова функции"

            st.button("Вызов функции", on_click=update_value)

            ##### Опция использования контейнера #####
            container = st.container()
            if st.button("Контейнер"):
                st.session_state.value = "Нажата кнопка изменения контейнера"

            container.header(st.session_state.value)
    elif options == "Листинг 5.16":
        st.write('Код листинга 5.16 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st

            # Скрыть боковую панель
            st.set_page_config(initial_sidebar_state="collapsed")

            # Задать начальное значение элементу session
            if 'bt' not in st.session_state:
                st.session_state.disabled = False
            else:
                st.session_state.disabled = True

            txt_1 = st.text('Приложение запущено')
            txt_2 = st.text('')

            # Создать кнопку
            bt = st.button('Остановка приложения',
                           key='bt',
                           disabled=st.session_state.disabled)

            # Обработать событие нажатия кнопки
            if bt:
                txt_1.text('Приложение остановлено')
                