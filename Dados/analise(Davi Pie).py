import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Dashboard do Limpa Brasil!', page_icon='🚮', layout='wide')

df = pd.read_excel('planilha_tratada_oficial.xlsx')

st.sidebar.header('Personalize sua visualização')

# Filtro de Ano
ano = st.sidebar.multiselect(
    'Ano',
    options=df['Ano'].unique(),
    default=df['Ano'].unique(),
    key='ano'
)

# Filtro de Quadrimestre
quadrimestre = st.sidebar.multiselect(
    'Quadrimestre',
    options=df['Quadrimestre'].unique(),
    default=df['Quadrimestre'].unique(),
    key='quadrimestre'
)

# Filtro de Empresa Contratada
empresa = st.sidebar.multiselect(
    'Empresas',
    options=df['Contratada'].unique(),
    default=df['Contratada'].unique(),
    key='empresa'
)


df_selecao = df.query('Ano in @ano and Contratada in @empresa and Quadrimestre in @quadrimestre')

def home():
    st.title('🗑️ Pontos Viciados de Lixo')

    volume_total = df['Volume_int'].sum()
    
    dic_subprefeitura_count = dict(df['Subprefeitura'].value_counts())
    list_subprefeitura_count = list(dic_subprefeitura_count)
    subprefeitura_com_mais_pontos = list_subprefeitura_count[0]

    dic_empresas_count = list(dict(df['Contratada'].value_counts()))
    empresa_mais_contratada = dic_empresas_count[0]

    metrica1, metrica2, metrica3 = st.columns(3)

    with metrica1:
        st.metric('🎚️ Volume Total (m³)', value=f'{int(volume_total)} m³')
    with metrica2:
        st.metric('🗾 Subprefeitura com Mais Pontos', value=f'{subprefeitura_com_mais_pontos} - {dic_subprefeitura_count['SÉ']} pontos')
    with metrica3:
        st.metric('🏭 Empresa mais Contratada', value=empresa_mais_contratada)

    st.markdown('---')

def graphs():
    if len(df_selecao) > 300:
        df_plot = df_selecao.sample(300, random_state=42)
        st.warning("Mostrando uma amostra de 300 pontos para melhor desempenho.")
    else:
        df_plot = df_selecao

    df_plot['Volume_categoria'] = df_plot['Volume_int'].astype(str)

    fig_map = px.scatter_map(
        df_plot,
        lat='Lat',
        lon='Long',
        color='Volume_categoria',
        color_discrete_map= {
            '1': '#FFDEDE',
            '3': '#FF8585',
            '5': '#FF4B4B',
        },
        category_orders={
            'Volume_categoria': ['1', '3', '5']
        },
        size='Volume_int',
        hover_name='Endereço',
        hover_data=['Lat', 'Long', 'Volume_categoria'],
        zoom=10,
        height=700,
        title='Mapeamento de Pontos Viciados de Lixo',
        subtitle='Na Cidade de São Paulo',
        labels={
            'Lat': 'Latitude',
            'Long': 'Longitude',
            'Volume_categoria': 'Volume (m³)',
        },
        map_style='carto-darkmatter'
    )

    # fig_map.update_layout(mapbox_style='open-street-map')
    # fig_map.update_layout(margin={'r':0,'t':0,'l':0,'b':0})

    fig_bar = px.bar(
        df_selecao.groupby(['Subprefeitura', 'Ano'])['Volume_int'].sum().reset_index(),
        x='Ano',
        y='Volume_int',
        height=700,
        barmode='group',
        color='Subprefeitura',
        title='Volume Total de Lixo',
        subtitle='Por Subprefeitura',
        labels={
            'Volume_int': 'Volume (m³)',
        }
    )
    
    # Usar volume int e contratada de cada empresa
    df_empresa_grafico = df.groupby("Contratada", as_index=False)["Volume_int"].sum()
    
    fig_pie = px.pie(
        df_empresa_grafico, 
        values="Volume_int", 
        names="Contratada", 
        title="Volume total por empresa por volume(m³)", 
        labels= {'Volume_int': "Volume (m³)", "Contratada": "Empresa"},
        color= 'Contratada'
        )

    st.plotly_chart(fig_map, use_container_width=True)
    st.plotly_chart(fig_bar, use_container_width=True)
    st.plotly_chart(fig_pie, use_container_width=True)

def side_bar():
    with st.sidebar:
        selecionado = option_menu(
            menu_title='Menu',
            options=['Pontos Viciados de Lixo', 'Tipos de Resíduos de Lixo'],
            default_index=0
        )

    if selecionado == 'Pontos Viciados de Lixo':
        home()
        graphs()
    elif selecionado == 'Tipos de Resíduos de Lixo':
        graphs()
    


side_bar()

## SABER PONTOS REVITALIZADOS

## SABER PONTOS ELIMINADOS