import streamlit as st
import pandas as pd
import numpy as np
import funciones_app
import math

st.title('Metodos Numericos')

col1, col2= st.columns([1,1])

with col1:
    error = st.selectbox(
    "Quieres utilizar Cifras Significativas o Decimales Correctos?",
    ("Decimales Correctos", "Cifras Significatias"),
)

with col2:
    decimals = st.number_input(f'Ingrese el número de {error}', min_value=1, max_value=10, value=3)

if error == "Decimales Correctos":
    tol = 0.5 * 10 ** (-decimals)
else:
    tol = 10 ** (-decimals)

method = st.selectbox(
"Que metodo quieres utilizar?",
("Biseccion", "Regla Falsa", "Secante", "Newton", "Punto Fijo", "Raices Multiples 2"),)

methods = {
    "Biseccion": funciones_app.biseccion_app,
    "Regla Falsa": funciones_app.regla_falsa_app,
    "Secante": funciones_app.secante_app,
    "Newton": funciones_app.newton_app,
    "Punto Fijo": funciones_app.punto_fijo_app,
    "Raices Multiples 2":funciones_app.raices_multiples2_app,
}
if method in ["Biseccion", "Regla Falsa", "Secante", "Punto Fijo"]:
    cols = st.columns([1,1,1])
else:
    cols = st.columns([1,1])

methods[method](cols, error,tol)

