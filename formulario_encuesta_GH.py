import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Configuración visual
st.set_page_config(page_title="Evaluación BEPENSA", page_icon="🧠", layout="centered")

# Fondo negro y estilo general
st.markdown(
    """
    <style>
    body {background-color: black; color: white;}
    .stApp {background-color: black;}
    h1, h2, h3, label, p, div, span {color: white !important;}
    .stRadio > label {color: white !important;}
    .stButton > button {
        background-color: #E63946;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        height: 3em;
        width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Archivo CSV
RESPUESTAS_FILE = "respuestas.csv"
if not os.path.exists(RESPUESTAS_FILE):
    pd.DataFrame(columns=["timestamp", "p1", "p2", "p3", "p4", "p5"]).to_csv(RESPUESTAS_FILE, index=False)

# Logo
st.image("logo.png", width=300)
st.title("🧠 Evaluación de Proyectos - BEPENSA")

preguntas = [
    "¿El equipo comunica con claridad los objetivos, la problemática que atiende y la propuesta de valor del proyecto?",
    "¿La presentación demuestra con datos y métricas concretas el impacto alcanzado o esperado del proyecto?",
    "¿El proyecto propone ideas innovadoras y se alinea con los pilares de GROWTH (Global, Rebalance, Our People, Value, The Coca-Cola Company)?",
    "¿El proyecto demuestra ser factible con los recursos disponibles y presenta un plan realista para su continuidad o expansión?",
    "¿Se evidencia un trabajo colaborativo entre distintas áreas y un impacto positivo en las personas o cultura organizacional?",
]

# Estado de envío
if "submitted" not in st.session_state:
    st.session_state.submitted = False

if not st.session_state.submitted:
    st.markdown("Selecciona una calificación del **1 al 5** para cada pregunta:")

    respuestas = []
    for i, pregunta in enumerate(preguntas):
        valor = st.radio(
            f"{i+1}. {pregunta}",
            options=[1, 2, 3, 4, 5],
            horizontal=True,
            key=f"p{i+1}",
        )
        respuestas.append(valor)

    if st.button("Enviar respuesta ✅"):
        df = pd.read_csv(RESPUESTAS_FILE)
        nueva = pd.DataFrame([[datetime.now()] + respuestas],
                             columns=["timestamp", "p1", "p2", "p3", "p4", "p5"])
        df = pd.concat([df, nueva], ignore_index=True)
        df.to_csv(RESPUESTAS_FILE, index=False)
        st.session_state.submitted = True
        st.rerun()
else:
    st.success("🎉 ¡Gracias por tu respuesta!")
    st.info("Tu opinión es muy valiosa para el equipo.")
