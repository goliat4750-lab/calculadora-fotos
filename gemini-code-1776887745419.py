import streamlit as st
import urllib.parse
from datetime import datetime
import base64
import os

# --- 1. FUNCIONES DE APOYO ---
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

# --- 2. CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="DL Fotografía y Video", 
    page_icon="foto4.png",
    layout="wide"
)

# --- 3. TRUCO PARA OCULTAR PROPAGANDA (CSS) ---
hide_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stToolbar"] {visibility: hidden;}
    /* Esto quita el espacio blanco de arriba */
    .block-container {
        padding-top: 2rem;
    }
    </style>
"""
st.markdown(hide_style, unsafe_allow_html=True)

# --- 4. ESTILOS VISUALES Y HERO SECTION ---
logo_base64 = get_base64_image("foto4.png")

st.markdown(f"""
    <style>
    .stApp {{
        background-color: #0b0d10;
        color: white;
    }}
    .hero-section {{
        text-align: center;
        padding: 40px 10px;
        background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), url("https://images.unsplash.com/photo-1492691527719-9d1e07e534b4?q=80&w=2071&auto=format&fit=crop");
        background-size: cover;
        border-radius: 15px;
        margin-bottom: 30px;
    }}
    .logo-img {{
        max-width: 220px;
        filter: drop-shadow(0px 0px 12px rgba(0,74,173,0.6));
    }}
    </style>
    <div class="hero-section">
        <img src="data:image/png;base64,{logo_base64}" class="logo-img">
        <h1 style='margin-top:15px; font-family: sans-serif;'>DL Fotografía y Video</h1>
        <p style='font-size: 1.1rem; opacity: 0.9;'>Capturando momentos únicos en San Juan</p>
    </div>
    """, unsafe_allow_html=True)

# --- 5. SECCIÓN: SOBRE MÍ Y EQUIPOS ---
col_foto, col_texto = st.columns([1, 1.5])

with col_foto:
    if os.path.exists("foto1.jpg"):
        st.image("foto1.jpg", use_container_width=True)
    else:
        st.info("Sube 'foto1.jpg' para ver tu perfil.")

with col_texto:
    st.header("Sobre mi trabajo")
    st.write("""
    Mi nombre es **Diego Lozano**. Soy un apasionado de la narrativa visual, especializado en 
    bodas, 15 años y eventos sociales en Albardón y toda la provincia.
    
    Mi enfoque combina la espontaneidad del momento con la más alta calidad técnica. 
    Para garantizar resultados impecables, trabajo con **equipos profesionales**: 
    cámaras Nikon de alta resolución y tomas aéreas con drone **Potensic Atom 2** en 4K.
    """)
    if os.path.exists("foto3.jpg"):
        st.image("foto3.jpg", caption="Post-producción profesional", use_container_width=True)

# --- 6. LÓGICA DE LA CALCULADORA ---
st.divider()
st.title("📊 Cotizá tu evento al instante")

fecha_actual = datetime.now()
fecha_aumento = datetime(2026, 6, 1)
multiplicador = 1.20 if fecha_actual >= fecha_aumento else 1.0

SERVICIOS = {
    "Evento 15/18 años": {"base": 230000 * multiplicador, "con_drone": 300000 * multiplicador, "desc": "6hs de cobertura, +100 fotos editadas y 1 video resumen."},
    "Boda Completa": {"base": 320000 * multiplicador, "con_drone": 390000 * multiplicador, "desc": "Civil, Iglesia y Fiesta. +200 fotos y 2 videos editados."},
    "Bautismo (Iglesia + Fiesta)": {"base": 230000 * multiplicador, "con_drone": 230000 * multiplicador, "desc": "Cobertura completa, +100 fotos y 1 video."},
    "Video Musical 4K": {"base": 300000 * multiplicador, "con_drone": 300000 * multiplicador, "desc": "Producción y edición profesional de video musical."},
    "Sesión Retrato/Bebé (2hs)": {"base": 40000 * multiplicador, "con_drone": 40000 * multiplicador, "desc": "50-70 fotos digitales editadas en alta calidad."},
    "Evento (Solo Fotos)": {"base": 180000 * multiplicador, "con_drone": 180000 * multiplicador, "desc": "Cobertura fotográfica profesional completa."}
}

DEPARTAMENTOS = {
    "Albardón": 0, "Capital": 15, "Chimbas": 8, "Santa Lucía": 18, "Rivadavia": 20,
    "Rawson": 22, "Pocito": 30, "Caucete": 35, "Angaco": 10, "San Martín": 18,
    "9 de Julio": 23, "Ullum": 20, "Zonda": 25, "Sarmiento": 45, "25 de Mayo": 40,
    "Jáchal": 150, "Iglesia": 170, "Calingasta": 180, "Valle Fértil": 250
}

c1, c2 = st.columns(2)
with c1:
    servicio_nom = st.selectbox("¿Qué tipo de servicio buscás?", list(SERVICIOS.keys()))
    con_drone = st.checkbox("¿Incluir tomas con Drone 4K? (Potensic Atom 2)")
with c2:
    lugar_evento = st.selectbox("¿En qué departamento es el evento?", list(DEPARTAMENTOS.keys()))

datos = SERVICIOS[servicio_nom]
total_final = (datos["con_drone"] if con_drone else datos["base"]) + (DEPARTAMENTOS[lugar_evento] * 1000)

st.metric(label="Presupuesto Estimado", value=f"${total_final:,.0f}")
st.info(f"📝 **Incluye:** {datos['desc']} | **Entrega en 48hs vía Google Drive.**")

# --- 7. BOTÓN DE WHATSAPP ---
mi_numero = "5492645164757"
texto_mensaje = f"Hola Diego! Coticé un '{servicio_nom}' en {lugar_evento}. Total: ${total_final:,.0f}."
st.link_button("📱 Consultar disponibilidad por WhatsApp", 
               f"https://wa.me/{mi_numero}?text={urllib.parse.quote(texto_mensaje)}", 
               use_container_width=True)

st.markdown("<br><hr><center>© 2026 DL Fotografía y Video | Albardón, San Juan</center>", unsafe_allow_html=True)
