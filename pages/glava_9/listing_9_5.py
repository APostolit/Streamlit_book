import streamlit as st

# Скрыть боковую панель
st.set_page_config(initial_sidebar_state="collapsed")

st.markdown("## Элемент st.json")
st.json(
    {
        "Напиток": "Молоко",
        "Фрукты": [ "Яблоки", "Груши", "Мандарины",],
        "Уровень 1": {"Уровень 2": {"Уровень 3": {"Ключ": "Значение"}}},
    },
    expanded=2,
)