import streamlit as st
import urllib.parse

# 1. Configuración de la pestaña con tu logo
st.set_page_config(
    page_title="Presupuestador DL Fotografía", 
    page_icon="logo.png",
    layout="centered"
)

# 2. Tu Logo de DL Fotografía y Video
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("logo.png", use_container_width=True)

# --- SECCIÓN 1: CALENDARIO (PRIMERO) ---
st.divider()
st.subheader("📅 Disponibilidad de Fechas")
st.write("Consultá si tu fecha está libre antes de cotizar:")
calendar_url = "https://calendar.google.com/calendar/embed?src=goliat4750%40gmail.com&ctz=America%2FArgentina%2FCordoba"
st.components.v1.iframe(calendar_url, height=500, scrolling=True)

# --- SECCIÓN 2: CALCULADORA ---
st.divider()
st.subheader("📊 Calculadora de Presupuestos")

SERVICIOS = {
    "Sesión Retrato/Bebé (2hs)": {"base": 40000, "con_drone": 40000, "desc": "50-70 fotos digitales."},
    "Evento 15/18 años": {"base": 230000, "con_drone": 300000, "desc": "6hs de cobertura, +100 fotos y 1 video."},
    "Boda Completa": {"base": 300000, "con_drone": 370000, "desc": "Civil, Iglesia y Fiesta. +200 fotos y 2 videos."},
    "Bautismo (Iglesia + Fiesta)": {"base": 230000, "con_drone": 230000, "desc": "+100 fotos y 1 video."},
    "Evento (Solo Fotos)": {"base": 180000, "con_drone": 180000, "desc": "Cobertura fotográfica profesional."}
}

servicio_nom = st.selectbox("Seleccione el servicio:", list(SERVICIOS.keys()))
con_drone = st.checkbox("¿Incluir servicio de Drone (4K)?")
distancia = st.number_input("KM fuera de Albardón (ida y vuelta):", min_value=0, step=2)

datos = SERVICIOS[servicio_nom]
precio_base = datos["con_drone"] if con_drone else datos["base"]
detalles = datos["desc"]
viaticos = (distancia / 2) * 1000
total_final = precio_base + viaticos

st.metric(label="Presupuesto Estimado", value=f"${total_final:,.0f}")
st.write(f"**Incluye:** {detalles}")

# --- SECCIÓN 3: CONTACTO ---
mi_numero = "5492645164757" 
texto_mensaje = f"Hola Diego! Coticé un servicio de {servicio_nom}. El total es ${total_final:,.0f}. ¿Tenés disponibilidad?"
mensaje_url = urllib.parse.quote(texto_mensaje)
link_whatsapp = f"https://wa.me/{mi_numero}?text={mensaje_url}"

st.write("---")
st.link_button("📱 Consultar disponibilidad por WhatsApp", link_whatsapp, use_container_width=True)
