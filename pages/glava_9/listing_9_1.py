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