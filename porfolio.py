import streamlit as st
from PIL import Image


st.set_page_config(page_title="Portfólio Valdir", layout="wide")

# 1. INJEÇÃO DE CSS PERSONALIZADO 
st.markdown("""
<style>
    .title {
        font-size: 120px;
        font-weight: bold;
        color: #2c3e50;
    }
    .subtitle {
        font-size: 20px;
        color: #7f8c8d;
    }
    
    /* 🎯 CÓDIGO PARA CENTRALIZAR O BLOCO DE TÍTULO 🎯 */
    .header-container {
        display: flex; /* Habilita o layout flexível */
        justify-content: center; /* Centraliza horizontalmente o conteúdo */
        align-items: center; /* Alinha o ícone e o texto verticalmente */
        width: 100%;
    }
    
    /* Estilo do Título Principal */
    .title-h1 {
        font-size: 90px;
        font-weight: bold;
        color: #2c3e50;
        margin: 0; /* Remove margens extras do h1 */
    }
</style>
""", unsafe_allow_html=True)


# 2. CABEÇALHO COM IMAGEM INLINE E CENTRALIZADA
st.markdown(
    """
    <div class="header-container">
        <img src="Taleh azul 3D ícone.png" 
             alt="Ícone Taleh" 
             width="90" 
             height="90" 
             style="vertical-align: middle; margin-right: 20px;">
        <h1 class="title-h1">
            Taleh Soluções Tecnológicas - Portfólio de Projetos
        </h1>
    </div>
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
