import streamlit as st
import datetime
from PIL import Image

# Configuração da página
st.set_page_config(page_title="Feliz Aniversário!", page_icon="🎂", layout="centered")

# Estilização básica com CSS
st.markdown("""
    <style>
        .titulo {
            text-align: center;
            color: #FF1493;
            font-size: 3rem;
            font-weight: bold;
        }
        .mensagem {
            text-align: center;
            font-size: 1.2rem;
            color: #333333;
            padding: 20px;
            background-color: #FFF0F5;
            border-radius: 10px;
        }
        .stButton>button {
            background-color: #FF1493;
            color: white;
            font-size: 18px;
            border-radius: 10px;
            padding: 10px 24px;
        }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho
st.markdown("<h1 class='titulo'>🎉 Parabéns! 🎂</h1>", unsafe_allow_html=True)

# Mensagem principal
st.markdown("""
    <div class='mensagem'>
        Hoje é um dia super especial! Desejo que seu aniversário seja repleto de sorrisos, 
        abraços e muitas comemorações. Que este novo ciclo venha acompanhado de muita paz, 
        saúde e realizações. Aproveite o seu dia! 💖
    </div>
""", unsafe_allow_html=True)

# Efeito de confetes (ocorre quando o botão é clicado)
if st.button("Clique aqui para uma surpresa!"):
    st.balloons()
    st.success("Que o seu ano seja incrível! ✨")

# Seção interativa de recados
st.write("---")
st.subheader("Deixe uma mensagem para o aniversariante:")

with st.form("form_recado"):
    remetente = st.text_input("Seu nome:")
    texto_recado = st.text_area("Escreva sua mensagem:")
    enviado = st.form_submit_button("Enviar Recado")

if enviado:
    if remetente and texto_recado:
        st.success(f"Mensagem enviada com sucesso por {remetente}! 💌")
        # Aqui você poderia salvar a mensagem em um banco de dados ou arquivo de texto
        with st.expander("Ver recado enviado"):
            st.write(f"**De:** {remetente}")
            st.write(f"**Mensagem:** {texto_recado}")
    else:
        st.warning("Por favor, preencha o seu nome e a mensagem!")
