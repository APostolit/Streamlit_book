import streamlit as st

st.sidebar.text('Элемент st.sidebar')

# Добавление элементов через метод
add_selectbox = st.sidebar.selectbox(
    "Как поддерживать обратную связь?",
    ("По Email", "По телефону", "По мобильному тел.")
)

# Добавление элементов через with
with st.sidebar:
    add_radio = st.radio(
        "Выберите способ доставки",
        ("Стандартная (5-15 дней)", "Быстрая (2-3 дня)")
    )