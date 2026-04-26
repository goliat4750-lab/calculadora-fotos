import streamlit as st
import urllib.parse
from datetime import datetime
import os
import base64

# --- 1. CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="DL Fotografía y Video", 
    page_icon="logo.png",
    layout="wide"
)

# --- 2. ESTILOS CSS ---
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stToolbar"] {visibility: hidden;}
    [data-testid="stElementToolbar"] {display: none !important;}
    
    .block-container { 
        padding-top: 1rem !important; 
        margin-top: -1rem !important;
    }
    
    .stApp { background-color: #0b0d10; color: white; }
    
    .centrar-todo {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        text-align: center;
        padding: 20px 0;
    }
    
    .logo-img {
        max-width: 280px;
        width: 80%; 
        height: auto;
    }

    /* Estilo para que el calendario se vea bien en móviles */
    .calendar-container {
        position: relative;
        padding-bottom: 75%;
        height: 0;
        overflow: hidden;
        border-radius: 10px;
        border: 1px solid #333;
        margin-bottom: 2rem;
    }
    .calendar-container iframe {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. ENCABEZADO CON LOGO ---
logo_path = "logo.png"
if os.path.exists(logo_path):
    with open(logo_path, "rb") as f:
        data = base64.b64encode(f.read()).decode()
    st.markdown(f'<div class="centrar-todo"><img src="data:image/png;base64,{data}" class="logo-img"></div>', unsafe_allow_html=True)
else:
    st.markdown("<h2 style='text-align: center;'>DL FOTOGRAFÍA Y VIDEO</h2>", unsafe_allow_html=True)

# --- 4. VIDEO DE BIENVENIDA ---
if os.path.exists("teatro.mp4"):
    st.video("teatro.mp4", loop=True, autoplay=True, muted=True)

# --- 5. SECCIÓN: SOBRE MÍ ---
st.divider()
col_info, col_extra = st.columns([2, 1])
with col_info:
    st.header("Sobre mi trabajo")
    st.write("""
    Especialista en narrativa visual para bodas, 15 años y eventos sociales en San Juan. 
    Mi enfoque combina la espontaneidad con la más alta calidad técnica, 
    utilizando equipos profesionales y tomas aéreas 4K para un resultado cinematográfico.
    """)
    st.success("✅ **Entrega Digital:** Todos los trabajos se entregan mediante una galería privada en **Google Drive** para descarga inmediata.")

with col_extra:
    if os.path.exists("foto3.jpg"):
        st.image("foto3.jpg", caption="Post-producción profesional", use_container_width=True)

# --- 6. COTIZADOR Y CALENDARIO ---
st.divider()
st.title("📊 Cotizá tu evento")
st.warning("⚠️ **Precios vigentes hasta el 31 de Mayo de 2026**")

# Calendario ubicado justo después del título
st.subheader("📅 Consultá mi disponibilidad")
google_calendar_url = "https://calendar.google.com/calendar/embed?src=goliat4750@gmail.com&ctz=America/Argentina/Buenos_Aires&wkst=1&bgcolor=%230b0d10&showTitle=0&showNav=1&showPrint=0&showTabs=0&showCalendars=0&showTz=0"

st.markdown(f"""
    <div class="calendar-container">
        <iframe src="{google_calendar_url}" style="border-width:0" frameborder="0" scrolling="no"></iframe>
    </div>
""", unsafe_allow_html=True)

# --- 7. CALCULADORA DE PRECIOS ---
SERVICIOS = {
    "Evento 15/18 años": {"base": 320000, "con_drone": 400000, "desc": "6hs de cobertura, +100 fotos editadas y video hd."},
    "Boda Completa": {"base": 400000, "con_drone": 470000, "desc": "Civil, Iglesia y Fiesta. +200 fotos y 2 videos."},
    "Bautismo (Iglesia + Fiesta)": {"base": 280000, "con_drone": 365000, "desc": "Cobertura completa, +100 fotos y 1 video."},
    "Video Musical 4K": {"base": 360000, "con_drone": 445000, "desc": "Producción y edición profesional."},
    "Sesión Retrato (2hs)": {"base": 60000, "con_drone": 135000, "desc": "50-70 fotos digitales editadas."},
    "Evento (Solo Fotos)": {"base": 215000, "con_drone": 300000, "desc": "Cobertura fotográfica completa."}
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
total_final = (datos["con_drone"] if con_drone else datos["base"]) + (DEPARTAMENTOS[lugar_evento] * 1200)

st.metric(label="Presupuesto Estimado", value=f"${total_final:,.0f}")
st.info(f"📝 **Incluye:** {datos['desc']}")

# --- 8. BOTÓN DE WHATSAPP ---
mi_numero = "5492645164757"
texto_mensaje = f"Hola Diego! Coticé un '{servicio_nom}' en {lugar_evento}. Total: ${total_final:,.0f}."
st.link_button("📱 Consultar por WhatsApp", 
               f"https://wa.me/{mi_numero}?text={urllib.parse.quote(texto_mensaje)}", 
               use_container_width=True)

st.markdown("<br><hr><center>© 2026 DL Fotografía y Video | Albardón, San Juan</center>", unsafe_allow_html=True)
