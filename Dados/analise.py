import streamlit as st
import pandas as pd
import plotly
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Dashboard do Limpa Brasil!', page_icon='🗑️', layout='wide')

df = pd.read_excel('planilha_tratada_oficial.xlsx')

st.sidebar.header('Personalize em')

# Filtro de Subprefeitura
subprefeitura = st.sidebar.multiselect(
    'Subprefeituras',
    options=df['Subprefeitura'].unique(),
    default=df['Subprefeitura'].unique(),
    key='subprefeitura'
)

# Filtro de Empresa Contratada
empresa = st.sidebar.multiselect(
    'Empresas',
    options=df['Contratada'].unique(),
    default=df['Contratada'].unique(),
    key='empresa'
)

quadrimestre = st.sidebar.multiselect(
    'Quadrimestre',
    options=df['Quadrimestre'].unique(),
    default=df['Quadrimestre'].unique(),
    key='quadrimestre'
)

df_selecao = df.query('Subprefeitura in @subprefeitura and Contratada in @empresa and Quadrimestre in @quadrimestre')

def home():
    st.title('Pontos Viciados de Lixo')

    volume_total = df['Volume_int'].sum()
    
    dic_subprefeitura_count = list(dict(df['Subprefeitura'].value_counts()))
    subprefeitura_com_mais_pontos = dic_subprefeitura_count[0]

    dic_empresas_count = list(dict(df['Contratada'].value_counts()))
    empresa_mais_contratada = dic_empresas_count[0]

    metrica1, metrica2, metrica3 = st.columns(3)

    with metrica1:
        st.metric('Volume Total (m³)', value=int(volume_total))
    with metrica2:
        st.metric('Subprefeitura com Mais Pontos', value=subprefeitura_com_mais_pontos)
    with metrica3:
        st.metric('Empresa mais Contratada', value=empresa_mais_contratada)

    st.markdown('---')

def graphs():
    fig_map = st.map(
        df_selecao,
        latitude='Lat',
        longitude='Long',
    )

    # fig_linha = st.line_chart(
    #     df_selecao.sum(numeric_only=True),
    #     x='Subprefeitura',
    #     y='Volume_int',
    #     color='Ano'
    # )

    fig1 = st.columns(1)

    with fig1:
        st.plotly_chart(fig_map, use_container_width=True)
    # with fig2:
    #     st.plotly_chart(fig_linha, use_container_width=True)

def side_bar():
    with st.sidebar:
        selecionado = option_menu(
            menu_title='Menu',
            options=['Home', 'Gráficos'],
            default_index=0
        )

    if selecionado == 'Home':
        home()
        graphs()
    elif selecionado == 'Gráficos':
        graphs()
    
side_bar()