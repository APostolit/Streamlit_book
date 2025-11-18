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
    color='Origin',)
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