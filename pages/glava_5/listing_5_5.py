import streamlit as st
import time

st.text('Функция st.empty с элементом container')

# Кнопка перезапуска приложения
st.button("Перезапустить")

# Создание пустой области страницы
placeholder = st.empty()

# Вывод в пустую область текста
placeholder.markdown("Старт работы программы")
time.sleep(3)

# Вывод в пустую область индикатора состояния
placeholder.progress(0, "Ждите, идет процесс ...")
time.sleep(2)
placeholder.progress(50, "Ждите, идет процесс ...")
time.sleep(2)
placeholder.progress(100, "Ждите, идет процесс ...")
time.sleep(2)

# Создание в пустой области контейнера
with placeholder.container():
    st.line_chart({"data": [1, 5, 2, 6]})
    time.sleep(1)
    st.markdown("3...")
    time.sleep(1)
    st.markdown("2...")
    time.sleep(1)
    st.markdown("1...")
    time.sleep(1)
    # Вывод в пустую область текста
    st.markdown("Заполнение пустой области завершено!")
    time.sleep(5)

# Очистка пустой области
placeholder.empty()