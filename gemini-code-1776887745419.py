import streamlit as st
import urllib.parse
from datetime import datetime
import base64

# Funciòn para convertir imagen a Base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# 1. Configuración de la pestaña
st.set_page_config(
    page_title="Presupuestador DL Fotografía", 
    page_icon="logo.png",
    layout="centered"
)

# Lógica de precios
fecha_actual = datetime.now()
fecha_aumento = datetime(2026, 6, 1)
multiplicador = 1.20 if fecha_actual >= fecha_aumento else 1.0

# Intentamos cargar la imagen de fondo y el logo en Base64
try:
    img_fondo_base64 = get_base64_image("_DSC3558.jpg")
    logo_base64 = get_base64_image("logo.png")
except:
    img_fondo_base64 = ""
    logo_base64 = ""

# --- ESTILOS ---
st.markdown(f"""
    <style>
    .stApp {{
        background: linear-gradient(135deg, #004aad 0%, #6a0dad 100%);
        color: white;
    }}
    .stMarkdown, p, span, label, h1, h2, h3 {{ color: white !important; }}

    /* CONTENEDOR DEL LOGO CON TU FOTO _DSC3558.jpg */
    .logo-container {{
        position: relative;
        width: 100%;
        height: 350px;
        border-radius: 20px;
        overflow: hidden;
        margin-bottom: 20px;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.5);
        border: 1px solid rgba(255, 255, 255, 0.2);
        background-image: url("data:image/jpg;base64,{img_fondo_base64}");
        background-size: cover;
        background-position: center;
    }}
    
    .overlay {{
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background: rgba(0, 0, 0, 0.4); /* Oscurece un poco la foto */
        backdrop-filter: blur(2px); /* Desenfoque suave */
        display: flex;
        align-items: center;
        justify-content: center;
    }}

    .logo-image {{
        max-width: 75%;
        filter: drop-shadow(0px 8px 20px rgba(0,0,0,0.9));
    }}
    
    /* Botón y tarjetas */
    .stButton>button {{ background-color: #25d366; color: white; border-radius: 10px; font-weight: bold; }}
    [data-testid="stMetric"] {{ background-color: rgba(255, 255, 255, 0.1); backdrop-filter: blur(10px); padding: 15px; border-radius: 15px; }}
    </style>

    <div class="logo-container">
        <div class="overlay">
            <img src="data:image/png;base64,{logo_base64}" class="logo-image">
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- RESTO DEL CÓDIGO (Calculadora y WhatsApp) ---
st.divider()
st.subheader("📅 Disponibilidad de Fechas")
calendar_url = "https://calendar.google.com/calendar/embed?src=goliat4750%40gmail.com&ctz=America%2FArgentina%2FCordoba"
st.components.v1.iframe(calendar_url, height=500, scrolling=True)

st.divider()
st.subheader("📊 Cotizá tu Servicio")

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
con_drone = st.checkbox("¿Querés incluir tomas con Drone 4K?")
lugar_evento = st.selectbox("¿En qué departamento es el evento?", list(DEPARTAMENTOS.keys()))

total_final = (datos["con_drone"] if con_drone else datos["base"]) + (DEPARTAMENTOS[lugar_evento] * 1000)

st.write("---")
st.metric(label="Presupuesto Estimado", value=f"${total_final:,.0f}")
st.write(f"📝 **Incluye:** {datos['desc']}")
st.success("⚡ **Entrega Express:** Todo el material editado disponible en **48 horas** en **Google Drive**.")

if fecha_actual < fecha_aumento:
    st.info("⚠️ **Validez:** Precios firmes hasta el **31 de mayo de 2026**.")

# Botón WhatsApp
mi_numero = "5492645164757"
texto_mensaje = f"Hola Diego! Coticé un '{servicio_nom}' en {lugar_evento}. Total: ${total_final:,.0f}."
st.link_button("📱 Consultar por WhatsApp", f"https://wa.me/{mi_numero}?text={urllib.parse.quote(texto_mensaje)}", use_container_width=True)
st.caption("DL Fotografía y Video | Albardón, San Juan")
