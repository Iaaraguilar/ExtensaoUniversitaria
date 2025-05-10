import streamlit as st

st.set_page_config(page_title="Sobre", layout="wide")

# Aplica o CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Título e subtítulo
st.markdown('<h1 class="animado">Pontos Viciados de Lixo em São Paulo</h1>', unsafe_allow_html=True)


st.markdown('<h4 class="sub">Mapeamento e Tipos de Resíduos</h4>', unsafe_allow_html=True)

# Imagem e resumo lado a lado
col1, col2 = st.columns([3, 1])  # 3 partes para texto, 1 parte para imagem (ajuste conforme preferir)

with col1:
    # Texto à esquerda
    st.markdown("""
    <h5 class="paragrafo">
    A cidade de São Paulo produz por dia 20 mil toneladas de resíduos sólidos, segundo dados da prefeitura paulistana.
    Resíduos sólidos são todos os produtos não aproveitados das atividades humanas (domésticas, comerciais, industriais e de serviços de saúde) ou aqueles gerados pela natureza, como folhas, galhos, terra, areia, que são retirados das ruas e logradouros pela operação de varrição e enviados para os locais de destinação ou tratamento.
    </h5>
    <h5 class="paragrafo">
    Desse total, 12 mil toneladas (mais de 60%) são geradas pelos domicílios. Outras 8 mil toneladas de resíduos são resultado da varrição de ruas.
    </h5>
    <h5 class="paragrafo">
    Cada um dos 11,452 milhões de habitantes (Censo IBGE 2022) da capital paulista produz, em média, pouco mais de 1 quilograma de resíduos sólidos diariamente. Isso gera um gasto de R$ 2 bilhões para dar o destino certo a todo esse lixo.
    </h5>
    <h5 class="paragrafo">
    São reciclados menos de 3% do total de resíduos sólidos produzidos na cidade de São Paulo.
    </h5>
    """, unsafe_allow_html=True)

with col2:
    # Imagem à direita
    st.image("foto4.jpeg", width=500)  # Ajuste o tamanho da imagem conforme necessário
