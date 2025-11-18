import pandas as pd
import streamlit as st

# Скрыть боковую панель
st.set_page_config(initial_sidebar_state="collapsed")

st.markdown("#### Конфигуратор для колонок выбора")

# Набор данных
data_df = pd.DataFrame(
    {
        "Конфеты": ["Белочка", "Мишка на севере", "Трюфели", "Ласточка"],
        "Включить": [True, False, False, True],
        "Упаковка": ["На вес⚖️", "На вес⚖️", "Коробка🍫", "На вес⚖️"],
        "Вес": [200, 400, 800, 1000],
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
    "Включить": st.column_config.CheckboxColumn(
            label="Включить в набор?",
            help="Выберите любимые конфеты 🤎",
            default=False,
        ),
        "Упаковка": st.column_config.SelectboxColumn(
            label="Упаковка",
            help="Выбор типа упаковки",
            width="medium",
            options=["На вес⚖️", "Коробка🍫",],
            required=True,
        ),
        "Вес": st.column_config.NumberColumn(
            label="Вес (гр.)",
            help="Введите вес",
            width="small",
            required=True,
        ),
    }

# Таблица с данными
st.data_editor(data_df,
               column_config=col_config,
               hide_index=True,
               num_rows="dynamic",)