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
calendar_url = "https://calendar.google.com/calendar/embed?src=goliat4750%40gmail.com&ctz=America%2FArgentina%2FCordoba"
st.components.v1.iframe(calendar_url, height=500, scrolling=True)

# --- SECCIÓN 2: CALCULADORA ---
st.divider()
st.subheader("📊 Cotizá tu Servicio")

# Base de datos de servicios actualizada
SERVICIOS = {
    "Sesión Retrato/Bebé (2hs)": {"base": 40000, "con_drone": 40000, "desc": "50-70 fotos digitales."},
    "Evento 15/18 años": {"base": 230000, "con_drone": 300000, "desc": "6hs de cobertura, +100 fotos y 1 video."},
    "Boda Completa": {"base": 300000, "con_drone": 370000, "desc": "Civil, Iglesia y Fiesta. +200 fotos y 2 videos."},
    "Bautismo (Iglesia + Fiesta)": {"base": 230000, "con_drone": 230000, "desc": "+100 fotos y 1 video."},
    "Video Musical 4K": {"base": 300000, "con_drone": 300000, "desc": "Producción profesional (aprox. 5 min)."},
    "Promo 2026 - Solo Fotos": {"base": 8000, "per_person": True, "desc": "Cobertura fotográfica por alumno."},
    "Promo 2026 - Video + Fotos": {"base": 10000, "per_person": True, "desc": "Combo de video y fotos por alumno."},
    "Promo 2026 - Combo Full (Drone)": {"base": 12000, "per_person": True, "desc": "Fotos, Video y Drone 4K por alumno."},
    "Evento (Solo Fotos)": {"base": 180000, "con_drone": 180000, "desc": "Cobertura fotográfica profesional."}
}

DEPARTAMENTOS = {
    "Albardón": 0, "Capital": 15, "Chimbas": 8, "Santa Lucía": 18, "Rivadavia": 20,
    "Rawson": 22, "Pocito": 30, "Caucete": 35, "Angaco": 10, "San Martín": 18,
    "9 de Julio": 23, "Ullum": 20, "Zonda": 25, "Sarmiento": 45, "25 de Mayo": 40,
    "Jáchal": 150, "Iglesia": 170, "Calingasta": 180, "Valle Fértil": 250
}

# Selección del Usuario
servicio_nom = st.selectbox("¿Qué tipo de servicio buscás?", list(SERVICIOS.keys()))
datos = SERVICIOS[servicio_nom]

# Lógica especial para Promos (Cantidad de alumnos)
cantidad = 1
if datos.get("per_person"):
    cantidad = st.number_input("¿Cuántos alumnos son?", min_value=1, value=20, step=1)
    con_drone = False # Ya está incluido en el precio de la promo full
else:
    con_drone = st.checkbox("¿Querés incluir tomas con Drone 4K? 🚁")

lugar_evento = st.selectbox("¿En qué departamento es el evento?", list(DEPARTAMENTOS.keys()))

# --- CÁLCULO FINAL ---
precio_base = datos["con_drone"] if (not datos.get("per_person") and con_drone) else datos["base"]
subtotal = precio_base * cantidad
km_ida = DEPARTAMENTOS[lugar_evento]
viaticos = km_ida * 1000
total_final = subtotal + viaticos

# Mostrar resultado
st.info(f"**Servicio:** {servicio_nom}")
if datos.get("per_person"):
    st.write(f"👥 Presupuesto para {cantidad} alumnos.")

st.metric(label="Presupuesto Estimado", value=f"${total_final:,.0f}")
st.caption(f"Detalle: {datos['desc']}")

# --- SECCIÓN 3: CONTACTO ---
mi_numero = "5492645164757" 
texto_mensaje = f"Hola Diego! Coticé un {servicio_nom} en {lugar_evento} para {cantidad} personas. Total: ${total_final:,.0f}."
mensaje_url = urllib.parse.quote(texto_mensaje)
link_whatsapp = f"https://wa.me/{mi_numero}?text={mensaje_url}"

st.write("---")
st.link_button("📱 Consultar por WhatsApp", link_whatsapp, use_container_width=True)
