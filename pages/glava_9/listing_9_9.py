import streamlit as st
import pandas as pd

# Скрыть боковую панель
st.set_page_config(initial_sidebar_state="collapsed")

# Набор данных
data_df = pd.DataFrame(
    {
        "json": [
            {"Напитки": ["Молоко", "Квас", "Лимонад"]},
            {"Фрукты": [ "Яблоки", "Груши", "Мандарины"]},
            {"Овощи": [ "Лук", "Морковь", "Капуста",]}
        ],
        "Продажи": [
            [10, 14, 26, 80, 90, 40],
            [10, 20, 80, 80, 70, 10],
            [10, 10, 20, 90, 30,50]
        ],
        "Сайты": [
            "https://dzen.ru",
            "https://google.com",
            "https://mail.ru",
        ],
        "img": [
            "https://storage.googleapis.com/s4a-prod-share-preview/default/"
            "st_app_screenshot_image/5435b8cb-6c6c-490b-9608-799b543655d3/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/"
            "st_app_screenshot_image/ef9a7627-13f2-47e5-8f65-3f69bb38a5c2/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/"
            "st_app_screenshot_image/31b99099-8eae-4ff8-aa89-042895ed3843/Home_Page.png",
        ],
    }
)

# Конфигуратор колонок
conf = {
        "json": st.column_config.JsonColumn(
            label="Данные JSON",
            help="Данные формата JSON",
            width="medium",),
        "Продажи": st.column_config.ListColumn(
            label="Продажи (список)",
            help="Продажи за последние 6 месяцев",
            width="medium",),
        "Сайты": st.column_config.LinkColumn(
            label="Сайты",
            help="Ссылки на сайты",
        ),
        "img": st.column_config.ImageColumn(
            label="Изображения",
            help="Скриншоты приложений Streamlit"
        )
        }

st.markdown("## Таблица с данными объектов")
# Таблица с данными
st.data_editor(
    data_df,
    column_config=conf,
    hide_index=True)