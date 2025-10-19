import streamlit as st

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 2", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

# Текст по центру страницы
st.columns(3)[1].header("👩🏻‍💻Примеры главы 2")

# Контейнер
cont_1 = st.container(width=300)
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
    elif options == "Листинг 2.1":
        st.write('Код листинга 2.1 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st
            import pandas as pd
            import altair as alt
            from numpy.random import default_rng as rng
            from PIL import Image

            # Простая строка
            st.write("Вывод простой строки")

            # Строка с иконкой
            st.write("Вас приветствует, *Streamlit!* :sunglasses:")

            # Вывод числа
            st.write(1234)

            # Вывод набора данных Pandas
            df = pd.DataFrame(
                {
                    "Колонка 1": [1, 2, 3, 4],
                    "Колонка 2": [10, 20, 30, 40],
                }
            )
            st.write(df)

            # Вывод нескольких элементов
            st.write("1 + 1 = ", 2)
            st.write("Заголовок таблицы:", df, "Текст после таблицы")

            # Вывод графика
            df = pd.DataFrame(rng(0).standard_normal((200, 3)), columns=["a", "b", "c"])
            chart = (
                alt.Chart(df)
                .mark_circle()
                .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
            )
            st.write(chart)

            # Вывод изображения
            img = Image.open('static/AP_400.png')
            st.write(img)
    elif options == "Листинг 2.2":
        st.write('Код листинга 2.2 и результаты его выполнения')
        with st.echo(code_location="above"):
            import time
            import numpy as np
            import pandas as pd
            import streamlit as st
            from PIL import Image

            txt = """
            Функция st.write_stream в библиотеке Streamlit позволяет писать данные 
            в приложение в режиме потоковой передачи. 
            Это позволяет динамически обновлять отображаемый контент 
            по мере поступления новых данных.
            """

            def stream_data():
                # Вывод текста
                for word in txt.split(" "):
                    yield word + " "
                    time.sleep(0.10)

                # Вывод набора данных
                yield pd.DataFrame(
                    np.random.randn(5, 10),
                    columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
                )

                # Вывод изображения
                yield Image.open('static/AP_400.png')


            if st.button("Загрузить элементы"):
                st.write_stream(stream_data)
    elif options == "Листинг 2.3":
        st.write('Код листинга 2.3 и результаты его выполнения')
        with st.echo(code_location="above"):
            import matplotlib.pyplot as plt
            import numpy as np
            import pandas as pd

            # Вывод текста
            '''
            # Заголовок страница
            Это текст с использованием _markdown_.
            '''

            # Формирование набора данных
            df = pd.DataFrame({'Данные': [1, 2, 3]})
            "Пример вывода таблицы"
            df  # Вывод набора данных

            # Формирование числового объекта
            x = 10
            'x=', x  # Вывод строки и значения объекта X

            # Формирование графика с библиотекой matplotlib
            arr = np.random.normal(1, 1, size=100)
            fig, ax = plt.subplots()
            ax.hist(arr, bins=20)

            'Пример вывода графика'
            fig  # Вывод графика matplotlib
    elif options == "Листинг 2.4":
        st.write('Код листинга 2.4 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st

            # Элементы title
            st.title("Заголовок страницы")
            st.title("_Заголовок курсив с иконкой_ :sunglasses:")
            st.title(":blue[Заголовок цветной]")

            # Элементы header
            st.header("_Заголовок курсив_ :blue[цветной] с иконкой :sunglasses:")
            st.header("Заголовок с серым разделителем", divider="gray")
            st.header("Заголовки динамичными разделителями")
            st.header("Заголовок 1", divider=True)
            st.header("Заголовок 2", divider=True)
            st.header("Заголовок 3", divider=True)

            # Элементы subheader
            st.subheader("_Подзаголовок курсив_ :blue[цветной] с иконкой :sunglasses:")
            st.subheader("Подзаголовок в серым разделителем", divider="gray")
            st.subheader("Подзаголовки динамичными разделителями")
            st.subheader("Подзаголовок 1", divider=True)
            st.subheader("Подзаголовок 2", divider=True)
            st.subheader("Подзаголовок 3", divider=True)

            # Элементы markdown
            st.markdown("*Streamlit* действительно **'крутой'** ***Фреймворк!!!***.")

            st.markdown('''
                :red[Streamlit] :orange[может] :green[выводить] :blue[текст] :violet[в]
                :gray[различных] :rainbow[цветах] и :blue-background[выделять цветным фоном].''')

            st.markdown("А это букет из иконок &mdash;\
                        :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

            multi = '''Если вы в коде перенесли часть текста на новую строку,
            то она будет показана одной строкой.

            Для разделения текста между строками можно добавить пустую строку.
            '''
            st.markdown(multi)

            # Текст мелким шрифтом
            st.markdown(':small[Текст мелким шрифтом]')
    elif options == "Листинг 2.5":
        st.write('Код листинга 2.5 и результаты его выполнения')
        with st.echo(code_location="above"):
            import base64
            import streamlit as st

            # Задать имя PDF файла
            pdf_file = 'pdf/Python_vsem.pdf'

            # Открыть PDF файл
            with open(pdf_file, "rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')

            # Создать объект для вывода в HTML
            pdf_display = (F'<embed src="data:application/pdf;base64,{base64_pdf}"'
                           F' width="1000" height="800" type="application/pdf">')

            st.subheader(":blue[Содержимое PDF файла с оглавлением]")

            # Отобразить содержимое PDF файла
            st.markdown(body=pdf_display, unsafe_allow_html=True)
    elif options == "Листинг 2.6":
        st.write('Код листинга 2.6 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st

            # Элемент st.badge
            st.badge("Бейджик")
            st.badge("Завершено успешно", icon=":material/check:", color="green")

            # Несколько значков рядом
            st.markdown(
                ":violet-badge[:material/star: Лучший фильм] :orange-badge[⚠️ Внимание]"
                " :material/chronic: :gray-badge[На обсуждении]"
            )
            st.divider()  # Разделитель

            # Элемент st.caption
            st.caption("Это строка с примером текста мелким шрифтом.")
            st.caption("Это строка с текстом _italics_ :blue[синего цвета] и с эмодзи :sunglasses:")
            st.divider()  # Разделитель

            # Элемент st.code
            code = '''
            def hello():
                print("Привет Streamlit!")
                for i range(10):
                    print('Шаг цикла-", i)
            '''
            st.code(code, language="python", line_numbers=True)
            st.divider()  # Разделитель

            # Элемент st.echo (программный код после результатов его выполнения)
            with st.echo(code_location="below"):
                st.write('Вывод текстовой строки на страницу приложения')
            st.divider()

            # Элемент st.echo (программный код перед результатами его выполнения)
            with st.echo(code_location="above"):
                # Содержимое этого блока, будет как выведено на экране, так и выполнено
                def get_user_name(code_location="above" or "below"):
                    return 'Виктор!'

                greeting = "Приветствую тебя, "
                value = get_user_name()
                st.write(greeting, value)
            st.divider()  # Разделитель

            go = 'Продолжение программы'
            st.write(go)
            st.divider()  # Разделитель

            # Элемент st.echo
            st.latex(r'''
                a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
                \sum_{k=0}^{n-1} ar^k =
                a \left(\frac{1-r^{n}}{1-r}\right)
                ''')
            st.divider()  # Разделитель

            # Элемент st.text
            st.text("Это первая строка текста.\n [Это вторая строка, ](продолжение второй строки).")
    elif options == "Листинг 2.7":
        st.write('Код листинга 2.7 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st

            # Скрыть боковую панель
            st.set_page_config(initial_sidebar_state="collapsed")

            st.markdown("## Элемент st.help")
            st.text('Справка об элементе st.title')
            st.help(st.title)
    elif options == "Листинг 2.8":
        st.write('Код листинга 2.8 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st

            # Скрыть боковую панель
            st.set_page_config(initial_sidebar_state="collapsed")

            st.markdown("#### Элемент st.html")

            st.html("<h1><span style='color:blue;'>Заголовок H1 (синим цветом)</span></h1>")
            st.html("<style> h1 {color: red;}</style>"
                    "<body><h1>Заголовок H1 красным цветом</h1></body>")