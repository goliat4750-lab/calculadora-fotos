import streamlit as st
import urllib.parse

# 1. Configuración de la pestaña
st.set_page_config(
    page_title="Presupuestador DL Fotografía", 
    page_icon="logo.png",
    layout="centered"
)

# 2. Tu Logo de DL Fotografía y Video
try:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("logo.png", use_container_width=True)
except:
    st.title("DL Fotografía y Video")

# --- SECCIÓN 1: CALENDARIO ---
st.divider()
st.subheader("📅 Disponibilidad de Fechas")
st.write("Consultá si tu fecha está libre antes de cotizar:")
calendar_url = "https://calendar.google.com/calendar/embed?src=goliat4750%40gmail.com&ctz=America%2FArgentina%2FCordoba"
st.components.v1.iframe(calendar_url, height=500, scrolling=True)

# --- SECCIÓN 2: CALCULADORA ---
st.divider()
st.subheader("📊 Cotizá tu Servicio")

# Diccionario de Servicios
SERVICIOS = {
    "Sesión Retrato/Bebé (2hs)": {"base": 40000, "con_drone": 40000, "desc": "50-70 fotos digitales."},
    "Evento 15/18 años": {"base": 230000, "con_drone": 300000, "desc": "6hs de cobertura, +100 fotos y 1 video."},
    "Boda Completa": {"base": 300000, "con_drone": 370000, "desc": "Civil, Iglesia y Fiesta. +200 fotos y 2 videos."},
    "Bautismo (Iglesia + Fiesta)": {"base": 230000, "con_drone": 230000, "desc": "+100 fotos y 1 video."},
    "Evento (Solo Fotos)": {"base": 180000, "con_drone": 180000, "desc": "Cobertura fotográfica profesional."}
}

# Distancias de IDA desde Albardón (Aproximadas)
DEPARTAMENTOS = {
    "Albardón": 0,
    "Capital": 15,
    "Chimbas": 8,
    "Santa Lucía": 18,
    "Rivadavia": 20,
    "Rawson": 22,
    "Pocito": 30,
    "Caucete": 35,
    "Angaco": 10,
    "San Martín": 18,
    "9 de Julio": 23,
    "Ullum": 20,
    "Zonda": 25,
    "Sarmiento": 45,
    "25 de Mayo": 40,
    "Jáchal": 150,
    "Iglesia": 170,
    "Calingasta": 180,
    "Valle Fértil": 250
}

# Selección del Usuario
servicio_nom = st.selectbox("¿Qué tipo de servicio buscás?", list(SERVICIOS.keys()))
con_drone = st.checkbox("¿Querés incluir tomas con Drone 4K? 🚁")
lugar_evento = st.selectbox("¿En qué departamento es el evento?", list(DEPARTAMENTOS.keys()))

# Lógica "bajo la manga" (Solo IDA)
datos = SERVICIOS[servicio_nom]
precio_base = datos["con_drone"] if con_drone else datos["base"]
km_ida = DEPARTAMENTOS[lugar_evento]
viaticos = km_ida * 1000 # $1000 por km de ida
total_final = precio_base + viaticos

# Mostrar resultado
st.info(f"**Servicio:** {servicio_nom}")
st.write(f"📍 Destino: {lugar_evento}")
st.metric(label="Presupuesto Estimado", value=f"${total_final:,.0f}")
st.caption("Nota: El presupuesto es una estimación base.")

# --- SECCIÓN 3: CONTACTO ---
mi_numero = "5492645164757" 
texto_mensaje = f"Hola Diego! Coticé un servicio de {servicio_nom} en {lugar_evento}. El total es ${total_final:,.0f}. ¿Tenés la fecha disponible?"
mensaje_url = urllib.parse.quote(texto_mensaje)
link_whatsapp = f"https://wa.me/{mi_numero}?text={mensaje_url}"

st.write("---")
st.link_button("📱 Consultar por WhatsApp", link_whatsapp, use_container_width=True)
