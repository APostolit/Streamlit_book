import streamlit as st

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 8", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

# Текст по центру страницы
st.columns(3)[1].header("👩🏻‍💻Примеры главы 8")

# Контейнер
cont_1 = st.container(width=300)
with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги главы 6",
        ("Листинг 8.1", "Листинг 8.2", "Листинг 8.3", "Листинг 8.4",
         "Листинг 8.5", "Листинг 8.6", "Листинг 8.7", "Листинг 8.8",
         "Листинг 8.9", "Листинг 8.10", "Листинг 8.11", "Листинг 8.12"),
        index=None,
        placeholder="Выберите листинг..."
    )

# Контейнер
cont_2 = st.container()
with cont_2:
    if options is None:
        st.write('Листинг не выбран')
    elif options == "Листинг 8.1":
        st.write('Код листинга 8.1 и результаты его выполнения')
        with st.echo(code_location="above"):
            import pandas as pd
            import streamlit as st
            from numpy.random import default_rng as rng
            from vega_datasets import data

            # Скрыть боковую панель
            st.set_page_config(initial_sidebar_state="collapsed")

            df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])

            st.write('Диаграмма st.area_chart с параметрами по умолчанию')
            st.area_chart(df)

            df = pd.DataFrame(
                {
                    "col1": list(range(20)) * 3,
                    "col2": rng(0).standard_normal(60),
                    "col3": ["a"] * 20 + ["b"] * 20 + ["c"] * 20,
                }
            )

            st.write('Диаграмма st.area_chart с параметрами x, y и color')
            st.area_chart(df, x="col1", y="col2", color="col3")

            df = data.unemployment_across_industries()
            st.write('Диаграмма st.area_chart с параметрами x, y, color,stack')
            st.area_chart(df, x="date", y="count", color="series", stack="center")
    elif options == "Листинг 8.2":
        st.write('Код листинга 8.2 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st
            import pandas as pd

            # Скрыть боковую панель
            st.set_page_config(initial_sidebar_state="collapsed")

            # Создать набор данных
            data = pd.DataFrame({
                'Фрукты': ['Яблоки', 'Груши', 'Бананы', 'Апельсины'],
                'Количество': [15, 35, 25, 45]
            })

            st.write('Столбчатая диаграмма st.bar_chart')
            st.bar_chart(data, x='Фрукты', y='Количество')
    elif options == "Листинг 8.3":
        st.write('Код листинга 8.3 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st
            import pandas as pd

            # Скрыть боковую панель
            st.set_page_config(initial_sidebar_state="collapsed")

            # Создать dataframe
            df = pd.DataFrame({'Годы': ['2018', '2019', '2020', '2021'],
                               'Продажи': [350, 480, 550, 680]}
                              )
            # Создать диаграмму
            st.write('Линейная диаграмма st.line_chart')
            st.line_chart(df, x='Годы', y='Продажи',
                          x_label='Годы', y_label='Продажи')
    elif options == "Листинг 8.4":
        st.write('Код листинга 8.4 и результаты его выполнения')
        with st.echo(code_location="above"):
            import pandas as pd
            import streamlit as st
            from numpy.random import default_rng as rng

            # Координаты точек в районе г. Москва
            df = pd.DataFrame(
                rng(0).standard_normal((100, 2)) / [50, 50] + [55.7522, 37.6156],
                columns=["lat", "lon"],
            )
            st.write('Положение точек на карте г. Москва с элементом st.map_chart')
            st.map(df)

            df = pd.DataFrame(
                {
                    "col1": rng(0).standard_normal(100) / 50 + 55.7522,
                    "col2": rng(1).standard_normal(100) / 50 + 37.6156,
                    "col3": rng(2).standard_normal(100) * 100,
                    "col4": rng(3).standard_normal((100, 4)).tolist(),
                }
            )
            st.write('Карта г. Москва с точками разных цветов и размеров')
            st.map(df, latitude="col1", longitude="col2", size="col3", color="col4")
    elif options == "Листинг 8.5":
        st.write('Код листинга 8.5 и результаты его выполнения')
        with st.echo(code_location="above"):
            import pandas as pd
            import streamlit as st
            from numpy.random import default_rng as rng

            # Скрыть боковую панель
            st.set_page_config(initial_sidebar_state="collapsed")

            df = pd.DataFrame(rng(0).standard_normal((10, 3)), columns=["a", "b", "c"])

            st.write('Диаграмма st.scatter_chart с точками одного размера и цвета')
            st.scatter_chart(df)

            df = pd.DataFrame(
                rng(0).standard_normal((20, 3)), columns=["col1", "col2", "col3"]
            )
            df["col4"] = rng(0).choice(["a", "b", "c"], 20)

            st.write('Диаграмма st.scatter_chart с точками разного размера и цвета')
            st.scatter_chart(df,
                             x="col1",
                             y="col2",
                             color="col4",
                             size="col3")
    elif options == "Листинг 8.6":
        st.write('Код листинга 8.6 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st
            import altair as alt
            from vega_datasets import data
            import pandas as pd
            from numpy.random import default_rng as rng

            # Набор данных Pandas
            df = pd.DataFrame(rng(0).standard_normal((60, 3)), columns=["a", "b", "c"])

            # Диаграмма с параметрами altair
            chart = (
                alt.Chart(df)
                .mark_circle()
                .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
            )
            st.write('Диаграмма altair_chart с темой по умолчанию')
            st.altair_chart(chart)

            # Набор данных из библиотеки vega_datasets
            source = data.cars()

            # Диаграмма с параметрами altair
            chart = (alt.Chart(source).mark_circle().encode(
                x=alt.X('Horsepower',
                        title='Мощность двигателя (л.с)'),
                y=alt.Y('Miles_per_Gallon',
                        title='Расход топлива (мили/галон)'),
                color='Origin', )
                     .interactive())

            st.write('Диаграмма altair_chart с разными темами')

            # Вкладки страницы приложения
            tab1, tab2 = st.tabs(["Тема Streamlit (default)", "Тема Altair"])
            with tab1:
                # Диаграмма с темой Streamlit (по умолчанию).
                st.altair_chart(chart, theme="streamlit", use_container_width=True)
            with tab2:
                # Диаграмма с нативной темой Altair
                st.altair_chart(chart, theme=None, use_container_width=True)
    elif options == "Листинг 8.7":
        st.write('Код листинга 8.7 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st
            from bokeh.plotting import figure

            # Скрыть боковую панель
            st.set_page_config(initial_sidebar_state="collapsed")

            # Исходные данные
            x = [1, 2, 3, 4, 5]
            y = [2, 4, 8, 16, 32]

            # Создание графика с библиотекой Bokeh
            p = figure(title="График с библиотекой Bokeh",
                       x_axis_label="Ось x",
                       y_axis_label="Ось y")
            p.line(x, y, legend_label="Тренд", line_width=2)

            st.write('Диаграмма с элементом st.bokeh_chart')
            st.bokeh_chart(p)
    elif options == "Листинг 8.8":
        st.write('Код листинга 8.8 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st
            import graphviz

            # Скрыть боковую панель
            st.set_page_config(initial_sidebar_state="collapsed")

            st.write('Графы с элементом st.graphviz_chart')

            # Граф - родственники, как объект
            graph = graphviz.Digraph()
            graph.edge("Я", "Мать")
            graph.edge("Я", "Отец")
            graph.edge("Брат", "Мать")
            graph.edge("Брат", "Отец")
            graph.edge("Мать", "Бабушка по матери")
            graph.edge("Мать", "Дедушка по матери")
            graph.edge("Отец", "Бабушка по отцу")
            graph.edge("Отец", "Дедушка по отцу")
            graph.edge("Сестра", "Бабушка по матери")
            graph.edge("Сестра", "Бабушка по отцу")

            # Вкладки страницы приложения
            tab1, tab2 = st.tabs(["Граф 1", "Граф 2"])

            with tab1:
                st.write('Родственники')
                st.graphviz_chart(graph)

            with tab2:
                st.write('Кольцевой маршрут автобуса')
                # Граф кольцевой маршрут, как текстовая строка
                st.graphviz_chart('''
                    digraph {
                        Вокзал -> Магазин
                        Аптека -> Вокзал
                        Магазин -> Рынок            
                        Рынок -> Стадион
                        Стадион -> Школа
                        Школа -> Магазин
                        Магазин -> Аптека                
                    }
                ''')
    elif options == "Листинг 8.9":
        st.write('Код листинга 8.9 и результаты его выполнения')
        with st.echo(code_location="above"):
            import plotly.graph_objects as go
            import plotly.figure_factory as ff
            import streamlit as st
            from numpy.random import default_rng as rng

            # Скрыть боковую панель
            st.set_page_config(initial_sidebar_state="collapsed")

            # Формирование графика с библиотекой Plotly
            fig = go.Figure()
            fig.add_trace(
                go.Scatter(
                    x=[1, 2, 3, 4, 5],
                    y=[1, 3, 2, 5, 4]
                )
            )
            st.write('График plotly.graph_objects с элементом st.plotly_chart')
            st.plotly_chart(fig, config={'scrollZoom': False})

            # Формирование данных
            data = [
                rng(0).standard_normal(200) - 2,
                rng(1).standard_normal(200),
                rng(2).standard_normal(200) + 2,
            ]
            group_labels = ["Group 1", "Group 2", "Group 3"]

            # Формирование графика с библиотекой Plotly
            fig = ff.create_distplot(data,
                                     group_labels,
                                     bin_size=[0.1, 0.25, 0.5]
                                     )
            st.write('График plotly.figure_factory с элементом st.plotly_chart')
            st.plotly_chart(fig)
    elif options == "Листинг 8.10":
        st.write('Код листинга 8.10 и результаты его выполнения')
        with st.echo(code_location="above"):
            import pandas as pd
            import pydeck as pdk
            import streamlit as st
            from numpy.random import default_rng as rng

            # Скрыть боковую панель
            st.set_page_config(initial_sidebar_state="collapsed")

            # Сгенерировать данные
            df = pd.DataFrame(
                rng(0).standard_normal((100, 2)) / [60, 60] + [55.7522, 37.6156],
                columns=["lat", "lon"])

            # Создать объект pydeck
            fig = pdk.Deck(
                map_style=None,  # Тема Streamlit
                initial_view_state=pdk.ViewState(
                    latitude=55.7522,
                    longitude=37.6156,
                    zoom=11,
                    pitch=50, ),
                layers=[
                    pdk.Layer(
                        "HexagonLayer",
                        data=df,
                        get_position="[lon, lat]",
                        radius=200,
                        elevation_scale=4,
                        elevation_range=[0, 500],
                        pickable=True,
                        extruded=True, ),
                    pdk.Layer(
                        "ScatterplotLayer",
                        data=df,
                        get_position="[lon, lat]",
                        get_color="[200, 30, 0, 160]",
                        get_radius=200, ),
                ],
            )

            st.write('Карта с библиотекой pydeck и элементом st.pydeck_chart')
            st.pydeck_chart(fig)
    elif options == "Листинг 8.11":
        st.write('Код листинга 8.11 и результаты его выполнения')
        with st.echo(code_location="above"):
            import matplotlib.pyplot as plt
            import streamlit as st
            from numpy.random import default_rng as rng

            # Скрыть боковую панель
            st.set_page_config(initial_sidebar_state="collapsed")

            # Данные для гистограммы
            data = rng(0).normal(1, 1, size=100)
            # Формирование гистограммы с matplotlib
            fig, ax = plt.subplots()
            ax.hist(data, bins=20)

            st.write('График с библиотекой matplotlib')
            st.pyplot(fig)
    elif options == "Листинг 8.12":
        st.write('Код листинга 8.12 и результаты его выполнения')
        with st.echo(code_location="above"):
            import pandas as pd
            import streamlit as st
            from numpy.random import default_rng as rng
            from vega_datasets import data

            # Скрыть боковую панель
            st.set_page_config(initial_sidebar_state="collapsed")

            df = pd.DataFrame(rng(0).standard_normal((60, 3)), columns=["a", "b", "c"])

            v_spec = {
                "mark": {"type": "circle", "tooltip": True},
                "encoding": {
                    "x": {"field": "a", "type": "quantitative"},
                    "y": {"field": "b", "type": "quantitative"},
                    "size": {"field": "c", "type": "quantitative"},
                    "color": {"field": "c", "type": "quantitative"},
                },
            }

            st.write('График с библиотекой Vega-Lite и элементом st.vega_lite_chart')
            st.vega_lite_chart(df, v_spec)

            # Набор данных из библиотеки vega_datasets
            source = data.cars()

            # Диаграмма с параметрами Vega-Lite
            chart = {
                "mark": "point",
                "encoding": {
                    "x": {
                        "field": "Horsepower",
                        "type": "quantitative",
                        "title": "Мощность двигателя (л.с.)",
                    },
                    "y": {
                        "field": "Miles_per_Gallon",
                        "type": "quantitative",
                        "title": "Расход топлива (мили/галон)",
                    },
                    "color": {"field": "Origin", "type": "nominal"},
                    "shape": {"field": "Origin", "type": "nominal"},
                },
            }

            st.write('Диаграмма Vega-Lite с разными темами')

            tab1, tab2 = st.tabs(["Тема Streamlit (default)", "Нативная тема Vega-Lite"])

            with tab1:
                # Диаграмма с темой Streamlit (по умолчанию).
                st.vega_lite_chart(source,
                                   chart,
                                   theme="streamlit",
                                   use_container_width=True)
            with tab2:
                # Диаграмма с нативной темой Vega-Lite
                st.vega_lite_chart(source,
                                   chart,
                                   theme=None,
                                   use_container_width=True)
                