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