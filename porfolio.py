import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="Portfólio Valdir", layout="wide")

# Nome do arquivo na raiz
FILENAME = "Taleh azul 3D ícone.png"  

# Verifica se arquivo existe na raiz
if not os.path.exists(FILENAME):
    st.error(f"Imagem não encontrada na raiz: '{FILENAME}'. Verifique nome e capitalização.")
else:
    # CSS para o título
    st.markdown("""
    <style>
    .title-h1 {
        font-size: 90px;
        font-weight: bold;
        color: #2c3e50;
        margin: 0;
    }
    .subtitle {
        font-size: 20px;
        color: #7f8c8d;
        margin-top: 6px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Layout centralizado com ícone à esquerda do texto
    left, center, right = st.columns([1, 3, 1])
    with center:
        col_img, col_txt = st.columns([1, 6], gap="small")
        with col_img:
            img = Image.open(FILENAME)
            st.image(img, width=90)
        with col_txt:
            st.markdown(f'<h1 class="title-h1">Taleh Soluções Tecnológicas - Portfólio de Projetos</h1>', unsafe_allow_html=True)
            st.markdown(f'<div class="subtitle">Bem-vindo! Explore meus projetos em IA, Streamlit e automação laboratoriais.</div>', unsafe_allow_html=True)
            
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
