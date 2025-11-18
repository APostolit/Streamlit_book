import matplotlib.pyplot as plt
import streamlit as st
from numpy.random import default_rng as rng

# Скрыть боковую панель
st.set_page_config(initial_sidebar_state="collapsed")

# Данные для гистограммы
data = rng(0).normal(1, 1, size=100)
# Формирование гистограммы с matplotlib
fig, ax = plt.subplots()
ax.hist(data, bins=20)

st.write('График с библиотекой matplotlib')
st.pyplot(fig)