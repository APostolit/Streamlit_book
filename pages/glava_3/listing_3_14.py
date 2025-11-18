import streamlit as st

st.text("Элементы st.select_slider")

st.badge("Выбор одного значения")
c = st.select_slider(
    "Выберите страну",
    options=["Россия", "Китай", "США", "Великобритания",
        "Франция", "Германия", "Италия", ],)
st.write("Выбрана страна:", c)

st.divider()  # Разделитель

st.badge("Выбор двух значений")
start_color, end_color = st.select_slider(
    "Выберите диапазон цветов",
    options=["red", "orange", "yellow", "green",
        "blue", "indigo", "violet",],
    value=("red", "blue"),
)
st.write("Выбраны цвета:", start_color, "и", end_color)