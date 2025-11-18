import streamlit as st

st.text("Элементы st.feedback")
# Палец
st.badge("Палец")
sent_1 = [":material/thumb_down:", ":material/thumb_up:"]
selected_1 = st.feedback("thumbs")
if selected_1 is not None:
    st.markdown(f"Ваш выбор: {sent_1[selected_1]}")
st.divider()  # Разделитель

# Звезды
st.badge("Звезды")
sent_2 = ["1", "2", "3", "4", "5"]
selected_2 = st.feedback("stars")
if selected_2 is not None:
    st.markdown(f"Количество выбранных звезд {sent_2[selected_2]}")
st.divider()  # Разделитель


# Лица
st.badge("Лица")
sent_3 = ["1", "2", "3", "4", "5"]
selected_3 = st.feedback("faces")
if selected_3 is not None:
    st.markdown(f"Оценка пользователя {sent_3[selected_3]}")
st.divider()  # Разделитель