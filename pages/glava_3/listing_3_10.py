import streamlit as st

st.text("Элементы st.pills")

st.divider()  # Разделитель
st.badge("Множественный выбор")
options = ["Яблоки", "Груши", "Апельсины", "Мандарины"]
select_1 = st.pills("Фрукты ", options, selection_mode="multi")
if select_1:
    st.markdown(f"Вы выбрали: {select_1}.")
st.divider()  # Разделитель

st.badge("Простой выбор")
option_map = {
    1: ":material/add:",
    2: ":material/zoom_in:",
    3: ":material/zoom_out:",
    4: ":material/zoom_out_map:",
}
select_2 = st.pills(
    "Инструменты масштабирования",
    options=option_map.keys(),
    format_func=lambda option: option_map[option],
    selection_mode="single",
)
if select_2:
    st.write(
        "Ваш выбор: "
        f"{None if select_2 is None else option_map[select_2]}"
    )
st.divider()  # Разделитель