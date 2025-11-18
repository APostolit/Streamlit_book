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
st.plotly_chart(fig, config = {'scrollZoom': False})

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