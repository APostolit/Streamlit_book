import pandas as pd
import streamlit as st

# Скрыть боковую панель
st.set_page_config(initial_sidebar_state="collapsed")

st.markdown("#### Конфигуратор колонок для текстовых и числовых данных")

# Набор данных
data_df = pd.DataFrame(
    {
        "Конфеты": ["Белочка", "Мишка на севере", "Трюфели", "Ласточка"],
        "Упаковка": ["На вес", "На вес", "Коробка", "На вес"],
        "Вес": [200, 400, 800, 1000],
        "Цена": [200, 400, 250, 600],
    }
)

# Конфигуратор колонок
col_config = {
        "Конфеты": st.column_config.Column(
            label="Сорта конфет",
            help="Введите сорт конфет",
            width="medium",
            required=True,
        ),
        "Упаковка": st.column_config.TextColumn(
            label="Вид упаковки",
            help="Как упакованы",
            width="small",
            required=True,
        ),
        "Вес": st.column_config.NumberColumn(
            label="Вес (гр.)",
            help="Введите вес",
            width="small",
            required=True,
        ),
        "Цена": st.column_config.NumberColumn(
            label="Цена (руб.)",
            help="Укажите цену",
            width="small",
            required=True,
            format="₽%d"
        )
    }

# Таблица с данными
st.data_editor(data_df,
               column_config=col_config,
               hide_index=True,
               num_rows="dynamic",)