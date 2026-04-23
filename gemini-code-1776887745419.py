import streamlit as st
import urllib.parse
from datetime import datetime

# 1. Configuración de la pestaña
st.set_page_config(
    page_title="Presupuestador DL Fotografía", 
    page_icon="logo.png",
    layout="centered"
)

# --- LÓGICA DE ACTUALIZACIÓN AUTOMÁTICA ---
fecha_actual = datetime.now()
fecha_aumento = datetime(2026, 6, 1)
multiplicador = 1.20 if fecha_actual >= fecha_aumento else 1.0

# --- ESTILOS PERSONALIZADOS ---
st.markdown("""
    <style>
    /* Estilo general de la app */
    .stApp {
        background: linear-gradient(135deg, #004aad 0%, #6a0dad 100%);
        color: white;
    }
    
    /* Textos en blanco */
    .stMarkdown, p, span, label, h1, h2, h3 {
        color: white !important;
    }

    /* Selectores con fondo traslúcido */
    .stSelectbox div[data-baseweb="select"], .stNumberInput div[data-baseweb="input"] {
        background-color: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 10px;
    }

    /* Botón de WhatsApp */
    .stButton>button {
        background-color: #25d366;
        color: white;
        border-radius: 10px;
        border: none;
        font-weight: bold;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.3);
    }

    /* Tarjetas de métricas */
    [data-testid="stMetric"] {
        background-color: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        padding: 15px;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    [data-testid="stMetricValue"] {
        color: #ffffff !important;
    }

    /* === NUEVO ESTILO PARA EL FONDO DEL LOGO === */
    .logo-container {
        position: relative;
        width: 100%;
        height: 300px; /* Ajusta la altura a tu gusto */
        border-radius: 20px;
        overflow: hidden;
        margin-bottom: 20px;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.5);
    }

    .background-image {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        /* ABAJO: Cambia "_DSC3558.jpg" por el nombre de tu foto llamativa */
        background-image: url('_DSC3558.jpg'); 
        background-size: cover;
        background-position: center;
        filter: blur(3px) brightness(0.6); /* Desenfoque y oscurecimiento para resaltar logo */
        z-index: 1;
    }

    .logo-image {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        max-width: 80%; /* Ajusta el tamaño del logo */
        max-height: 80%;
        z-index: 2;
        filter: drop-shadow(0px 5px 15px rgba(0,0,0,0.8)); /* Sombra para el logo PNG */
    }
    /* =========================================== */
    </style>
    """, unsafe_allow_html=True)

# 2. SECCIÓN DEL LOGO CON IMAGEN DE FONDO
st.write("---") # Una línea divisoria antes de la sección
try:
    # Creamos el contenedor HTML con la imagen de fondo y el logo encima
    st.markdown(f"""
        <div class="logo-container">
            <div class="background-image"></div>
            <img src="logo.png" class="logo-image" alt="DL Fotografía y Video">
        </div>
    """, unsafe_allow_html=True)
except:
    # Si las imágenes no cargan, mostramos el título como respaldo
    st.title("DL Fotografía y Video")


# --- SECCIÓN 1: CALENDARIO ---
st.divider()
st.subheader("📅 Disponibilidad de Fechas")
calendar_url = "https://calendar.google.com/calendar/embed?src=goliat4750%40gmail.com&ctz=America%2FArgentina%2FCordoba"
st.components.v1.iframe(calendar_url, height=500, scrolling=True)

# --- SECCIÓN 2: CALCULADORA ---
st.divider()
st.subheader("📊 Cotizá tu Servicio")

# Lista de servicios actualizada
SERVICIOS = {
    "Evento 15/18 años": {"base": 230000 * multiplicador, "con_drone": 300000 * multiplicador, "desc": "6hs de cobertura, +100 fotos y 1 video."},
    "Boda Completa": {"base": 320000 * multiplicador, "con_drone": 390000 * multiplicador, "desc": "Civil, Iglesia y Fiesta. +200 fotos y 2 videos."},
    "Bautismo (Iglesia + Fiesta)": {"base": 230000 * multiplicador, "con_drone": 230000 * multiplicador, "desc": "+100 fotos y 1 video."},
    "Video Musical 4K": {"base": 300000 * multiplicador, "con_drone": 300000 * multiplicador, "desc": "Producción profesional de video musical."},
    "Sesión Retrato/Bebé (2hs)": {"base": 40000 * multiplicador, "con_drone": 40000 * multiplicador, "desc": "50-70 fotos digitales."},
    "Evento (Solo Fotos)": {"base": 180000 * multiplicador, "con_drone": 180000 * multiplicador, "desc": "Cobertura fotográfica profesional."}
}

DEPARTAMENTOS = {
    "Albardón": 0, "Capital": 15, "Chimbas": 8, "Santa Lucía": 18, "Rivadavia": 20,
    "Rawson": 22, "Pocito": 30, "Caucete": 35, "Angaco": 10, "San Martín": 18,
    "9 de Julio": 23, "Ullum": 20, "Zonda": 25, "Sarmiento": 45, "25 de Mayo": 40,
    "Jáchal": 150, "Iglesia": 170, "Calingasta": 180, "Valle Fértil": 250
}

servicio_nom = st.selectbox("¿Qué tipo de servicio buscás?", list(SERVICIOS.keys()))
datos = SERVICIOS[servicio_nom]

# Opciones de drone
con_drone = st.checkbox("¿Querés incluir tomas con Drone 4K?")

lugar_evento = st.selectbox("¿En qué departamento es el evento?", list(DEPARTAMENTOS.keys()))

# --- CÁLCULO ---
km_ida = DEPARTAMENTOS[lugar_evento]
viaticos = km_ida * 1000

subtotal = datos["con_drone"] if con_drone else datos["base"]
total_final = subtotal + viaticos

# --- MOSTRAR RESULTADO ---
st.write("---")
st.metric(label="Presupuesto Estimado", value=f"${total_final:,.0f}")

st.write(f"📝 **Incluye:** {datos['desc']}")
st.success(f"⚡ **Entrega Express:** Todo el material editado estará disponible en **48 horas**.")
st.write("📂 **Método:** Subido a **Google Drive** para descarga directa (disponible por 30 días).")

# --- SECCIÓN DE ADVERTENCIA POR INFLACIÓN ---
if fecha_actual < fecha_aumento:
    st.info(
        "⚠️ **Validez del Presupuesto:** Los valores se mantienen firmes "
        "únicamente hasta el **31 de mayo de 2026**. \n\n"
        "💡 *El precio se congela exclusivamente mediante el pago de la seña.*"
    )

# --- SECCIÓN 3: CONTACTO ---
mi_numero = "5492645164757" 
msg_total = total_final
detalle_msg = "con Drone" if con_drone else "base"

texto_mensaje = f"Hola Diego! Coticé un '{servicio_nom}' {detalle_msg} en {lugar_evento}. Total: ${msg_total:,.0f}."
mensaje_url = urllib.parse.quote(texto_mensaje)
link_whatsapp = f"https://wa.me/{mi_numero}?text={mensaje_url}"

st.write("---")
st.link_button("📱 Consultar disponibilidad por WhatsApp", link_whatsapp, use_container_width=True)
st.caption("DL Fotografía y Video | Albardón, San Juan")
