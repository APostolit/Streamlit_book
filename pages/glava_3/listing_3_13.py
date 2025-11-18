import streamlit as st

st.badge("Виджет st.selectbox с начальным значением элемента выбора")
option = st.selectbox(
    "Выберите способ связи",
    ("E-mail", "Стационарный телефон", "Мобильный телефон"),
)
if option:
    st.write("Сделан выбор-", option)
st.divider()  # Горизонтальная линия

st.badge("Виджет st.selectbox без начального значения элемента выбора")
option = st.selectbox(
    "Выберите способ связи",
    ("E-mail", "Стационарный телефон", "Мобильный телефон"),
    index=None,
    placeholder="Выберите способ связи..."
)
if option:
    st.write("Сделан выбор-", option)
st.divider()  # Горизонтальная линия

st.badge("Виджет st.selectbox с возможностью ввода элемента выбора")
option = st.selectbox(
    "Электронная почта",
    ["victor@mail.ru", "oleg@mail.ru", "maxim@mail.ru"],
    index=None,
    placeholder="Выберите или введите e-mail",
    accept_new_options=True,
)
st.write("Сделан выбор-", option)
st.divider()  # Горизонтальная линия

# Инициализация значений виджетов в состоянии сессии
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

st.badge("Управление состоянием виджет st.selectbox")
# Создание контейнера
cont = st.container(border=True)

# Создание колонок в контейнере
with cont:
    col1, col2 = st.columns(2)

with col1:
    st.checkbox("Сделать виджет недоступным", key="disabled")
    radio = st.radio(
        "Изменить видимость метки 👉",
        options=["Показать", "Скрыть", "Свернуть"],
    )
    if radio:
        if radio == "Скрыть":
            st.session_state.visibility = "hidden"
        elif radio == "Показать":
                st.session_state.visibility = "visible"
        elif radio == "Свернуть":
            st.session_state.visibility = "collapsed"

with col2:
    option1 = st.selectbox(
        "Выберите способ связи",
        ("Email", "Домашний", "Мобильный"),
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
    )