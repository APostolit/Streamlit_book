import streamlit as st

st.text('Элемент st.dialog')

# функция - диалог
@st.dialog("Диалог - выбор цвета")
# Обработка ответа пользователя
def vote(item):
    st.write(f"Почему вы выбрали {item}?")
    reason = st.text_input("Потому, что...")
    if st.button("Ответить"):
        st.session_state.vote = {"item": item, "reason": reason}
        st.rerun()

# Формирование вопроса к пользователю
if "vote" not in st.session_state:
    st.write("Какой цвет вам нравится больше всего?")
    if st.button("Красный"):
        vote("Красный")
    if st.button("Синий"):
        vote("Синий")
else:
    st.text(f"Вы выбрали {st.session_state.vote['item']} потому, "
            f"что {st.session_state.vote['reason']}")