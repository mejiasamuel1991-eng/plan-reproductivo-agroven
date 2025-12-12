import streamlit as st
import os

print("--- INICIO DIAGNÓSTICO DE SECRETOS ---")

# Intento 1: Leer desde st.secrets
try:
    key = st.secrets["GOOGLE_API_KEY"]
    # MOSTRAR SOLO LOS PRIMEROS 4 CARACTERES POR SEGURIDAD
    masked_key = key[:4] + "..." + key[-4:]
    print(f"✅ ÉXITO: Clave encontrada en secrets.toml: {masked_key}")
    print(f"Longitud de la clave: {len(key)} caracteres")
except Exception as e:
    print(f"❌ FALLO: No se pudo leer st.secrets: {e}")

# Verificación de archivo físico
if os.path.exists(".streamlit/secrets.toml"):
    print("✅ El archivo .streamlit/secrets.toml EXISTE físicamente.")
else:
    print("❌ ALERTA: El archivo .streamlit/secrets.toml NO EXISTE o no se encuentra.")

print("--- FIN DIAGNÓSTICO ---")
