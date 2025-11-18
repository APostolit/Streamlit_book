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
            pitch=50,),
        layers=[
            pdk.Layer(
                "HexagonLayer",
                data=df,
                get_position="[lon, lat]",
                radius=200,
                elevation_scale=4,
                elevation_range=[0, 500],
                pickable=True,
                extruded=True,),
            pdk.Layer(
                "ScatterplotLayer",
                data=df,
                get_position="[lon, lat]",
                get_color="[200, 30, 0, 160]",
                get_radius=200,),
        ],
    )

st.write('Карта с библиотекой pydeck и элементом st.pydeck_chart')
st.pydeck_chart(fig)