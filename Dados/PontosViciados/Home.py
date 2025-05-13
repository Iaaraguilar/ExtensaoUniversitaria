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

  <h5 class="paragrafo">
    ▻ A capital paulista é responsável pela produção diária de 20 mil toneladas de resíduos sólidos, segundo dados da Prefeitura de São Paulo¹;<br>
    ▻ Desse total, 12 mil toneladas (mais de 60%) de resíduos sólidos são geradas pelos domicílios paulistanos;<br> 
    ▻ Outras 8 mil toneladas de lixo são provenientes da varrição de ruas;<br>
    ▻ Cada um dos 11,452 milhões de habitantes (Censo IBGE 2022²) da cidade produz, em média, pouco mais de 1kg de resíduos sólidos por dia;<br>
    ▻ São Paulo gasta todos os anos mais de R$ 2 bilhões para dar o destino certo a todo esse lixo;<br>
    ▻ Menos de 3% do total dos resíduos sólidos produzidos na cidade são reciclados.      
  </h5>
<div style="display: flex; justify-content: center; gap: 20px; margin: 30px 0;">
    <img src="https://imprensa.prefeitura.sp.gov.br/imgcache/thumb3350781148.jpg" alt="Ilustração de resíduos" width="400">
    <img src="https://www.nossasaopaulo.org.br/wp-content/uploads/2014/07/centraltriagem1.jpg" alt="Ilustração de resíduos" width="400">
  </div>

  <h5 class="paragrafo">
    Este estudo visa analisar a base de dados sobre pontos viciados de descarte irregular, produzida pela Prefeitura de São Paulo, a pedido da Limpa Brasil, uma organização não governamental especializada no acesso a informações públicas. 
  </h5>

  <h5 class="paragrafo">
    Alguns resultados apontaram o volume total de lixo de 35.302 m³ de resíduos sólidos urbanos descartados de maneira irregular em pontos viciados nos logradouros da cidade de São Paulo.
  </h5>

  <h5 class="paragrafo">
    Também obtivemos outro insight: a Subprefeitura Sé é a que tem mais pontos viciados de descarte de lixo sólido da cidade. Do total de 13.966 pontos de descarte irregular de resíduos sólidos na cidade de São Paulo, a Subprefeitura Sé registrou 1.822 pontos (13% do total).
  </h5>

  <h5 class="paragrafo">
    Em segundo lugar, aparece a Subprefeitura São Mateus com 1.458 pontos (10%) de descarte irregular de resíduos sólidos. A Subprefeitura do Itaim Paulista ficou em terceiro lugar no ranking, com 1.174 (8%) ocorrências identificadas pela Prefeitura de São Paulo.
  </h5>

  <h5 class="paragrafo">
    As Subprefeituras de Jaçanã/Tremembé registraram o menor número de denúncias, com 22 pontos viciados cada uma (0,5% do total).
    <br><br>
    A empresa Corpus Saneamento e Obras foi a que mais vezes prestou serviço de coleta desses resíduos. A companhia ficou responsável por cuidar de um total de 3.892 locais.
  </h5>

  <div style="text-align: center; margin-top: 10px; margin-bottom: 20px;">
    <img src="https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQYjGc7zc5MMdPnEl-ngCJS6WKXjtFcICjslFQUgVtwnN8ZU6O9" alt="Ilustração de resíduos" width="600">
  </div>
</section>
            



<div style="text-align: left; font-size: 0.85em; margin-left: 20px;">
    <h6>Referências</h6>
  <ul style="list-style: none; padding-left: 0;">
    <li>1 <a href="https://capital.sp.gov.br/web/spregula/w/residuos_solidos/residuos_solidos/229517" target="_blank">
        Prefeitura de São Paulo – Resíduos Sólidos</a></li>
    <li>2 <a href="https://www.ibge.gov.br/cidades-e-estados/sp/sao-paulo.html" target="_blank">
        IBGE – Perfil dos municípios: São Paulo</a></li>
    <li>3 <a href="https://www.tce.sp.gov.br/6524-relatorio-tcesp-mostra-panorama-gestao-residuos-solidos#:~:text=09%2F03%2F2021%20%E2%80%93%20S%C3%83O,e%20a%20maior%20taxa%20nacional." target="_blank">
        Tribunal de Contas do Estado de São Paulo</a></li>
     <li>4<a href="https://www.prefeitura.sp.gov.br/cidade/secretarias/upload/servicos/arquivos/PGIRS-2014.pdf" target="_blank">
       Plano de Gestão Integrada de Resíduos Sólidos - PGIRS da Cidade de São Paulo</a></li>        
  </ul>
</div>


<hr>



<p class="rodape">
  Desenvolvido por Davi, Gabryell, Gustavo, Iara e Julio. <br>
  © 2025 - Uso educativo.
</p>
""", unsafe_allow_html=True)