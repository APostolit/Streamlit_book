import streamlit as st

st.text('Элемент st.expander')

with st.expander("График Pandas"):
    st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

with st.expander("Открыть изображение st.expander"):
    st.write('''
       Академия Python. Цифровые интерактивные книги, учебники
        и учебные пособия.
    ''')
    st.image("AP_400.png")


expander = st.expander("Показать изображение по URL")
expander.write('Это изображение загружено из сети интернет')
expander.image("https://static.streamlit.io/examples/dice.jpg")