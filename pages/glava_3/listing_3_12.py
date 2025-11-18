import streamlit as st

st.text("Элементы st_segmented_control")

st.divider()  # Разделитель
st.badge("Множественный выбор")
options = ["Север", "Восток", "Юг", "Запад"]
select_1 = st.segmented_control(
    "Направление", options, selection_mode="multi"
)
if select_1:
    st.markdown(f"Выбрано: {select_1}.")

st.divider()  # Разделитель

st.badge("Выбор одного элемента")
option_map = {
    0: ":material/add:",
    1: ":material/zoom_in:",
    2: ":material/zoom_out:",
    3: ":material/zoom_out_map:",
}
select_2 = st.segmented_control(
    "Инструменты масштабирования",
    options=option_map.keys(),
    format_func=lambda option: option_map[option],
    selection_mode="single",
)

st.write(
    "Выбрано: "
    f"{None if select_2 is None else option_map[select_2]}"
    )