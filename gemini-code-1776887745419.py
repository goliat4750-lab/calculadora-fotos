import streamlit as st
import urllib.parse
from datetime import datetime
import os

# --- 1. CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="DL Fotografía y Video", 
    page_icon="foto4.png",
    layout="wide"
)

# --- 2. TRUCO PARA OCULTAR PROPAGANDA Y ESTILOS ---
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stToolbar"] {visibility: hidden;}
    .block-container { padding-top: 1rem; }
    .stApp { background-color: #0b0d10; color: white; }
    
    /* Estilo para centrar la cabecera */
    .header-box {
        text-align: center;
        padding: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. ENCABEZADO: FOTO Y LOGO ---
st.markdown('<div class="header-box">', unsafe_allow_html=True)
col_a, col_b, col_c = st.columns([1, 1, 1])

with col_b:
    # Mostramos tu foto sentado arriba y chica
    if os.path.exists("foto1.jpg"):
        st.image("foto1.jpg", width=150)
    
    # Mostramos el logo justo abajo de tu foto
    if os.path.exists("foto4.png"):
        st.image("foto4.png", width=220)
    else:
        st.write("### DL Fotografía y Video") # Respaldo si no carga el logo
st.markdown('</div>', unsafe_allow_html=True)

# --- 4. VIDEO DE BIENVENIDA (TEATRO) ---
if os.path.exists("teatro.mp4"):
    st.video("teatro.mp4", loop=True, autoplay=True, muted=True)

# --- 5. SECCIÓN: SOBRE MÍ Y DRIVE ---
st.divider()
col_video, col_info = st.columns([1, 1.5])

with col_video:
    if os.path.exists("campo.mp4"):
        st.write("🎬 **En acción:**")
        st.video("campo.mp4", loop=True, autoplay=True, muted=True)
    if os.path.exists("foto3.jpg"):
        st.image("foto3.jpg", caption="Edición Profesional", width=300)

with col_info:
    st.header("Diego Lozano - Fotografía y Video")
    st.write("""
    Especialista en narrativa visual para bodas, 15 años y eventos sociales. 
    Mi enfoque combina la espontaneidad con la más alta calidad técnica, 
    utilizando equipos de alta gama y tomas aéreas 4K para un resultado cinematográfico.
    """)
    st.success("✅ **Entrega Digital:** Todos los trabajos se entregan mediante una galería privada en **Google Drive** para descarga inmediata.")

# --- 6. CALCULADORA DE PRECIOS ---
st.divider()
st.title("📊 Cotizá tu evento")
st.warning("⚠️ **Precios vigentes hasta el 31 de Mayo de 2026**")

fecha_actual = datetime.now()
fecha_aumento = datetime(2026, 6, 1)
multiplicador = 1.20 if fecha_actual >= fecha_aumento else 1.0

SERVICIOS = {
    "Evento 15/18 años": {"base": 230000 * multiplicador, "con_drone": 300000 * multiplicador, "desc": "6hs de cobertura, +100 fotos editadas y video resumen."},
    "Boda Completa": {"base": 320000 * multiplicador, "con_drone": 390000 * multiplicador, "desc": "Civil, Iglesia y Fiesta. +200 fotos y 2 videos."},
    "Bautismo (Iglesia + Fiesta)": {"base": 230000 * multiplicador, "con_drone": 230000 * multiplicador, "desc": "Cobertura completa, +100 fotos y 1 video."},
    "Video Musical 4K": {"base": 300000 * multiplicador, "con_drone": 300000 * multiplicador, "desc": "Producción y edición profesional."},
    "Sesión Retrato (2hs)": {"base": 40000 * multiplicador, "con_drone": 40000 * multiplicador, "desc": "50-70 fotos digitales editadas."},
    "Evento (Solo Fotos)": {"base": 180000 * multiplicador, "con_drone": 180000 * multiplicador, "desc": "Cobertura fotográfica completa."}
}

DEPARTAMENTOS = {
    "Albardón": 0, "Capital": 15, "Chimbas": 8, "Santa Lucía": 18, "Rivadavia": 20,
    "Rawson": 22, "Pocito": 30, "Caucete": 35, "Angaco": 10, "San Martín": 18,
    "9 de Julio": 23, "Ullum": 20, "Zonda": 25, "Sarmiento": 45, "25 de Mayo": 40,
    "Jáchal": 150, "Iglesia": 170, "Calingasta": 180, "Valle Fértil": 250
}

c1, c2 = st.columns(2)
with c1:
    servicio_nom = st.selectbox("¿Qué servicio buscás?", list(SERVICIOS.keys()))
    con_drone = st.checkbox("¿Incluir tomas aéreas 4K?")
with c2:
    lugar_evento = st.selectbox("¿Departamento?", list(DEPARTAMENTOS.keys()))

datos = SERVICIOS[servicio_nom]
total_final = (datos["con_drone"] if con_drone else datos["base"]) + (DEPARTAMENTOS[lugar_evento] * 1000)

st.metric(label="Presupuesto Estimado", value=f"${total_final:,.0f}")
st.info(f"📝 **Incluye:** {datos['desc']} | ☁️ **Entrega vía Google Drive**.")

# --- 7. BOTÓN DE WHATSAPP ---
mi_numero = "5492645164757"
texto_mensaje = f"Hola Diego! Coticé un '{servicio_nom}' en {lugar_evento}. Total: ${total_final:,.0f}. Entrega en Drive."
st.link_button("📱 Consultar disponibilidad por WhatsApp", 
               f"https://wa.me/{mi_numero}?text={urllib.parse.quote(texto_mensaje)}", 
               use_container_width=True)

st.markdown("<br><hr><center>© 2026 DL Fotografía y Video | Albardón, San Juan</center>", unsafe_allow_html=True)
