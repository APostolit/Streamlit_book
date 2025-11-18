import streamlit as st

# Скрыть боковую панель
st.set_page_config(initial_sidebar_state="collapsed")

st.markdown("#### Элемент st.html")

st.html("<h1><span style='color:blue;'>Заголовок H1 (синим цветом)</span></h1>")
st.html("<style> h1 {color: red;}</style>"
        "<body><h1>Заголовок H1 красным цветом</h1></body>")