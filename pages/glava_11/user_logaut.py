import streamlit as st

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Выход",   # Текст на вкладке браузера
    page_icon='🚪️',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Свернуть боковую панель
)

cont = st.container(border=True, width=400)
with cont:
    st.subheader("Выйти из системы🚪🏃‍♂️‍➡️")
    bd_user = st.session_state['user_name']
    st.write('Выход пользователя- 👨', bd_user)
    btn = st.button(label='Выйти из системы╰┈➤')

if btn:
    st.session_state['user_name'] = None
    st.session_state['legal'] = False
    #  Перейти на главную страницу
    st.switch_page(page="pages/home_reg.py")
