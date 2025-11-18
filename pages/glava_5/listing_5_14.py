import streamlit as st

# Скрыть боковую панель
st.set_page_config(initial_sidebar_state="collapsed")

# Задать значения счетчикам при первом запуске приложения
if "app_runs" not in st.session_state:
    st.session_state.app_runs = 0
    st.session_state.fragment_runs = 0

# Функция с фрагментом приложения
@st.fragment
def my_fragment():
    st.session_state.fragment_runs += 1
    # Кнопка запуска фрагмента приложения
    st.button("Выполнить фрагмент")
    st.write(f"Фрагмент выполнен {st.session_state.fragment_runs} раз.")

st.session_state.app_runs += 1

# Вызов функции с декоратором @st.fragment
my_fragment()

# Кнопка перезапуска всего приложения
st.button("Выполнить все приложение")
st.write(f"Все приложение выполнено {st.session_state.app_runs} раз.")
st.write(f"Приложение видит, что фрагмент выполнен {st.session_state.fragment_runs} раз.")