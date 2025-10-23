import streamlit as st
import pandas as pd
import os
import time

st.set_page_config(page_title="Contador BEPENSA", page_icon="🧮", layout="centered")

# Fondo negro y estilos
st.markdown(
    """
    <style>
    body {background-color: black; color: white;}
    .stApp {background-color: black;}
    h1, h2, h3, p, div, span {color: white !important;}
    .stButton > button {
        background-color: #E63946;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.5em 1.5em;
        border: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.image("logo.png", width=300)
st.title("🧮 Contador de Respuestas")

RESPUESTAS_FILE = "respuestas.csv"
placeholder = st.empty()

# Campo de contraseña para acceso administrativo
admin_pass = st.sidebar.text_input("Contraseña de administrador", type="password")

# Mostrar botón de reinicio si la contraseña es correcta
if admin_pass == "bepensa2025":
    if st.sidebar.button("Reiniciar contador 🧹"):
        pd.DataFrame(columns=["timestamp", "p1", "p2", "p3", "p4", "p5"]).to_csv(RESPUESTAS_FILE, index=False)
        st.sidebar.success("¡Contador reiniciado!")
        time.sleep(1)
        st.rerun()

# Refrescar en bucle
while True:
    if os.path.exists(RESPUESTAS_FILE):
        try:
            df = pd.read_csv(RESPUESTAS_FILE)
            total = len(df)
        except pd.errors.EmptyDataError:
            total = 0
    else:
        total = 0

    with placeholder.container():
        st.markdown(
            f"<h1 style='text-align:center; font-size:120px; color:#E63946;'>{total}</h1>",
            unsafe_allow_html=True
        )
        st.markdown("<h3 style='text-align:center;'>Respuestas registradas</h3>", unsafe_allow_html=True)

    time.sleep(3)
    st.rerun()