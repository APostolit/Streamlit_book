import streamlit as st

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 9", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

# Текст по центру страницы
st.columns(3)[1].header("👩🏻‍💻Примеры главы 9")

# Контейнер
cont_1 = st.container(width=300)
with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги главы 9",
        ("Листинг 9.1", "Листинг 9.2", "Листинг 9.3", "Листинг 9.4",
         "Листинг 9.5", "Листинг 9.6", "Листинг 9.7", "Листинг 9.8",
         "Листинг 9.9", "Листинг 9.10"),
        index=None,
        placeholder="Выберите листинг..."
    )

# Контейнер
cont_2 = st.container()
with cont_2:
    if options is None:
        st.write('Листинг не выбран')
    elif options == "Листинг 9.1":
        st.write('Код листинга 9.1 и результаты его выполнения')
        with st.echo(code_location="above"):
            import pandas as pd
            import streamlit as st
            from numpy.random import default_rng as rng

            # Скрыть боковую панель
            st.set_page_config(initial_sidebar_state="collapsed")

            # Сформировать набор данных
            df = pd.DataFrame(
                rng(0).standard_normal((50, 20)),
                columns=("col %d" % i for i in range(20))
            )

            st.write('Простая таблица с элементом st.dataframe')
            st.dataframe(df)

            # Сформировать набор данных
            df = pd.DataFrame(
                {
                    "name": ["Новое в Streamlit", "Библиотека Extras", "Описание ошибок"],
                    "url": [
                        "https://roadmap.streamlit.app",
                        "https://extras.streamlit.app",
                        "https://issues.streamlit.app",
                    ],
                    "stars": rng(0).integers(0, 1000, size=3),
                    "views_history": rng(0).integers(0, 5000, size=(3, 30)).tolist(),
                }
            )

            st.write('Таблица с элементом st.dataframe и конфигуратором колонок')
            st.dataframe(
                df,
                column_config={
                    "name": "Имя приложения",
                    "stars": st.column_config.NumberColumn(
                        "Звезды Github",
                        help="Количество звезд на GitHub",
                        format="%d ⭐",
                    ),
                    "url": st.column_config.LinkColumn("URL адрес"),
                    "views_history": st.column_config.LineChartColumn(
                        "Просмотры (последние 30 дней)", y_min=0, y_max=5000
                    ),
                },
                hide_index=True,
            )
    elif options == "Листинг 9.2":
        st.write('Код листинга 9.2 и результаты его выполнения')
        with st.echo(code_location="above"):
            import pandas as pd
            import streamlit as st

            # Набор данных
            df = pd.DataFrame(
                [
                    {"Конфеты": "Белочка", "Количество (гр.)": 300, "Включить в набор": True},
                    {"Конфеты": "Мишка косолапый", "Количество (гр.)": 500, "Включить в набор": False},
                    {"Конфеты": "Птичье молоко", "Количество (гр.)": 800, "Включить в набор": True},
                    {"Конфеты": "Грильяж", "Количество (гр.)": 600, "Включить в набор": False},
                    {"Конфеты": "Трюфели", "Количество (гр.)": 200, "Включить в набор": True},
                ]
            )
            st.write('Редактируемая таблица с элементом st.data_editor')
            edited_df = st.data_editor(df)

            # Выбор  любимых конфет
            favorite = edited_df.loc[edited_df["Количество (гр.)"].idxmax()]["Конфеты"]
            st.markdown(f"Я больше всего люблю конфеты - **{favorite}** 👍")
    elif options == "Листинг 9.3":
        st.write('Код листинга 9.3 и результаты его выполнения')
        with st.echo(code_location="above"):
            import pandas as pd
            import streamlit as st
            from numpy.random import default_rng as rng

            # Скрыть боковую панель
            st.set_page_config(initial_sidebar_state="collapsed")

            # Набор данных
            df = pd.DataFrame(
                rng(0).standard_normal(size=(10, 5)),
                columns=("col %d" % i for i in range(5)),
            )
            st.write('Статичная таблица с элементом st.table')
            st.table(df)

            df = pd.DataFrame(
                {
                    "Элемент": ["**st.table**", "*st.dataframe*"],
                    "Тип": ["`Статичный`🧎️", "`Интерактивный`🏃‍♂️"],
                    "Ссылка на документацию": [
                        "[:rainbow[docs]](https://docs.streamlit.io"
                        "/develop/api-reference/data/st.dataframe)",
                        "[:open_book:](https://docs.streamlit.io"
                        "/develop/api-reference/data/st.table)",
                    ],
                }
            )

            # Набор данных
            st.write('Статичная таблица с элементом st.table и Markdown')
            st.table(df)
    elif options == "Листинг 9.4":
        st.write('Код листинга 9.4 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st

            # Скрыть боковую панель
            st.set_page_config(initial_sidebar_state="collapsed")

            # Данные:
            current_sales = 15000
            previous_sales = 12000
            sklad = 50
            sale = 45
            # Рассчитать разницу
            delta_sales = current_sales - previous_sales
            percentage_change = (delta_sales / previous_sales) * 100
            ostat = sklad - sale
            delta_kol = ostat - sklad

            st.markdown("## Элементы st.metric")

            # Отобразить метрики
            st.markdown("#### Динамика продаж")
            st.metric(label="Абсолютные продажи",
                      value=f"Р{current_sales}",
                      delta=f"Р{delta_sales}",
                      delta_color="normal")
            st.metric(label="Процент изменения",
                      value=f"{percentage_change:.2f}%",
                      delta=f"{percentage_change:.2f}%",
                      delta_color="normal",
                      width='content',
                      border=True)
            st.metric(label="Остаток на складе",
                      value=f"{ostat}",
                      delta=f"{delta_kol}",
                      delta_color="normal")

            st.markdown("## Элементы st.metric в колонках")
            col1, col2, col3 = st.columns(3)
            col1.metric("Температура", "25 °C", "3 °C", border=True)
            col2.metric("Ветер", "4 м/с", "-8%", border=True)
            col3.metric("Влажность", "75%", "4%", border=True)
    elif options == "Листинг 9.5":
        st.write('Код листинга 9.5 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st

            # Скрыть боковую панель
            st.set_page_config(initial_sidebar_state="collapsed")

            st.markdown("## Элемент st.json")
            st.json(
                {
                    "Напиток": "Молоко",
                    "Фрукты": ["Яблоки", "Груши", "Мандарины", ],
                    "Уровень 1": {"Уровень 2": {"Уровень 3": {"Ключ": "Значение"}}},
                },
                expanded=2,
            )
    elif options == "Листинг 9.6":
        st.write('Код листинга 9.6 и результаты ее выполнения')
        with st.echo(code_location="above"):
            import pandas as pd
            import streamlit as st

            # Скрыть боковую панель
            st.set_page_config(initial_sidebar_state="collapsed")

            st.markdown("#### Конфигуратор колонок для текстовых и числовых данных")

            # Набор данных
            data_df = pd.DataFrame(
                {
                    "Конфеты": ["Белочка", "Мишка на севере", "Трюфели", "Ласточка"],
                    "Упаковка": ["На вес", "На вес", "Коробка", "На вес"],
                    "Вес": [200, 400, 800, 1000],
                    "Цена": [200, 400, 250, 600],
                }
            )

            # Конфигуратор колонок
            col_config = {
                "Конфеты": st.column_config.Column(
                    label="Сорта конфет",
                    help="Введите сорт конфет",
                    width="medium",
                    required=True,
                ),
                "Упаковка": st.column_config.TextColumn(
                    label="Вид упаковки",
                    help="Как упакованы",
                    width="small",
                    required=True,
                ),
                "Вес": st.column_config.NumberColumn(
                    label="Вес (гр.)",
                    help="Введите вес",
                    width="small",
                    required=True,
                ),
                "Цена": st.column_config.NumberColumn(
                    label="Цена (руб.)",
                    help="Укажите цену",
                    width="small",
                    required=True,
                    format="₽%d"
                )
            }

            # Таблица с данными
            st.data_editor(data_df,
                           column_config=col_config,
                           hide_index=True,
                           num_rows="dynamic", )
    elif options == "Листинг 9.7":
        st.write('Код листинга 9.7 и результаты его выполнения')
        with st.echo(code_location="above"):
            import pandas as pd
            import streamlit as st

            # Скрыть боковую панель
            st.set_page_config(initial_sidebar_state="collapsed")

            st.markdown("#### Конфигуратор для колонок выбора")

            # Набор данных
            data_df = pd.DataFrame(
                {
                    "Конфеты": ["Белочка", "Мишка на севере", "Трюфели", "Ласточка"],
                    "Включить": [True, False, False, True],
                    "Упаковка": ["На вес⚖️", "На вес⚖️", "Коробка🍫", "На вес⚖️"],
                    "Вес": [200, 400, 800, 1000],
                }
            )

            # Конфигуратор колонок
            col_config = {
                "Конфеты": st.column_config.Column(
                    label="Сорта конфет",
                    help="Введите сорт конфет",
                    width="medium",
                    required=True,
                ),
                "Включить": st.column_config.CheckboxColumn(
                    label="Включить в набор?",
                    help="Выберите любимые конфеты 🤎",
                    default=False,
                ),
                "Упаковка": st.column_config.SelectboxColumn(
                    label="Упаковка",
                    help="Выбор типа упаковки",
                    width="medium",
                    options=["На вес⚖️", "Коробка🍫", ],
                    required=True,
                ),
                "Вес": st.column_config.NumberColumn(
                    label="Вес (гр.)",
                    help="Введите вес",
                    width="small",
                    required=True,
                ),
            }

            # Таблица с данными
            st.data_editor(data_df,
                           column_config=col_config,
                           hide_index=True,
                           num_rows="dynamic", )
    elif options == "Листинг 9.8":
        st.write('Код листинга 9.8 и результаты его выполнения')
        with st.echo(code_location="above"):
            from datetime import datetime
            from datetime import time
            import pandas as pd
            import streamlit as st

            # Скрыть боковую панель
            st.set_page_config(initial_sidebar_state="collapsed")

            st.markdown("#### Конфигуратор для колонок даты и времени")

            # Набор данных
            data_df = pd.DataFrame(
                {
                    "Лекции": [
                        datetime(2025, 2, 5, 8, 00),
                        datetime(2025, 2, 6, 9, 45),
                        datetime(2025, 2, 7, 11, 30), ],
                    "Праздники": [
                        datetime(2025, 2, 23),
                        datetime(2025, 3, 8),
                        datetime(2025, 5, 1)],
                    "Время": [
                        time(8, 00),
                        time(13, 00),
                        time(18, 00), ],
                }
            )

            # Конфигуратор колонок
            col_config = {
                "Лекции": st.column_config.DatetimeColumn(
                    label="Начало лекций ✍",
                    min_value=datetime(2025, 2, 1),
                    max_value=datetime(2025, 6, 5),
                    format="D MMM YYYY, h:mm a ✍",
                    step=60, ),
                "Праздники": st.column_config.DateColumn(
                    label="Праздники 🎇",
                    format="D MMM YYYY", ),
                "Время": st.column_config.TimeColumn(
                    label="Время приема пищи",
                    format="HH:mm 👩🏻‍🍳", ),
            }

            # Таблица с данными
            st.data_editor(
                data_df,
                column_config=col_config,
                hide_index=True,
            )
    elif options == "Листинг 9.9":
        st.write('Код листинга 9.9 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st
            import pandas as pd

            # Скрыть боковую панель
            st.set_page_config(initial_sidebar_state="collapsed")

            # Набор данных
            data_df = pd.DataFrame(
                {
                    "json": [
                        {"Напитки": ["Молоко", "Квас", "Лимонад"]},
                        {"Фрукты": ["Яблоки", "Груши", "Мандарины"]},
                        {"Овощи": ["Лук", "Морковь", "Капуста", ]}
                    ],
                    "Продажи": [
                        [10, 14, 26, 80, 90, 40],
                        [10, 20, 80, 80, 70, 10],
                        [10, 10, 20, 90, 30, 50]
                    ],
                    "Сайты": [
                        "https://dzen.ru",
                        "https://google.com",
                        "https://mail.ru",
                    ],
                    "img": [
                        "https://storage.googleapis.com/s4a-prod-share-preview/default/"
                        "st_app_screenshot_image/5435b8cb-6c6c-490b-9608-799b543655d3/Home_Page.png",
                        "https://storage.googleapis.com/s4a-prod-share-preview/default/"
                        "st_app_screenshot_image/ef9a7627-13f2-47e5-8f65-3f69bb38a5c2/Home_Page.png",
                        "https://storage.googleapis.com/s4a-prod-share-preview/default/"
                        "st_app_screenshot_image/31b99099-8eae-4ff8-aa89-042895ed3843/Home_Page.png",
                    ],
                }
            )

            # Конфигуратор колонок
            conf = {
                "json": st.column_config.JsonColumn(
                    label="Данные JSON",
                    help="Данные формата JSON",
                    width="medium", ),
                "Продажи": st.column_config.ListColumn(
                    label="Продажи (список)",
                    help="Продажи за последние 6 месяцев",
                    width="medium", ),
                "Сайты": st.column_config.LinkColumn(
                    label="Сайты",
                    help="Ссылки на сайты",
                ),
                "img": st.column_config.ImageColumn(
                    label="Изображения",
                    help="Скриншоты приложений Streamlit"
                )
            }

            st.markdown("## Таблица с данными объектов")
            # Таблица с данными
            st.data_editor(
                data_df,
                column_config=conf,
                hide_index=True)
    elif options == "Листинг 9.10":
        st.write('Код листинга 9.10 и результаты его выполнения')
        with st.echo(code_location="above"):
            import pandas as pd
            import streamlit as st

            # Скрыть боковую панель
            st.set_page_config(initial_sidebar_state="collapsed")

            # Набор данных
            data_df = pd.DataFrame(
                {
                    "sales1": [
                        [0, 4, 26, 80, 100, 40],
                        [80, 20, 80, 35, 40, 100],
                        [10, 20, 80, 80, 70, 0],
                    ],
                    "sales2": [
                        [0, 4, 26, 80, 100, 40],
                        [80, 20, 80, 35, 40, 100],
                        [10, 20, 80, 80, 70, 0],
                    ],
                    "sales3": [
                        [0, 4, 26, 80, 100, 40],
                        [80, 20, 80, 35, 40, 100],
                        [10, 20, 80, 80, 70, 0],
                    ],
                    "sales4": [200, 550, 1000],
                }
            )

            # Конфигуратор колонок
            conf = {
                "sales1": st.column_config.AreaChartColumn(
                    label="График областей",
                    width="small",
                    help="Продажи за 6 мес. с выделением области",
                    y_min=0,
                    y_max=400,
                ),
                "sales2": st.column_config.LineChartColumn(
                    label="График линий)",
                    width="small",
                    help="Продажи за 6 мес. (линия)",
                    y_min=0,
                    y_max=100,
                ),
                "sales3": st.column_config.BarChartColumn(
                    label="Столбчатый график ",
                    width="small",
                    help="Продажи за 6 мес. (столбчатый график))",
                    y_min=0,
                    y_max=100,
                ),
                "sales4": st.column_config.ProgressColumn(
                    label="Индикатор (объем продаж)",
                    help="Объем продаж (индикатор)",
                    format="₽%f",
                    min_value=0,
                    max_value=1000,
                ),
            }

            st.markdown("## Таблица с диаграммами")
            # Таблица с данными
            st.data_editor(
                data_df,
                column_config=conf,
                hide_index=True,
                row_height=100
            )
