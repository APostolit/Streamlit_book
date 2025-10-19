import streamlit as st
from streamlit_product_card import product_card

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Каталог", # Текст на вкладке браузера
    page_icon='🛒',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="expanded",  # Развернуть боковую панель
)

def card11():
    product = product_card(
        product_name="Элегантные часы",
        description="Неподвластная времени вещь для повседневной жизни",
        price="₽980.00",
        product_image="https://img.joomcdn.net/0c90b3764f7c60956d6f01618020a9702f74b67b_original.jpeg",
        picture_position="top",
        image_aspect_ratio="16/9",
    )
    return product

def card12():
    product = product_card(
        product_name="Элегантные часы",
        description="VA VA VOOM Часы механические, мужские, спортивные",
        price="₽2700.",
        product_image="https://img.joomcdn.net/ab2ccc5aef25698bea24a34df6fb2ef141e822a1_1024_1024.jpeg",
        picture_position="top",
        image_aspect_ratio="16/9",
    )
    return product

def card13():
    product = product_card(
        product_name="Элегантные часы",
        description="Модные мужские часы с автоматическим механизмом, водонепроницаемые",
        price="₽3700.00",
        product_image="https://img.joomcdn.net/b577ed1923c5b7154927fe8756a39f532c600650_1024_1024.jpeg",
        picture_position="top",
        image_aspect_ratio="16/9",
    )
    return product

def card21():
    product = product_card(
        product_name="Элегантные часы",
        description="WINNER Стимпанк модные треугольные золотые скелетоны,  лучший бренд класса люкс",
        price="₽2150.00",
        product_image="https://upload.joomcdn.net/44a274ed1d4f67853cf3b9dceab4ec60c293557b_original.jpeg",
        picture_position="top",
        image_aspect_ratio="16/9",
    )
    return product

def card22():
    product = product_card(
        product_name="Элегантные часы",
        description="Мужские механические наручные часы T-winner с календарём, на ремешке из нержавеющей стали",
        price="₽2120.00",
        product_image="https://img.joomcdn.net/76fdfe398f51f01926dea5fa92f4749e61311cc5_original.jpeg",
        picture_position="top",
        image_aspect_ratio="16/9",
    )
    return product

def card23():
    product = product_card(
        product_name="Элегантные часы",
        description="Мужские полностью автоматические механические часы, водонепроницаемые, светящиеся",
        price="₽4600.00",
        product_image="https://img.joomcdn.net/db6360ea92df118e5b1e3c79b68d00fc8d4a38cf_1024_1024.jpeg",
        picture_position="top",
        image_aspect_ratio="16/9",
    )
    return product

# Боковая панель
with st.sidebar:
    # Раскрывающийся список
    add_selectbox = st.sidebar.selectbox(
        "Как поддерживать обратную связь?",
        ("По Email", "По телефону", "По мобильному тел.")
    )

    # Радиокнопки
    with st.sidebar:
        add_radio = st.radio(
            "Выберите способ доставки",
            ("Стандартная (5-15 дней)", "Быстрая (2-3 дня)")
        )

# Текст по центру страницы
st.columns(3)[1].header("🛒 Каталог")
# Текст с начала страницы
st.text("Добро пожаловать на страницу каталога")

# Контейнер
cont = st.container()
with cont:
    # Колонки контейнера
    row11, row12, row13 = st.columns(3, border=True)
    row21, row22, row23 = st.columns(3, border=True)

# Заполнение строк данными
with row11:
    card11()
with row12:
    card12()
with row13:
    card13()
with row21:
    card21()
with row22:
    card22()
with row23:
    card23()

