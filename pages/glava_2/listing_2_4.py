import streamlit as st

# Элементы title
st.title("Заголовок страницы")
st.title("_Заголовок курсив с иконкой_ :sunglasses:")
st.title(":blue[Заголовок цветной]")

# Элементы header
st.header("_Заголовок курсив_ :blue[цветной] с иконкой :sunglasses:")
st.header("Заголовок с серым разделителем", divider="gray")
st.header("Заголовки динамичными разделителями")
st.header("Заголовок 1", divider=True)
st.header("Заголовок 2", divider=True)
st.header("Заголовок 3", divider=True)

# Элементы subheader
st.subheader("_Подзаголовок курсив_ :blue[цветной] с иконкой :sunglasses:")
st.subheader("Подзаголовок в серым разделителем", divider="gray")
st.subheader("Подзаголовки динамичными разделителями")
st.subheader("Подзаголовок 1", divider=True)
st.subheader("Подзаголовок 2", divider=True)
st.subheader("Подзаголовок 3", divider=True)

# Элементы markdown
st.markdown("*Streamlit* действительно **'крутой'** ***Фреймворк!!!***.")

st.markdown('''
    :red[Streamlit] :orange[может] :green[выводить] :blue[текст] :violet[в]
    :gray[различных] :rainbow[цветах] и :blue-background[выделять цветным фоном].''')

st.markdown("А это букет из иконок &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''Если вы в коде перенесли часть текста на новую строку,
то она будет показана одной строкой.

Для разделения текста между строками можно добавить пустую строку.
'''
st.markdown(multi)

# Текст мелким шрифтом
st.markdown(':small[Текст мелким шрифтом]')