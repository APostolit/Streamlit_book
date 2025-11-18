import base64
import streamlit as st

# Задать имя PDF файла
pdf_file = 'pdf/Python_vsem.pdf'

# Открыть PDF файл
with open(pdf_file, "rb") as f:
    base64_pdf = base64.b64encode(f.read()).decode('utf-8')

# Создать объект для вывода в HTML
pdf_d = f'<embed src="data:application/pdf;base64,{base64_pdf}"' \
        f' width="1000" height="800" type="application/pdf">'

st.subheader(":blue[Содержимое PDF файла с оглавлением]")

# Отобразить содержимое PDF файла
st.markdown(body=pdf_d, unsafe_allow_html=True)
