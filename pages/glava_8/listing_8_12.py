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