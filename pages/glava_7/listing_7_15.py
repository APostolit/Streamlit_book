import streamlit as st

st.title('Приложение - счетчик')
count = 0

bt_increment = st.button('Увеличить счетчик')
if bt_increment:
    count += 1

st.write('Показание счетчика = ', count)
