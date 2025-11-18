import streamlit as st

# Скрыть боковую панель
st.set_page_config(initial_sidebar_state="collapsed")

if "value" not in st.session_state:
    st.session_state.value = "Заголовок при загрузке приложения"

##### Опция вызова st.rerun #####
st.header(st.session_state.value)
if st.button("Сменить заголовок"):
    st.session_state.value = "Новый заголовок"
    st.rerun()

##### Опция вызова функции #####
st.header(st.session_state.value)
def update_value():
    st.session_state.value = "Нажата кнопка вызова функции"

st.button("Вызов функции", on_click=update_value)

##### Опция использования контейнера #####
container = st.container()
if st.button("Контейнер"):
    st.session_state.value = "Нажата кнопка изменения контейнера"

container.header(st.session_state.value)