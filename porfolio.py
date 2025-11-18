import streamlit as st
from PIL import Image


# 1. CONFIGURAÇÕES DA PÁGINA
st.set_page_config(page_title="Portfólio Valdir", layout="wide")

# 2. INJEÇÃO DE CSS PERSONALIZADO (Definição de Estilos)
st.markdown("""
<style>
    /* Estilo para o TÍTULO PRINCIPAL */
    .title-h1 {
        font-size: 90px;
        font-weight: bold;
        color: #2c3e50;
        text-align: center;
        margin-top: 0px; /* Para ficar próximo ao ícone */
    }
    
    /* Estilos outros */
    .title {
        font-size: 120px;
        font-weight: bold;
        color: #2c3e50;
    }
    .subtitle {
        font-size: 20px;
        color: #7f8c8d;
    }
</style>
""", unsafe_allow_html=True)


# 3. CABEÇALHO COM ÍCONE (CENTRALIZAÇÃO)
# Usando colunas para centralizar o ícone de forma confiável
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Coloca a imagem na coluna central
    st.image("Taleh azul 3D ícone.png", width=128)

# 4. TÍTULO CENTRALIZADO (Aplicando o Estilo)
# Aplicamos o CSS personalizado na tag <h1>
st.markdown(
    """
    <h1 class="title-h1">
        Taleh Soluções Tecnológicas - Portfólio de Projetos
    </h1>
    """, 
    unsafe_allow_html=True
)

st.markdown('<p class="subtitle">Bem-vindo! Explore meus projetos em IA, Streamlit, análise de dados e mais.</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Com mais de 35 anos de atuação em indústrias químicas, estou em transição para o universo da tecnologia, aplicando minha bagagem técnica em soluções digitais com IA e automação..</p>', unsafe_allow_html=True)

st.divider()

# Lista de projetos
projetos = [
    {
        "nome": "🔍 Classificador de Vidraria",
        "descricao": "Modelo de IA treinado para identificar tipos de vidraria com base em características visuais.",
        "imagem": "vidros.png",
        "link": "https://labglassware.streamlit.app/"
    },
    {
        "nome": "📚 Analisador de Artigos",
        "descricao": "App que usa LLMs para resumir e interpretar artigos científicos com LangChain e Groq.",
        "imagem": "artigos.png",
        "link": "https://appartigos.streamlit.app/"
    },
    {
        "nome": "🧪 Gerenciador de Reagentes",
        "descricao": "App para gerenciar reagentes químicos controlando validades e localização (User/Test#2025).",
        "imagem": "reagentes.png",
        "link": "https://vaw.pythonanywhere.com/"
    }
]

# Exibição em colunas
cols = st.columns(3)
for i, projeto in enumerate(projetos):
    with cols[i]:
        st.image(projeto["imagem"], use_column_width=True)
        st.markdown(f"### {projeto['nome']}")
        st.markdown(f"<div style='min-height:80px'>{projeto['descricao']}</div>", unsafe_allow_html=True)
        st.markdown(f"[▶️ Abrir App]({projeto['link']})", unsafe_allow_html=True)

st.divider()

# Rodapé
st.markdown("""
**Contato:** [LinkedIn](https://www.linkedin.com/in/valdir-albino-wallauer-11682376/) | [GitHub](https://github.com/VAW1970) | 
**Tecnologias:** Python · Streamlit · LangChain · Groq · Pandas · Scikit-learn · Git
""")
