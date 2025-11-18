import streamlit as st
import time

# Скрыть боковую панель
st.set_page_config(initial_sidebar_state="collapsed")

# Функция - фрагмент приложения
@st.fragment
def start_balloons():
    # Кнопка выпуска воздушных шаров
    st.button("Выпустить воздушные шары",
              help="Перезапуск фрагмента")
    st.balloons()

# Процесс надувания воздушных шаров
with st.spinner("Ждите...! Идет процесс надувания воздушных шаров."):
    time.sleep(5)

# Вызов функции выпуска воздушных шаров
start_balloons()

# Кнопка перезапуска всего приложения
st.button("Надуть воздушные шары и выпустить",
          help="Перезапуск приложения")