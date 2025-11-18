import streamlit as st

st.badge("Радио кнопки")
genre = st.radio(
    label="Выберите категорию фильма",
    options=[":rainbow[Комедия]", "***Детектив***", "Историческое кино :movie_camera:"],
    index=0,
    captions=[
        "Отдохнуть и повеселится.",
        "Провести расследование.",
        "Окунуться в историю",
    ],
)

if genre == ":rainbow[Комедия]":
    st.write("Вы выбрали комедию")
elif genre == "***Детектив***":
    st.write("Вы выбрали детектив")
elif genre == "Историческое кино :movie_camera:":
    st.write("Вы выбрали Историческое кино")
else:
    st.write("Жанр не выбран")

st.divider()  # Разделитель

st.badge("Флажки и радиокнопки")
# Начальное значение виджетов в текущем сеансе
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False
    st.session_state.horizontal = False

# Разбивка страницы на колонки
col1, col2 = st.columns(2)

# Левая колонка с флажками
with col1:
    st.checkbox("Блокировать радиокнопки", key="disabled")
    st.checkbox("Радиокнопки в линию", key="horizontal")

# Правая колонка с радио кнопами
with col2:
    st.radio(
        label="Сделать метку видимой 👇",
        options=["visible", "hidden"],
        key="visibility",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        horizontal=st.session_state.horizontal,
    )