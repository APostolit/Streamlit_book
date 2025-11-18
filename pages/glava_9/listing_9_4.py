import streamlit as st

# Скрыть боковую панель
st.set_page_config(initial_sidebar_state="collapsed")

# Данные:
current_sales = 15000
previous_sales = 12000
sklad = 50
sale = 45
# Рассчитать разницу
delta_sales = current_sales - previous_sales
percentage_change = (delta_sales / previous_sales) * 100
ostat = sklad - sale
delta_kol =  ostat - sklad

st.markdown("## Элементы st.metric")

# Отобразить метрики
st.markdown("#### Динамика продаж")
st.metric(label="Абсолютные продажи",
          value=f"Р{current_sales}",
          delta=f"Р{delta_sales}",
          delta_color="normal")
st.metric(label="Процент изменения",
          value=f"{percentage_change:.2f}%",
          delta=f"{percentage_change:.2f}%",
          delta_color="normal",
          width='content',
          border=True)
st.metric(label="Остаток на складе",
          value=f"{ostat}",
          delta=f"{delta_kol}",
          delta_color="normal")

st.markdown("## Элементы st.metric в колонках")
col1, col2, col3 = st.columns(3)
col1.metric("Температура", "25 °C", "3 °C", border=True)
col2.metric("Ветер", "4 м/с", "-8%", border=True)
col3.metric("Влажность", "75%", "4%", border=True)