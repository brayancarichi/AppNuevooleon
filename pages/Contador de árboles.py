import streamlit as st


st.set_page_config(page_title='Contador de árboles')

df = st.file_uploader(label='Sube tu archivo en formato tif')