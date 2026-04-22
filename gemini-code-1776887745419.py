import streamlit as st
import urllib.parse

# Configuración visual
st.set_page_config(page_title="Presupuestador DL Fotografía", page_icon="📷")

st.title("📷 DL Fotografía y Video")
st.subheader("Calculadora de Presupuestos")

# --- ENTRADAS DEL USUARIO ---
servicio = st.selectbox(
    "Seleccione el servicio:",
    ["Sesión Retrato/Bebé (2hs)", "Evento 15/18 años", "Boda Completa", "Bautismo (Iglesia + Fiesta)", "Evento (Solo Fotos)"]
)

con_drone = st.checkbox("¿Incluir servicio de Drone (4K)?")

distancia = st.number_input("KM fuera de Albardón (ida y vuelta):", min_value=0, step=2)

# --- LÓGICA DE PRECIOS ---
total = 0
detalles = ""

if servicio == "Sesión Retrato/Bebé (2hs)":
    total = 40000
    detalles = "50-70 fotos digitales."
elif servicio == "Evento 15/18 años":
    total = 300000 if con_drone else 230000
    detalles = "6hs de cobertura, +100 fotos y 1 video."
elif servicio == "Boda Completa":
    total = 370000 if con_drone else 300000
    detalles = "Civil, Iglesia y Fiesta. +200 fotos y 2 videos."
elif servicio == "Bautismo (Iglesia + Fiesta)":
    total = 230000
    detalles = "+100 fotos y 1 video."
elif servicio == "Evento (Solo Fotos)":
    total = 180000
    detalles = "Cobertura fotográfica profesional."

# Viáticos ($1000 c/ 2km)
viaticos = (distancia / 2) * 1000
total_final = total + viaticos

# --- MOSTRAR RESULTADO ---
st.divider()
st.header(f"Total: ${total_final:,.0f}")
st.write(f"**Incluye:** {detalles}")

# --- BOTÓN DE WHATSAPP ---
# REEMPLAZA LAS X CON TU NÚMERO (Ejemplo: 5492645556677)
mi_numero = "5492645164757" 

texto_mensaje = f"Hola Diego! Coticé un servicio de {servicio}. Total: ${total_final:,.0f}. ¿Tenés disponibilidad?"
mensaje_url = urllib.parse.quote(texto_mensaje)
link_whatsapp = f"https://wa.me/{mi_numero}?text={mensaje_url}"

st.write("---")
st.write("¿Te interesa este presupuesto?")
st.link_button("📱 Consultar por WhatsApp", link_whatsapp)
st.divider()
st.subheader("📅 Consultá mi disponibilidad")
st.write("Fijate si tengo la fecha libre antes de consultar.")

# Usamos tu link dentro del formato que entiende Streamlit
calendar_html = """
<iframe src="https://calendar.google.com/calendar/embed?src=goliat4750%40gmail.com&ctz=America%2FArgentina%2FCordoba" 
style="border: 0" width="100%" height="600" frameborder="0" scrolling="no"></iframe>
"""

st.markdown(calendar_html, unsafe_allow_code=True)
