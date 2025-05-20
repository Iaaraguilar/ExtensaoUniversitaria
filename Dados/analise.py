import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Dashboard do Limpa Brasil!', page_icon='🚮', layout='wide')

df = pd.read_excel('planilha_tratada_oficialmente_oficial.xlsx')

with st.sidebar:
    # Menu
    selecionado = option_menu(
        menu_title='Menu',
        options=['Pontos Viciados de Lixo', 'Tipos de Resíduos de Lixo', 'Saiba Mais'],
        default_index=0
    )

    # Filtro de Ano
    ano = st.sidebar.multiselect(
        'Ano',
        options=df['Ano'].unique(),
        default=df['Ano'].unique(),
        key='ano'
    )

    # Filtro de zona
    zona = st.sidebar.multiselect(
        'Zona',
        options=df['Zona'].unique(),
        default=df['Zona'].unique(),
        key='zona'
    )

df_selecao = df.query('Ano in @ano and Zona in @zona')

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
        st.warning("Mapa: mostrando uma amostra de 300 pontos para melhor desempenho.")
    else:
        df_plot = df_selecao

    df_plot['Volume_categoria'] = df_plot['Volume_int'].astype(str)
    df_selecao['Volume_categoria'] = df_selecao['Volume_int'].astype(str)

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
        zoom=3,
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

    df_filtrado = df_selecao[df_selecao['Ano'].isin([2019, 2020, 2021])]

    df_filtrado['Zona'] = df_filtrado['Subprefeitura']

    fig_bar = px.bar(
        df_filtrado.groupby('Subprefeitura')['Volume_int'].sum().reset_index(),
        x='Subprefeitura',
        y='Volume_int',
        height=700,
        color='Subprefeitura',
        title='Volume Total de Lixo',
        subtitle='Por Subprefeitura',
        labels={
            'Volume_int': 'Volume (m³)'
        },
        color_discrete_sequence=['#FF4B4B', '#E3B23C', '#EDEBD7', '#03CEA4']
    )

    fig_area = px.bar(
        df_filtrado.groupby('Subprefeitura')['Volume_int'].count().reset_index(),
        x='Subprefeitura',
        y='Volume_int',
        height=500,
        color='Subprefeitura',
        title='Pontos Viciados de Lixo',
        subtitle='Por Subprefeitura'
    )

    fig_pie = px.pie(
        df_filtrado, 
        values="Volume_int", 
        names="Contratada", 
        title="Volume total por empresa por volume(m³)", 
        labels= {'Volume_int': "Volume (m³)", "Contratada": "Empresa"},
        color= 'Contratada'
        )

    # pontos / subprefeitura

    st.plotly_chart(fig_map, use_container_width=True)
    st.plotly_chart(fig_bar, use_container_width=True)
    st.plotly_chart(fig_area, use_container_width=True)
    st.plotly_chart(fig_pie, use_container_width=True)

def saiba():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Título e subtítulo
    st.markdown('<h1 class="animado"> Pontos viciados de lixo em São Paulo</h1>', unsafe_allow_html=True)
    st.markdown('<h4 class="sub">Análise dos resíduos sólidos na capital</h4>', unsafe_allow_html=True)

    # Conteúdo principal
    st.markdown("""
    <section class="conteudo">
    <h5 class="paragrafo">
        Pontos viciados de descarte irregular de resíduos sólidos são logradouros públicos onde a população deposita aleatoriamente o lixo proveniente das atividades humanas (domésticas, comerciais, industriais e de serviços de saúde) ou aqueles gerados pela natureza, como folhas, galhos, terra, areia.
    </h5>
    <br>
    <h5 class="paragrafo">
        🗑️  São Paulo produz 20 mil toneladas de lixo por dia;<br>
                <br>
        🏠  A maior parte (12 mil toneladas) vem das residências;<br> 
                <br>
        🧹  8 mil toneladas são da varrição das ruas;<br>
                <br>
        👤  Cada morador produz, em média, mais de 1 kg de lixo por dia;<br>
                <br>
        💸  São gastos mais de R$ 2 bilhões por ano com o lixo;<br>
                <br>
        ♻️  Menos de 3% do lixo é reciclado    
    </h5>
    <div style="display: flex; justify-content: center; gap: 20px; margin: 30px 0;">
        <img src="https://imprensa.prefeitura.sp.gov.br/imgcache/thumb3350781148.jpg" alt="Ilustração de resíduos" width="400">
        <img src="https://www.nossasaopaulo.org.br/wp-content/uploads/2014/07/centraltriagem1.jpg" alt="Ilustração de resíduos" width="400">
    </div>

    



    <hr>



    <p class="rodape">
    Desenvolvido por Davi, Gabryell, Gustavo, Iara e Julio. <br>
    © 2025 - Uso educativo.
    </p>
    """, unsafe_allow_html=True)

def side_bar():
    if selecionado == 'Pontos Viciados de Lixo':
        home()
        graphs()

    elif selecionado == 'Tipos de Resíduos de Lixo':
        graphs()

    elif selecionado == 'Saiba Mais':
        saiba()
    
side_bar()
