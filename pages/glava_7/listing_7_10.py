import streamlit as st

def page1():
    st.write(f'Выбраны фрукты -', st.session_state.Фрукты)
    st.write(f'Значение переключателя -', st.session_state.Переключатель)

def page2():
    st.write(f'Значение переключателя - ', st.session_state.Переключатель)
    st.write(f'Выбраны фрукты -', st.session_state.Фрукты)

# Виджеты, общие для всех страниц
st.sidebar.selectbox("Фрукты", ["Яблоки", "Груши", "Сливы"], key="Фрукты")
st.sidebar.checkbox("Переключатель", key="Переключатель")

pg = st.navigation([page1, page2])
pg.run()