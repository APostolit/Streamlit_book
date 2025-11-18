import streamlit as st

# Элемент st.badge
st.badge("Бейджик")
st.badge("Завершено успешно", icon=":material/check:", color="green")

# Несколько значков рядом
st.markdown(
    ":violet-badge[:material/star: Лучший фильм] :orange-badge[⚠️ Внимание]"
    " :material/chronic: :gray-badge[На обсуждении]"
)
st.divider()  # Разделитель

# Элемент st.caption
st.caption("Это строка с примером текста мелким шрифтом.")
st.caption("Это строка с текстом _italics_ :blue[синего цвета] и с эмодзи :sunglasses:")
st.divider() # Разделитель

# Элемент st.code
code = '''
def hello():
    print("Привет Streamlit!")
    for i range(10):
        print('Шаг цикла-", i)
'''
st.code(code, language="python", line_numbers=True)
st.divider()  # Разделитель

# Элемент st.echo (программный код после результатов его выполнения)
with st.echo(code_location="below"):
    st.write('Вывод текстовой строки на страницу приложения')
st.divider()

# Элемент st.echo (программный код перед результатами его выполнения)
with st.echo(code_location="above"):
    # Содержимое этого блока, будет как выведено на экране, так и выполнено
    def get_user_name(code_location="above" or "below"):
        return 'Виктор!'

    greeting = "Приветствую тебя, "
    value = get_user_name()
    st.write(greeting, value)
st.divider()  # Разделитель

go = 'Продолжение программы'
st.write(go)
st.divider()  # Разделитель

# Элемент st.echo
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')
st.divider()  # Разделитель

# Элемент st.text
st.text("Это первая строка текста.\n [Это вторая строка, ](продолжение второй строки).")