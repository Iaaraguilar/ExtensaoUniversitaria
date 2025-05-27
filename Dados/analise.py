import streamlit as st
import pandas as pd
import plotly.express as px
# import plotly.graph_objects as go
from streamlit_option_menu import option_menu


st.set_page_config(page_title='Dashboard do Limpa Brasil!', page_icon='🚮', layout='wide')

df = pd.read_excel('Dados/planilha_tratada_oficialmente_oficial.xlsx')
df_residuo = pd.read_excel('Dados/residuos_unificado.xlsx')


with st.sidebar:
    # Menu
    selecionado = option_menu(
        menu_title='Menu',
        options=['Pontos Viciados de Lixo', 'Tipos de Resíduos de Lixo', 'Saiba Mais'],
        default_index=0
    )

    
def pontos():
    st.title('🗑️ Pontos Viciados de Lixo')

    volume_total = df['Volume_int'].sum()
    
    dic_subprefeitura_count = dict(df['Subprefeitura'].value_counts())
    list_subprefeitura_count = list(dic_subprefeitura_count)
    subprefeitura_com_mais_pontos = list_subprefeitura_count[0]

    dic_empresas_count = list(dict(df['Contratada'].value_counts()))
    empresa_mais_contratada = dic_empresas_count[0]

    metrica1, metrica2, metrica3 = st.columns(3)

    with metrica1:
        st.metric('🎚️ Volume Total (m³)', value=f'{int(volume_total) // 1000} Km³')
    with metrica2:
        st.metric('🗾 Subprefeitura com Mais Pontos', value=f'{subprefeitura_com_mais_pontos}')
    with metrica3:
        st.metric('🏭 Empresa mais Contratada', value=empresa_mais_contratada)


    # Filtro de Ano
    with st.sidebar:
        ano = st.sidebar.multiselect(
        'Ano',
        options=df['Ano'].unique(),
        default=df['Ano'].unique(),
        key='ano'
        )


    df_plot = df.sample(300, random_state=45)
    df_ano = df_plot.query('Ano in @ano')

    

    df_plot['Volume_categoria'] = df_plot['Volume_int'].astype(str)
    df_ano['Volume_categoria'] = df_ano['Volume_int'].astype(str)

    fig_map = px.scatter_map(
        df_ano,
        lat='Lat',
        lon='Long',
        color='Volume_categoria',
        
        category_orders={
            'Volume_categoria': ['1', '3', '5'],
            'Ano': [2019, 2020, 2021]
        },
        size='Volume_int',
        hover_name='Endereço',
        hover_data=['Lat', 'Long', 'Volume_categoria'],
        zoom=9,
        height=600,
        title='Mapeamento de Pontos Viciados de Lixo',
        subtitle='Na Cidade de São Paulo',
        labels={
            'Lat': 'Latitude',
            'Long': 'Longitude',
            'Volume_categoria': 'Volume (m³)',
        },
        map_style='dark',
        animation_frame='Zona'
    )

    with st.sidebar:
         # Filtro de zona
        zona = st.sidebar.multiselect(
        'Zona',
        options=df['Zona'].unique(),
        default=df['Zona'].unique(),
        key='zona'
        )

    st.warning("Mapa: mostrando uma amostra de 300 pontos para melhor desempenho.")

    df_ano_zona = df.query('Ano in @ano and Zona in @zona')
    df_ano_zona['Volume_categoria'] = df_ano_zona['Volume_int'].astype(str)

    df_filtrado = df_ano_zona[df_ano_zona['Ano'].isin([2019, 2020, 2021])]

    fig_bar = px.bar(
        df_filtrado.groupby(['Subprefeitura', 'Zona'])['Volume_int'].sum().reset_index(),
        x='Volume_int',
        y='Subprefeitura',
        color='Zona',
        height=700,
        title='Volume Total de Lixo',
        subtitle='Por Subprefeitura',
        labels={
            'Volume_int': 'Volume (m³)'
        },
    )

    fig_pie = px.pie(
        df_filtrado, 
        values="Volume_int", 
        names="Contratada", 
        title="Volume Total de Lixo",
        subtitle="Por Empresa",
        labels= {'Volume_int': "Volume (m³)", "Contratada": "Empresa"},
        color= 'Contratada',
        
    )

    fig_hist = px.histogram(
        df_filtrado,
        y='Subprefeitura',
        title='Pontos Viciados',
        subtitle='Por Subprefeitura',
        color='Zona',
        height=700,
        labels= {'count': "Pontos Viciados"},
    )
    
    fig_bar.update_layout(yaxis={'categoryorder': 'total ascending'})
    fig_pie.update_layout(yaxis={'categoryorder': 'total ascending'})
    fig_hist.update_layout(yaxis={'categoryorder': 'total ascending'})

    st.plotly_chart(fig_map, use_container_width=True)
    st.plotly_chart(fig_bar, use_container_width=True)
    st.plotly_chart(fig_pie, use_container_width=True)
    st.plotly_chart(fig_hist, use_container_width=True)

def residuos():
    st.title('☣️ Tipos de resíduos de lixo')

    volume_total = df_residuo['quantidade'].sum()

    tipo_counts = df_residuo['tipo'].value_counts()
    maiores_tipos = tipo_counts.idxmax()

    ano_counts = df_residuo['ano'].value_counts()
    ano_maior = ano_counts.idxmax()

    metrica1, metrica2, metrica3 = st.columns(3)

    with metrica1:
        st.metric('⚖️ Quantidade Total (toneladas)', value=f'{int(volume_total) // 1000000} Mt')
    with metrica2:
        st.metric('🛢️ Maior tipo de lixo', value=maiores_tipos)
    with metrica3:
        st.metric('📅 Ano com mais resíduos', value=ano_maior)

    with st.sidebar:
        ano = st.sidebar.multiselect(
        'ano',
        options=df_residuo['ano'].unique(),
        default=df_residuo['ano'].unique(),
        key='ano'
        )

    df_residuos = df_residuo.query('ano in @ano')

    df_residuos['ano'] = df_residuos['ano'].apply(str)

    fig_bar_residuos = px.bar(
        df_residuos.groupby(['tipo', 'ano'])['quantidade'].sum().reset_index(),
        x='quantidade',
        y='tipo',
        color='ano',
        height=900,
        title='Quantidade de Lixo',
        subtitle='Por Tipo',
        labels={
            'quantidade': 'Quantidade (t)',
            'tipo': 'Tipo de Residuo'
        },
        
    )
    
    ordem_meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

    df_residuos['mes'] = pd.Categorical(df_residuos['mes'], categories=ordem_meses, ordered=True)

    fig_line_residuos = px.line(
        df_residuos.groupby(['ano', 'mes'])['quantidade'].sum().reset_index(),
        x='mes',
        y='quantidade',
        color='ano',
        title='Quantidade de Lixo',
        subtitle='Por Mês',
        
    )

    fig_bar_residuos.update_layout(yaxis={'categoryorder': 'total ascending'})

    st.plotly_chart(fig_bar_residuos, use_container_width=True)
    st.plotly_chart(fig_line_residuos, use_container_width=True)


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
        pontos()

    elif selecionado == 'Tipos de Resíduos de Lixo':
        residuos()

    elif selecionado == 'Saiba Mais':
        saiba()
    
side_bar()
