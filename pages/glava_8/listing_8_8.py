import streamlit as st
import graphviz

# Скрыть боковую панель
st.set_page_config(initial_sidebar_state="collapsed")

st.write('Графы с элементом st.graphviz_chart')

# Граф - родственники, как объект
graph = graphviz.Digraph()
graph.edge("Я", "Мать")
graph.edge("Я", "Отец")
graph.edge("Брат", "Мать")
graph.edge("Брат", "Отец")
graph.edge("Мать", "Бабушка по матери")
graph.edge("Мать", "Дедушка по матери")
graph.edge("Отец", "Бабушка по отцу")
graph.edge("Отец", "Дедушка по отцу")
graph.edge("Сестра", "Бабушка по матери")
graph.edge("Сестра", "Бабушка по отцу")

# Вкладки страницы приложения
tab1, tab2 = st.tabs(["Граф 1", "Граф 2"])

with tab1:
    st.write('Родственники')
    st.graphviz_chart(graph)

with tab2:
    st.write('Кольцевой маршрут автобуса')
    # Граф кольцевой маршрут, как текстовая строка
    st.graphviz_chart('''
        digraph {
            Вокзал -> Магазин
            Аптека -> Вокзал
            Магазин -> Рынок            
            Рынок -> Стадион
            Стадион -> Школа
            Школа -> Магазин
            Магазин -> Аптека                
        }
    ''')