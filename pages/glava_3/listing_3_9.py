import streamlit as st

st.badge("Элемент st_multiselect")

st.divider()  # Разделитель
options = st.multiselect(
    "Подбор овощей для салата",
    ["Огурцы", "Помидоры", "Лук", "Морковь", "Капуста"],
    help="Выберите овощи в любом сочетании",
    placeholder='Набор овощей для салата'
)
st.divider()  # Разделитель
if options:
    st.write("Сделан выбор:", options)
st.divider()  # Разделитель