import streamlit as st
import numpy as np

# Отправка сообщения из st.chat_message программы
with st.chat_message("user"):
    st.write("Вывод графика в блоке with 👋")
    st.line_chart(np.random.randn(20, 3))

# Отправка сообщения из программы
message = st.chat_message("assistant")
message.write("Вывод график с использованием метода объекта")
message.bar_chart(np.random.randn(20, 3))

# Отправка сообщения от пользователя
with st.sidebar:
    st.text('Элемент st.chat_message')
    messages = st.container(height=300)
    if prompt := st.chat_input("Введите сообщение"):
        messages.chat_message("user").write(f"Введено: {prompt}")
        messages.chat_message("assistant").write(f"Отправлено: {prompt}")