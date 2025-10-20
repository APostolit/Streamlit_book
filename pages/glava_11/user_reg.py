import streamlit as st
import hashlib

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Регистрация", # Текст на вкладке браузера
    page_icon='👨',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Свернуть боковую панель
)

# Получить БД из сессии
sql_bd = st.session_state['sql_bd']

# Зашифровать пароль
def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

# Регистрация пользователя
st.subheader("👨Создать аккаунт")
cont = st.container(border=True, width=300)
with cont:
    new_user = st.text_input('🙎🏻‍♂️Входное имя')
    new_passwd = st.text_input('🔐Пароль', type='password')
    new_email = st.text_input('📬email')
    btn = st.button('╰┈➤Создать')

if btn:
    con_bd = sql_bd.connect_to_db()  # Открыть соединение с БД
    # Проверить есть ли такой пользователь
    sql = 'SELECT *, count(*) FROM Users WHERE email=?'
    res = sql_bd.select_rec_p(con_bd, sql, new_email)
    count = res[0][3]  # Количество записей в БД
    if count >= 1:
        bd_user = res[0][0]
        bd_email = res[0][2]
        if bd_email == new_email:
            st.warning('Пользователь с таким email уже зарегистрирован',
                       icon="⚠️", width=300)
    else:
        data = [new_user, make_hashes(new_passwd),new_email]
        sql_add = 'INSERT INTO Users(username,password,email) VALUES (?,?,?)'
        # Добавить запись в БД
        res = sql_bd.insert_rec(con_bd, sql_add, data)
        if res == 'ok':
            st.success("Аккаунт создан. Войдите в систему через меню -'Вход'",
                       icon="👌", width=400)
        else:
            st.error('Ошибка при добавлении записи в БД',
                     icon="🚨", width=300)
    con_bd.close()  # Закрыть соединение