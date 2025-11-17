import streamlit as st
from PIL import Image

st.set_page_config(page_title="Portfólio Valdir", layout="wide")

# Cabeçalho
st.markdown("""
<style>
    .title {
        font-size: 48px;
        font-weight: bold;
        color: #2c3e50;
    }
    .subtitle {
        font-size: 20px;
        color: #7f8c8d;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.title {
    font-size: 200px;
    font-weight: bold;
    color: #2c3e50;
    text-align: center;
    margin-bottom: 20px;
}
</style>
<p class="title">👨‍💻 Portfólio de Projetos</p>
""", unsafe_allow_html=True)

st.markdown('<p class="subtitle">Bem-vindo! Explore meus projetos em IA, Streamlit, análise de dados e mais.</p>', unsafe_allow_html=True)

st.divider()

# Lista de projetos
projetos = [
    {
        "nome": "🔍 Classificador de Vidraria",
        "descricao": "Modelo de IA treinado para identificar tipos de vidraria com base em características visuais.",
        "imagem": "vidros.png",
        "link": "https://appartigos.streamlit.app/"
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
**Contato:** [LinkedIn](https://www.linkedin.com/in/valdir-albino-wallauer-11682376/) | [GitHub](https://github.com/VAW1970)  
**Tecnologias:** Python · Streamlit · LangChain · Groq · Pandas · Scikit-learn · Git
""")
