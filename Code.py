import streamlit as st
import datetime
from PIL import Image

st.set_page_config(page_title="Feliz Aniversário!", page_icon="🎂", layout="centered")

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

st.markdown("""
    <div class='mensagem'>
        Desejo que seu aniversário seja repleto de sorrisos, 
        abraços e muitas comemorações. Que este novo ciclo venha acompanhado de muita paz, 
        saúde e realizações. Aproveite o seu dia! 
    </div>
""", unsafe_allow_html=True)

if st.button("Clique aqui para uma surpresa!"):
    st.balloons()
    st.success("Que o seu ano seja incrível! ✨")
