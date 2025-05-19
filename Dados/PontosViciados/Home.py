import streamlit as st

st.set_page_config(page_title="Sobre", layout="wide")

# Aplica o CSS
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