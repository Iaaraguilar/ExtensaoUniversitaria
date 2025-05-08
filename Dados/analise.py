import streamlit as st
import pandas as pd
import plotly
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Dashboard do Limpa Brasil!', page_icon='🗑️', layout='wide')

df = pd.read_excel('planilha_tratada.xlsx')

st.sidebar.header('Personalize em')

# Filtro de Subprefeitura
subprefeitura = st.sidebar.multiselect(
    'Subprefeituras',
    options=df['Subprefeitura'].unique(),
    default=df['Subprefeitura'].unique(),
    key='subprefeitura'
)