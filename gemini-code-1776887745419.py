import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Calculadora DL Fotografía", page_icon="📸")

st.title("📸 Cotizador DL Fotografía y Video")
st.write("Calcula el presupuesto para tu evento de forma inmediata.")

# --- ENTRADAS DE USUARIO ---
tipo_evento = st.selectbox("Selecciona el tipo de evento:", ["15 Años", "Boda", "Sesión Urbana"])
quiere_drone = st.radio("¿Deseas incluir servicio de Drone? (Potensic Atom 2)", ["No", "Sí"])

# --- LÓGICA DE PRECIOS (Actualizados) ---
if tipo_evento == "15 Años":
    precio_base = 250000
elif tipo_evento == "Boda":
    precio_base = 280000 # Un estimado, puedes cambiarlo
else:
    precio_base = 60000 # Sesión urbana

# Ajuste por Drone
if quiere_drone == "Sí":
    total_calculado = 300000 if tipo_evento == "15 Años" else precio_base + 50000
else:
    total_calculado = precio_base

# --- MOSTRAR RESULTADO ---
st.markdown("---")
st.subheader("Presupuesto Estimado")
st.write(f"El valor total del servicio es: **${total_calculado:,}**")

# --- TU NUEVA CLÁUSULA DE INFLACIÓN ---
st.warning(
    "⚠️ **Nota sobre aranceles:** Los valores expresados en este presupuesto se mantienen vigentes "
    "hasta el **31 de mayo de 2026**. Pasada esta fecha, los precios quedan sujetos a reajustes "
    "según la tasa inflacionaria vigente. \n\n"
    "💡 *Recuerda: El precio del servicio se congela únicamente con el pago de la seña.*"
)

st.caption("DL Fotografía y Video | Albardón, San Juan")
