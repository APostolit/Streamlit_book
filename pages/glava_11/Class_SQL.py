import sqlite3 as sl

#########################
# Класс для работы с БД #
#########################
class Sql_meneg(object):
    def __init__(self, name_bd, sql):
        self.name_bd = name_bd
        self.sql = sql

    # Функция - метод подключения к БД
    def connect_to_db(self):
        try:
            conn = sl.connect(self.name_bd)  # подключиться к БД
            return conn  # вернуть подключение к БД
        except sl.Error as error:
            print('Ошибка при подключении к БД-', error)

    # Функция - метод создание таблицы БД
    def create_table(self, conn, create_table_sql):
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
            conn.commit()
        except sl.Error as error:
            print('Ошибка при создании таблицы-', error)

    # Функция - метод добавления или обновления записи в таблице
    def in_or_up(self, conn, sql, data):
        ok = None
        try:
            cur = conn.cursor()
            cur.execute(sql, data)
            conn.commit()
            cur.close()
            ok = 'ok'
        except sl.Error as error:
            # print('Ошибка при добавлении записи в таблицу-', error)
            ok = error
        return ok

    # Функция - метод вставки записи в таблицу
    def insert_rec(self, conn, sql, data):
        ok = None
        try:
            cur = conn.cursor()
            cur.execute(sql, data)
            conn.commit()
            cur.close()
            ok = 'ok'
        except sl.Error as error:
            # print('Ошибка при добавлении записи в таблицу-', error)
            ok = error
        return ok

    # Функция - метод добавления записи в таблицу
    def add_rec(self, conn, sql, data):
        ok = None
        try:
            cur = conn.cursor()
            cur.execute(sql, data)
            conn.commit()
            cur.close()
            ok = 'ok'
        except sl.Error as error:
            # print('Ошибка при добавлении записи в таблицу-', error)
            ok = error
        return ok

    # Функция - метод выборки записей все
    def select_rec_all(self, conn, sql):
        try:
            cur = conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
            cur.close()
            return rows
        except sl.Error as error:
            # print('select_rec_all Ошибка при выборке записей из таблицы-', error)
            ok = error
            return ok

    # Функция - метод выборки записей с параметром
    def select_rec_p(self, conn, sql, data):
        try:
            cur = conn.cursor()
            cur.execute(sql, [data])
            rows = cur.fetchall()
            cur.close()
            return rows
        except sl.Error as error:
            # print('select_rec_p Ошибка при выборке записи из таблицы-', error)
            ok = error
            return ok

    # Функция - метод выборки записей с параметрами
    def select_rec_pp(self, conn, sql, data):
        try:
            cur = conn.cursor()
            cur.execute(sql, data)
            rows = cur.fetchall()
            cur.close()
            return rows
        except sl.Error as error:
            # print('select_rec_p Ошибка при выборке записи из таблицы-', error)
            ok = error
            return ok

    # Функция - метод удаления записи из таблицы
    def delete_rec(self, conn, sql, id):
        try:
            with conn:
                cursor = conn.cursor()
                cursor.execute(sql, [id])
                conn.commit()
                cursor.close()
                ok = 'ok'
        except sl.Error as error:
            # print('Ошибка при удалении записи из таблицы-', error)
            ok = error
        return ok

    # Функция - метод обновление таблицы с записями
    def update_rec(self, conn, sql, data):
        try:
            with conn:
                cursor = conn.cursor()
                cursor.execute(sql, data)
                conn.commit()
                cursor.close()
                ok = 'ok'
        except sl.Error as error:
            # print('Ошибка при обновлении записи в таблице-', error)
            ok = error
        return ok

    # Функция - метод создать представление
    def create_view(self, conn, sql):
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            ok = 'ok'
        except sl.Error as error:
            # print('Ошибка при создании представления-', error)
            ok = error
        return ok

    # Функция - метод очистить таблицу БД
    def clear_tabl(self, conn, sql):
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            ok = 'ok'
        except sl.Error as error:
            # print('Ошибка при очистке таблицы-', error)
            ok = error
        return ok


if __name__ == "__main__":
    name_bd = 'my-test.db'            # задать имя БД
    sql = ''                          # создать пустой запрос к БД
    sql_bd = Sql_meneg(name_bd, sql)  # создать объект БД
    con_bd = sql_bd.connect_to_db()   # создать подключение к БД

    # создание таблицы методом create_table
    sql_cr_tab = """CREATE TABLE IF NOT EXISTS PPP(
    id_ppp INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
    ppp1 TEXT,
    ppp2 TEXT,
    ppp3 TEXT);"""
    sql_bd.create_table(con_bd, sql_cr_tab)

    # вставить запись в таблицу
    p1 = 5
    p2 = '55555555555555555555555'
    data = [p1, p2]
    # print(data)
    sql_ins = '''INSERT INTO PPP (Номер, Вопрос) VALUES (?,?)'''  # Запрос, если вставлять списком
    # sql_ins = '''INSERT INTO PPP (ppp) VALUES('Строка');'''  # Запрос, если вставлять в поле
    # sql_bd.insert_rec(con_bd, sql_ins, data)  # Запрос, если вставлять из объекта

    # выбрать все записи из таблицы
    sql_sel_all = 'SELECT * FROM PPP'  # Запрос, если выбирать все записи
    ppp = sql_bd.select_rec_all(con_bd, sql_sel_all)
    # print(ppp)
    # выбрать конкретную запись из таблицы
    p = 1
    sql_p = 'SELECT * FROM PPP WHERE id_ppp=?'  # если выбирать из переменной (одну запись)
    ppp1 = sql_bd.select_rec_p(con_bd, sql_p, p)
    # print(ppp1)

    # удалить записи из таблицы
    pd = 5
    sql_del = """DELETE FROM PPP WHERE id_ppp=?"""
    # sql_bd.delete_rec(con_bd, sql_del, pd)

    # обновить записи в таблице
    id = 1
    p1 = 'Привет'
    p2 = 'Старое'
    p3 = 'Самое то'
    data_up = (p1, p2, p3, id)
    sql_up = "UPDATE PPP SET ppp1=?, ppp2=?, ppp3=? WHERE id_ppp= ?"
    # sql_bd.update_rec(con_bd, sql_up, data_up)

    con_bd.close()  # закрыть соединение

