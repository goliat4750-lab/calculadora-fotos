import streamlit as st
import urllib.parse

# 1. Configuración de la pestaña
st.set_page_config(
    page_title="Presupuestador DL Fotografía", 
    page_icon="logo.png",
    layout="centered"
)

# --- ESTILOS PERSONALIZADOS (Contraste para resaltar el logo) ---
st.markdown("""
    <style>
    /* Fondo degradado oscuro (Gris espacial / Negro) */
    .stApp {
        background: linear-gradient(180deg, #0f0f0f 0%, #2c2c2c 100%);
        color: white;
    }
    
    /* Forzar que los textos sean blancos para que resalten */
    .stMarkdown, p, span, label, h1, h2, h3 {
        color: white !important;
    }

    /* Estilo para los selectores (más oscuros para que no chillen) */
    .stSelectbox div[data-baseweb="select"], .stNumberInput div[data-baseweb="input"] {
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 10px;
    }

    /* Botón de WhatsApp en verde vibrante */
    .stButton>button {
        background-color: #25d366;
        color: white;
        border-radius: 10px;
        border: none;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #128c7e;
        transform: scale(1.02);
    }

    /* Tarjetas de métricas con borde azul (el azul de tu logo) */
    [data-testid="stMetric"] {
        background-color: rgba(0, 0, 0, 0.3);
        padding: 15px;
        border-radius: 15px;
        border: 1px solid #004aad; /* Usamos el azul de tu logo como acento */
    }
    
    [data-testid="stMetricValue"] {
        color: #ffffff !important;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Logo principal (Ahora va a resaltar mucho más)
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

servicio_nom = st.selectbox("¿Qué tipo de servicio buscás?", list(SERVICIOS.keys()))
datos = SERVICIOS[servicio_nom]

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
    total_grupo = (datos["base"] * cantidad) + viaticos
    precio_alumno = datos["base"]
else:
    subtotal = datos["con_drone"] if con_drone else datos["base"]
    total_final = subtotal + viaticos

# --- MOSTRAR RESULTADO ---
st.write("---")
if datos.get("per_person"):
    c1, c2 = st.columns(2)
    c1.metric(label="Precio por Alumno", value=f"${precio_alumno:,.0f}")
    c2.metric(label="Total Grupo (con traslado)", value=f"${total_grupo:,.0f}")
else:
    st.metric(label="Presupuesto Estimado", value=f"${total_final:,.0f}")

st.write(f"📝 **Incluye:** {datos['desc']}")

# --- SECCIÓN 3: CONTACTO ---
mi_numero = "5492645164757" 
if datos.get("per_person"):
    msg_total = total_grupo
    detalle_msg = f"para {cantidad} alumnos a ${precio_alumno:,.0f} c/u"
else:
    msg_total = total_final
    detalle_msg = "con Drone" if con_drone else "base"

texto_mensaje = f"Hola Diego! Coticé un '{servicio_nom}' {detalle_msg} en {lugar_evento}. Total: ${msg_total:,.0f}."
mensaje_url = urllib.parse.quote(texto_mensaje)
link_whatsapp = f"https://wa.me/{mi_numero}?text={mensaje_url}"

st.write("---")
st.link_button("📱 Consultar disponibilidad por WhatsApp", link_whatsapp, use_container_width=True)
