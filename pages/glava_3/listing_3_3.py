import streamlit as st

# Создать форму
with st.form(key='my_form'):
    # Поля для ввода
    name = st.text_input(label='Имя')
    age = st.number_input(label='Возраст', min_value=0)
    submit_button = st.form_submit_button(label='Отправить')

# Отображение результатов
if submit_button:
    st.write(f'Ведено имя- {name}, введен возраст {age}')