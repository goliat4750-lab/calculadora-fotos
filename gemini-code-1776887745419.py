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

def render_video(video_path, opacity=1.0, height="350px", loop=True):
    if os.path.exists(video_path):
        with open(video_path, "rb") as f:
            video_bytes = f.read()
        video_base64 = base64.b64encode(video_bytes).decode()
        loop_attr = "loop" if loop else ""
        return f'<video autoplay {loop_attr} muted playsinline style="width: 100%; height: {height}; object-fit: cover; opacity: {opacity}; border-radius: 15px;"><source src="data:video/mp4;base64,{video_base64}" type="video/mp4"></video>'
    return None

# --- 2. CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="DL Fotografía y Video", 
    page_icon="foto4.png",
    layout="wide"
)

# --- 3. TRUCO PARA OCULTAR PROPAGANDA (CSS) ---
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stToolbar"] {visibility: hidden;}
    .block-container { padding-top: 1rem; }
    .stApp { background-color: #0b0d10; color: white; }
    /* Ajuste global de imágenes */
    .stImage img { border-radius: 10px; }
    </style>
""", unsafe_allow_html=True)

# --- 4. SECCIÓN DE BIENVENIDA (TEATRO) ---
logo_base64 = get_base64_image("foto4.png")
video_html = render_video("teatro.mp4", opacity=0.5, height="400px")

if video_html:
    st.markdown(f"""
        <div style="position: relative; height: 400px; overflow: hidden; border-radius: 15px; margin-bottom: 30px;">
            <div style="position: absolute; width: 100%; height: 100%;">{video_html}</div>
            <div style="position: relative; z-index: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100%; text-align: center;">
                <img src="data:image/png;base64,{logo_base64}" style="max-width: 180px; filter: drop-shadow(0px 0px 15px rgba(0,74,173,0.8));">
                <h1 style="color: white; margin-top: 15px; text-shadow: 2px 2px 8px rgba(0,0,0,0.9);">DL Fotografía y Video</h1>
            </div>
        </div>
        """, unsafe_allow_html=True)
else:
    st.warning("Subí 'teatro.mp4' para ver el video de fondo.")

# --- 5. SECCIÓN: SOBRE MÍ ---
col_foto, col_texto = st.columns([1, 2])

with col_foto:
    if os.path.exists("foto1.jpg"):
        st.image("foto1.jpg", width=280)
    
    # Insertamos tu video del campo aquí (Vertical)
    video_campo_html = render_video("campo.mp4", height="400px")
    if video_campo_html:
        st.markdown("<p style='text-align:center; margin-top:10px;'>En acción</p>", unsafe_allow_html=True)
        st.markdown(video_campo_html, unsafe_allow_html=True)

with col_texto:
    st.header("Sobre mi trabajo")
    st.write("""
    Mi nombre es **Diego Lozano**. Soy un apasionado de la narrativa visual, especializado en 
    bodas, 15 años y eventos sociales en Albardón y toda la provincia.
    
    Mi enfoque combina la espontaneidad del momento con la más alta calidad técnica. 
    Para garantizar resultados impecables, utilizo **equipos profesionales de alta gama** y realizo **tomas aéreas en resolución 4K** para lograr una perspectiva cinematográfica única.
    """)
    if os.path.exists("foto3.jpg"):
        st.image("foto3.jpg", caption="Post-producción profesional", width=450)

# --- 6. CALCULADORA ---
st.divider()
st.title("📊 Cotizá tu evento")

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
    con_drone = st.checkbox("¿Incluir tomas aéreas 4K?")
with c2:
    lugar_evento = st.selectbox("¿En qué departamento?", list(DEPARTAMENTOS.keys()))

datos = SERVICIOS[servicio_nom]
total_final = (datos["con_drone"] if con_drone else datos["base"]) + (DEPARTAMENTOS[lugar_evento] * 1000)

st.metric(label="Presupuesto Estimado", value=f"${total_final:,.0f}")

# --- 7. BOTÓN DE WHATSAPP ---
mi_numero = "5492645164757"
texto_mensaje = f"Hola Diego! Coticé un '{servicio_nom}' en {lugar_evento}. Total: ${total_final:,.0f}."
st.link_button("📱 Consultar disponibilidad por WhatsApp", 
               f"https://wa.me/{mi_numero}?text={urllib.parse.quote(texto_mensaje)}", 
               use_container_width=True)

st.markdown("<br><hr><center>© 2026 DL Fotografía y Video | Albardón, San Juan</center>", unsafe_allow_html=True)
