import streamlit as st

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 6", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

# Текст по центру страницы
st.columns(3)[1].header("👩🏻‍💻Примеры главы 6")

# Контейнер
cont_1 = st.container(width=300)
with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги главы 6",
        ("Листинг 6.1", "Листинг 6.2", "Листинг 6.3", "Листинг 6.4",
         "Листинг 6.5", "Листинг 6.6", "Листинг 6.7"),
        index=None,
        placeholder="Выберите листинг..."
    )

# Контейнер
cont_2 = st.container()
with cont_2:
    if options is None:
        st.write('Листинг не выбран')
    elif options == "Листинг 6.1":
        st.write('Код листинга 6.1 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st

            # Кнопка
            bt = st.button("Выдать сообщения")
            if bt:
                st.success('Загрузка данных выполнена успешно!',
                           icon="✅",
                           width=400)
                st.info('Приветствуем вас на странице академии Python',
                        icon="ℹ️", width=400)
                st.warning('Внимание, данные будут удалены',
                           icon="⚠️",
                           width=300)
                st.error('Ошибка выполнения программы!',
                         icon="🚨",
                         width=300)
                e = RuntimeError("Это исключение типа RuntimeError")
                st.exception(e, width=300)
    elif options == "Листинг 6.2":
        st.write('Код листинга 6.2 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st
            import time

            bt = st.button("Старт загрузки данных")
            if bt:
                progress_text = "Данные загружаются. Ждите..."
                # Индикатор процесса
                my_bar = st.progress(0, text=progress_text)
                for percent in range(100):
                    time.sleep(0.04)
                    my_bar.progress(percent + 1, text=progress_text + str(percent))
                time.sleep(1)
                my_bar.empty()
    elif options == "Листинг 6.3":
        st.write('Код листинга 6.2 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st
            import time

            bt = st.button("Загрузка данных")
            if bt:
                with st.spinner("Ждите ...", show_time=True, width=400):
                    time.sleep(5)
                st.success("Загрузка данных выполнена успешно!", width=400)
    elif options == "Листинг 6.4":
        st.write('Код листинга 6.4 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st
            import time
            import numpy as np
            from numpy.random import default_rng as rng

            # Первый элемент st.status
            st_1 = st.status("Ждите, идет формирование графика...")
            with st_1:
                time.sleep(3)
                st.line_chart(np.random.randn(20, 3))
                st_1.update(
                    label="Формирование графика завершено!",
                    state="complete",
                    expanded=False)

            # Второй элемент st.status
            with st.status("Ждите, идет загрузка данных...", expanded=True) as status:
                # Набор данных DataFrame
                df = rng(0).standard_normal((5, 1))
                time.sleep(2)

                status.update(label="Ждите, идет формирование таблицы...!")
                time.sleep(5)

                # Две колонки с указанием ширины
                col1, col2 = st.columns([1, 3], border=True)
                # Вставить график в 1-ю колонку
                col1.subheader("Таблица с данными")
                col1.write(df)

                # Вставить данные во 2-ю колонку
                status.update(label="Ждите, идет формирование графика...!")
                time.sleep(5)
                col2.subheader("График")
                col2.line_chart(df)
                status.update(label="Все элементы загружены!")
                time.sleep(5)

                status.update(
                    label="Загрузка данных завершена!",
                    state="complete",
                    expanded=True
                )

            st.button("Обновить")
    elif options == "Листинг 6.5":
        st.write('Код листинга 6.5 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st

            bt1 = st.button('Вывод сообщения 1')
            if bt1:
                st.toast('Ваши данные успешно сохранены!', icon='😍')

            bt2 = st.button('Вывод сообщения 2')
            if bt2:
                st.toast('Данные загружены!', icon=":material/thumb_up:")

            bt3 = st.button('Вывод сообщения 3')
            if bt3:
                st.toast('Сбой загрузки через API!', icon=":material/thumb_down:")

            bt4 = st.button('Вывод сообщения 4')
            if bt4:
                st.toast('Процесс завершился успешно!!!', icon='🎉')
    elif options == "Листинг 6.6":
        st.write('Код листинга 6.6 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st

            bt = st.button('Запустить шары!')
            if bt:
                st.balloons()
    elif options == "Листинг 6.7":
        st.write('Код листинга 6.7 и результаты его выполнения')
        with st.echo(code_location="above"):
            import streamlit as st

            bt = st.button('Запустить снегопад!')
            if bt:
                st.snow()
