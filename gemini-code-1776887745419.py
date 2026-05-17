import streamlit as st
import urllib.parse
from datetime import datetime
import os
import base64

# --- 1. CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="DL Fotografía y Video", 
    page_icon="logo2.png",
    layout="wide"
)

# --- 2. ESTILOS CSS AVANZADOS (CINEMATIC DARK) ---
st.markdown("""
    <style>
    /* Importar fuentes de Google */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600&family=Oswald:wght@400;500;700&display=swap');

    /* Ocultar elementos por defecto de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stToolbar"] {visibility: hidden;}
    [data-testid="stElementToolbar"] {display: none !important;}
    
    .block-container { 
        padding-top: 1rem !important; 
        margin-top: -1rem !important;
    }
    
    /* Fondo y fuente global */
    .stApp { 
        background-color: #0b0d10; 
        color: #e0e0e0; 
        font-family: 'Montserrat', sans-serif;
    }

    /* Estilo de todos los títulos */
    h1, h2, h3 {
        font-family: 'Oswald', sans-serif !important;
        color: #E5A93C !important; /* Dorado cinematográfico */
        letter-spacing: 1.5px;
        text-transform: uppercase;
    }
    
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
        filter: drop-shadow(0px 0px 10px rgba(229, 169, 60, 0.3)); /* Resplandor dorado en el logo */
    }

    /* Contenedor del calendario */
    .calendar-container {
        position: relative;
        padding-bottom: 75%;
        height: 0;
        overflow: hidden;
        border-radius: 12px;
        border: 2px solid #E5A93C; /* Borde dorado */
        box-shadow: 0 4px 20px rgba(229, 169, 60, 0.15);
        margin-bottom: 2rem;
    }
    .calendar-container iframe {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
    }

    /* Estilo para la tarjeta de precio final (Metric) */
    [data-testid="stMetric"] {
        background-color: #15191f;
        border: 1px solid #E5A93C;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(229, 169, 60, 0.2);
        text-align: center;
    }
    [data-testid="stMetricValue"] {
        color: #E5A93C !important;
        font-family: 'Oswald', sans-serif;
        font-size: 3rem !important;
    }
    
    /* Alertas y avisos más estéticos (st.warning) */
    div[data-testid="stAlert"] {
        background-color: #15191f;
        color: #e0e0e0;
        border: none;
        border-left: 5px solid #E5A93C;
        border-radius: 4px;
    }

    /* Modificación del st.info para los detalles de la sesión */
    div[data-testid="stNotification"] {
        background-color: #15191f !important;
        border: none !important;
        border-left: 5px solid #E5A93C !important;
        border-radius: 4px !important;
    }
    div[data-testid="stNotification"] p {
        font-size: 18px !important; /* Texto más grande */
        color: #e0e0e0 !important; /* Color gris claro/blanco para quitar el azul */
    }

    /* Tarjetas personalizadas para formas de pago */
    .pago-card {
        background-color: #15191f;
        border: 1px solid #2a313d;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        height: 100%;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    }
    .pago-card h4 {
        color: #E5A93C;
        font-family: 'Oswald', sans-serif;
        margin-bottom: 10px;
    }

    /* Botón de WhatsApp Personalizado */
    .btn-whatsapp {
        display: flex;
        justify-content: center;
        align-items: center;
        background: linear-gradient(45deg, #25D366, #128C7E);
        color: white !important;
        padding: 18px 20px;
        text-decoration: none;
        border-radius: 10px;
        font-family: 'Montserrat', sans-serif;
        font-weight: 600;
        font-size: 18px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(37, 211, 102, 0.3);
        margin-top: 20px;
    }
    .btn-whatsapp:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(37, 211, 102, 0.5);
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. ENCABEZADO CON LOGO ---
logo_path = "logo2.png"
if os.path.exists(logo_path):
    with open(logo_path, "rb") as f:
        data = base64.b64encode(f.read()).decode()
    st.markdown(f'<div class="centrar-todo"><img src="data:image/png;base64,{data}" class="logo-img"></div>', unsafe_allow_html=True)
else:
    st.markdown("<h2 style='text-align: center; color: #E5A93C;'>DL FOTOGRAFÍA Y VIDEO</h2>", unsafe_allow_html=True)

# --- 4. VIDEO DE BIENVENIDA ---
if os.path.exists("bodadrone.mp4"):
    st.video("bodadrone.mp4", loop=True, autoplay=True, muted=True)

# --- 5. SECCIÓN: SOBRE MÍ ---
st.divider()
col_info, col_extra = st.columns([2, 1])
with col_info:
    st.header("Sobre mi trabajo")
    st.write("""
    Especialista en narrativa visual para bodas, 15 años y eventos sociales en San Juan. 
    Mi enfoque combina la espontaneidad con la más alta calidad técnica, 
    utilizando equipos profesionales y tomas con drone 4K para un resultado cinematográfico.
    """)
    st.success("✅ **Entrega Digital:** Todos los trabajos se entregan mediante una galería privada en **Google Drive** para descarga inmediata.")

with col_extra:
    if os.path.exists("foto3.jpg"):
        st.image("foto3.jpg", caption="Post-producción profesional", use_container_width=True)

# --- 6. COTIZADOR Y CALENDARIO ---
st.divider()
st.title("📊 Cotizá tu evento")
st.warning("⚠️ **Precios vigentes hasta el 31 de Mayo de 2026**")

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
    "Evento (Solo Fotos)": {"base": 215000, "con_drone": 300000, "desc": "Cobertura fotográfica completa."},
    "Cumpleaños Infantil": {"base": 220000, "con_drone": 290000, "desc": "3hs de cobertura, fotos ilimitadas y clip de video resumen."},
    "Baby Shower": {"base": 200000, "con_drone": 280000, "desc": "3hs de cobertura, fotos ilimitadas y clip de video resumen."},
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
    con_drone = st.checkbox("¿Incluir tomas con drone 4K?")
with c2:
    lugar_evento = st.selectbox("¿Departamento?", list(DEPARTAMENTOS.keys()))

datos = SERVICIOS[servicio_nom]
total_final = (datos["con_drone"] if con_drone else datos["base"]) + (DEPARTAMENTOS[lugar_evento] * 1200)

st.write("<br>", unsafe_allow_html=True) # Espacio extra

# Métrica de Streamlit
st.metric(label="Presupuesto Estimado", value=f"${total_final:,.0f}")
st.info(f"📝 **Incluye:** {datos['desc']} | ☁️ **Entrega vía Google Drive**.")

# --- NUEVA SECCIÓN: FORMAS DE PAGO ---
st.write("<br>", unsafe_allow_html=True)
st.subheader("💳 Formas de Pago y Reserva")

pay_col1, pay_col2, pay_col3 = st.columns(3)

with pay_col1:
    st.markdown("""
        <div class="pago-card">
            <h4>💵 Efectivo / Transferencia</h4>
            <p style="font-size: 14px; color: #b0b0b0;">Aboná de forma directa de manera rápida.</p>
        </div>
    """, unsafe_allow_html=True)

with pay_col2:
    st.markdown("""
        <div class="pago-card">
            <h4>🍊 Tarjeta Naranja X</h4>
            <p style="font-size: 14px; color: #b0b0b0;">Financiá la cobertura de tu evento con Naranja X.</p>
        </div>
    """, unsafe_allow_html=True)

with pay_col3:
    st.markdown("""
        <div class="pago-card">
            <h4>📅 Congelá la Fecha</h4>
            <p style="font-size: 14px; color: #b0b0b0;">Asegurá tu día reservando con una seña del 50%. El saldo restante se cancela el día del evento.</p>
        </div>
    """, unsafe_allow_html=True)


# --- 8. BOTÓN DE WHATSAPP (Avanzado) ---
mi_numero = "5492645164757"
texto_mensaje = f"Hola Diego! Coticé un '{servicio_nom}' en {lugar_evento}. Total estimado: ${total_final:,.0f}. Me gustaría coordinar los detalles y consultar por el pago con Naranja X."
link_wa = f"https://wa.me/{mi_numero}?text={urllib.parse.quote(texto_mensaje)}"

# Usamos HTML para inyectar el botón con nuestro estilo CSS
st.markdown(f"""
    <a href="{link_wa}" target="_blank" class="btn-whatsapp">
        📱 Enviar presupuesto por WhatsApp
    </a>
""", unsafe_allow_html=True)

st.markdown("<br><hr><center style='color: #666; font-size: 14px;'>© 2026 DL Fotografía y Video | Albardón, San Juan</center>", unsafe_allow_html=True)
