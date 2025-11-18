from datetime import datetime
from datetime import time
import pandas as pd
import streamlit as st

# Скрыть боковую панель
st.set_page_config(initial_sidebar_state="collapsed")

st.markdown("#### Конфигуратор для колонок даты и времени")

# Набор данных
data_df = pd.DataFrame(
    {
        "Лекции": [
            datetime(2025, 2, 5, 8, 00),
            datetime(2025, 2, 6, 9, 45),
            datetime(2025, 2, 7, 11, 30),],
        "Праздники": [
            datetime(2025, 2, 23),
            datetime(2025, 3, 8),
            datetime(2025, 5, 1)],
        "Время": [
            time(8, 00),
            time(13, 00),
            time(18, 00),],
    }
)

# Конфигуратор колонок
col_config = {
        "Лекции": st.column_config.DatetimeColumn(
            label="Начало лекций ✍",
            min_value=datetime(2025, 2, 1),
            max_value=datetime(2025, 6, 5),
            format="D MMM YYYY, h:mm a ✍",
            step=60,),
        "Праздники": st.column_config.DateColumn(
        label="Праздники 🎇",
        format="D MMM YYYY",),
        "Время": st.column_config.TimeColumn(
        label="Время приема пищи",
        format="HH:mm 👩🏻‍🍳",),
    }

# Таблица с данными
st.data_editor(
    data_df,
    column_config=col_config,
    hide_index=True,
)