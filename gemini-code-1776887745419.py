import streamlit as st
import urllib.parse

# 1. Configuración de la pestaña
st.set_page_config(
    # Inyectar CSS para cambiar el color de los botones a azul
st.markdown("""
    <style>
    .stButton>button {
        background-color: #004aad;
        color: white;
        border-radius: 20px;
        height: 3em;
        width: 100%;
    }
    .stMetric {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #004aad;
    }
    </style>
    """, unsafe_allow_html=True)
    page_title="Presupuestador DL Fotografía", 
    page_icon="logo.png",
    layout="centered"
)

# 2. Tu Logo
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

# Base de datos con precios FIJOS por alumno
SERVICIOS = {
    "Colegios: Promo 2026 (Solo Fotos)": {"base": 8000, "per_person": True, "desc": "Cobertura fotográfica profesional."},
    "Colegios: Promo 2026 (Fotos y Video)": {"base": 10000, "per_person": True, "desc": "Combo de video y fotos."},
    "Colegios: Promo 2026 (Completo: Fotos, Video y Drone)": {"base": 12000, "per_person": True, "desc": "Servicio premium con Drone 4K."},
    "Boda Completa": {"base": 300000, "con_drone": 370000, "desc": "Civil, Iglesia y Fiesta. +200 fotos y 2 videos."},
    "Evento 15/18 años": {"base": 230000, "con_drone": 300000, "desc": "6hs de cobertura, +100 fotos y 1 video."},
    "Video Musical 4K": {"base": 300000, "con_drone": 300000, "desc": "Producción profesional de video musical (aprox. 5 min)."},
    "Sesión Retrato/Bebé (2hs)": {"base": 40000, "con_drone": 40000, "desc": "50-70 fotos digitales."},
    "Bautismo (Iglesia + Fiesta)": {"base": 230000, "con_drone": 230000, "desc": "+100 fotos y 1 video."},
    "Evento (Solo Fotos)": {"base": 180000, "con_drone": 180000, "desc": "Cobertura fotográfica profesional."}
}

DEPARTAMENTOS = {
    "Albardón": 0, "Capital": 15, "Chimbas": 8, "Santa Lucía": 18, "Rivadavia": 20,
    "Rawson": 22, "Pocito": 30, "Caucete": 35, "Angaco": 10, "San Martín": 18,
    "9 de Julio": 23, "Ullum": 20, "Zonda": 25, "Sarmiento": 45, "25 de Mayo": 40,
    "Jáchal": 150, "Iglesia": 170, "Calingasta": 180, "Valle Fértil": 250
}

# Selección
servicio_nom = st.selectbox("¿Qué tipo de servicio buscás?", list(SERVICIOS.keys()))
datos = SERVICIOS[servicio_nom]

# Lógica según el tipo de servicio
if datos.get("per_person"):
    cantidad = st.number_input("¿Cuántos alumnos son?", min_value=1, value=25, step=1)
    con_drone = False 
else:
    cantidad = 1
    con_drone = st.checkbox("¿Querés incluir tomas con Drone 4K? 🚁")

lugar_evento = st.selectbox("¿En qué departamento es el evento?", list(DEPARTAMENTOS.keys()))

# --- CÁLCULO ---
km_ida = DEPARTAMENTOS[lugar_evento]
viaticos = km_ida * 1000

if datos.get("per_person"):
    subtotal_grupo = datos["base"] * cantidad
    total_final = subtotal_grupo + viaticos
    # El precio por alumno se mantiene en el base que vos pediste
    precio_mostrar_alumno = datos["base"]
else:
    subtotal = datos["con_drone"] if con_drone else datos["base"]
    total_final = subtotal + viaticos

# --- MOSTRAR RESULTADO ---
st.info(f"**Servicio:** {servicio_nom}")

if datos.get("per_person"):
    c1, c2 = st.columns(2)
    c1.metric(label="Precio por Alumno", value=f"${precio_mostrar_alumno:,.0f}")
    c2.metric(label="Total Grupo (con traslado)", value=f"${total_final:,.0f}")
    st.write(f"👥 Presupuesto para un grupo de **{cantidad}** alumnos.")
else:
    st.metric(label="Presupuesto Estimado", value=f"${total_final:,.0f}")

st.write(f"📝 **Incluye:** {datos['desc']}")

# --- SECCIÓN 3: CONTACTO ---
mi_numero = "5492645164757" 
if datos.get("per_person"):
    detalle_msg = f"para {cantidad} alumnos a ${precio_mostrar_alumno:,.0f} c/u"
else:
    detalle_msg = "con Drone" if con_drone else "base"

texto_mensaje = f"Hola Diego! Coticé un '{servicio_nom}' {detalle_msg} en {lugar_evento}. Total: ${total_final:,.0f}."
mensaje_url = urllib.parse.quote(texto_mensaje)
link_whatsapp = f"https://wa.me/{mi_numero}?text={mensaje_url}"

st.write("---")
st.link_button("📱 Consultar por WhatsApp", link_whatsapp, use_container_width=True)
