import streamlit as st
import hashlib

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Вход", # Текст на вкладке браузера
    page_icon='👨',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Свернуть боковую панель
)

# Зашифровать пароль
def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

st.subheader("🏃‍♂️‍➡️‍🚪Войти в систему")
# Получить БД из сессии
sql_bd = st.session_state['sql_bd']

cont = st.container(border=True, width=300)
with cont:
    username = st.text_input('👨Входное имя')
    password = st.text_input('🔐Пароль', type='password')
    btn = st.button('╰┈➤Войти')
    st.page_link(page="pages/user_reg.py", label="Создать аккаунт", icon="👨🏻‍💼")

if btn:
    con_bd = sql_bd.connect_to_db()  # Открыть соединение с БД
    hashed_pass = make_hashes(password)

    # check = check_hashes(password, hashed_pass)
    data = (username, hashed_pass)
    sql = 'SELECT *, count(*) FROM Users WHERE username =? AND password = ?'
    res = sql_bd.select_rec_pp(con_bd, sql, data)
    bd_user = res[0][0]
    bd_email = res[0][2]
    count = res[0][3]
    if count == 1:
        st.info(bd_user, icon="ℹ️", width=300)
        st.success("Вы успешно вошли в систему!", icon="👌", width=300)
        # Сохранить объект БД в сессии
        st.session_state['user_name'] = bd_user
        st.session_state['legal'] = True
        #  Перейти на главную страницу
        st.switch_page(page="pages/home_reg.py")
    else:
        st.warning('Ошибка в имени или пароли! Такого пользователя нет в системе',
                   icon="⚠️", width=300)
