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