import streamlit as st

@st.cache_resource
def init_connection():
    host = "hh-pgsql-public.ebi.ac.uk"
    database = "my_bd"
    user = "reader"
    password = "my_pass"
    return psycopg2.connect(host=host, database=database, user=user, password=password)

conn = init_connection()
