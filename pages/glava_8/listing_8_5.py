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