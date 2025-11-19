import streamlit as st

st.title('Приложение - счетчик')

if 'aaa' not in st.session_state:
    st.session_state.aaa = 0

# Обнуление счетчика
if 'count' not in st.session_state:
    st.session_state.count = 0

bt_increment = st.button('Увеличить счетчик')
# Увеличить счетчик
if bt_increment:
    st.session_state.count += 1
    st.session_state.aaa += 2

st.write('Показание счетчика = ', st.session_state.count)
st.write('Показание счетчика = ', st.session_state.aaa)