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