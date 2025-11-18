import streamlit as st
from numpy.random import default_rng as rng

st.text('Элемент st.tabs')

st.text('Изображения')
tab1, tab2, tab3, tab4 = st.tabs(["Кошка", "Собака", "Сова", "Python"])
# Вкладки созданные с использованием with
with tab1:
    st.header("Кошка")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
with tab2:
    st.header("Собака")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
    st.header("Сова")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=300)
with tab4:
    st.header("Академия Python")
    st.image("AP_400.png", width=300)

st.text('Данные Pandas')
df = rng(0).standard_normal((5, 1))

tab5, tab6 = st.tabs(["📈 График", "🗃 Данные"], width=400)
# Вкладки созданные с использованием метода объектов
tab5.subheader("Вкладка с графиком")
tab5.line_chart(df)

tab6.subheader("Вкладка с данными")
tab6.write(df)