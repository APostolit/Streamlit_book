import streamlit as st
import pandas as pd

# Скрыть боковую панель
st.set_page_config(initial_sidebar_state="collapsed")

# Создать dataframe
df = pd.DataFrame({'Годы': ['2018', '2019', '2020', '2021'],
                   'Продажи': [350, 480, 550, 680]}
                  )
# Создать диаграмму
st.write('Линейная диаграмма st.line_chart')
st.line_chart(df, x='Годы', y='Продажи',
              x_label='Годы', y_label='Продажи')