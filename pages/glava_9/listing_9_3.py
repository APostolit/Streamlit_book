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