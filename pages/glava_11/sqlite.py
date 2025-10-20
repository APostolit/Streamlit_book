import streamlit as st
from Class_SQL import Sql_meneg

# Создать подключение к БД через st.secrets["connections"]
name_bd = st.secrets["connections"]["url"]
# name_bd = st.secrets.connections.url
sql = ''  # создать пустой запрос к БД
sql_bd = Sql_meneg(name_bd, sql)  # создать объект БД
con_bd = sql_bd.connect_to_db()  # создать подключение к БД

# Создание таблицы методом create_table
# Запрос на создание таблицы
sql_cr_tab = """CREATE TABLE IF NOT EXISTS Table_1(
   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
   field_1 TEXT,
   field_2 TEXT,
   field_3 TEXT);"""
# Выполнить запрос на создание таблицы
sql_bd.create_table(con_bd, sql_cr_tab)

# Вставить запись в таблицу
p1 = 'Значение в поле 1'
p2 = 'Значение в поле 2'
p3 = 'Значение в поле 3'
data_add = [p1, p2, p3]

# Запрос на добавление записи
sql_ins = '''INSERT INTO Table_1 (field_1, field_2, field_3) VALUES (?,?,?)'''
# Выполнить запрос на добавление записи
sql_bd.insert_rec(con_bd, sql_ins, data_add)

# Выбрать все записи из таблицы (запрос)
sql_sel_all = 'SELECT * FROM Table_1'
# Выполнить запрос на получение данных
data = sql_bd.select_rec_all(con_bd, sql_sel_all)
my-test.db
# Конфигуратор колонок таблицы
column_config={
    "0": "🔑ID записи в БД",
    "1": st.column_config.TextColumn(label="Колонка 1👇"),
    "2": st.column_config.TextColumn(label="Колонка 2👇"),
    "3": st.column_config.TextColumn(label="Колонка 3👇")
}
# Заголовок таблицы
st.markdown('##### ⛁ Таблица из из базы данных SQLite ')
# Отображение таблицы
st.dataframe(data, column_config=column_config)
