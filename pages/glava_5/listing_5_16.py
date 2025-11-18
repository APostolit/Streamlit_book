import streamlit as st

# Скрыть боковую панель
st.set_page_config(initial_sidebar_state="collapsed")

# Задать начальное значение элементу session
if 'bt' not in st.session_state:
    st.session_state.disabled = False
else:
    st.session_state.disabled = True

txt_1 = st.text('Приложение запущено')
txt_2 = st.text('')

# Создать кнопку
bt = st.button('Остановка приложения',
               key='bt',
               disabled=st.session_state.disabled)

# Обработать событие нажатия кнопки
if bt:
    txt_1.text('Приложение остановлено')
    txt_2.text('пользователем, нажатием кнопки')
    st.session_state.disabled = True
    st.stop()