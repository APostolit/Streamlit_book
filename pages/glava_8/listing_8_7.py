import streamlit as st
from bokeh.plotting import figure

# Скрыть боковую панель
st.set_page_config(initial_sidebar_state="collapsed")

# Исходные данные
x = [1, 2, 3, 4, 5]
y = [2, 4, 8, 16, 32]

# Создание графика с библиотекой Bokeh
p = figure(title="График с библиотекой Bokeh",
           x_axis_label="Ось x",
           y_axis_label="Ось y")
p.line(x, y, legend_label="Тренд", line_width=2)

st.write('Диаграмма с элементом st.bokeh_chart')
st.bokeh_chart(p)