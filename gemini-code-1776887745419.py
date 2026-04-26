import streamlit as st

def calcular_presupuesto():
    st.title("Calculadora de Presupuestos - DL Fotografía y Video")
    st.write("Tarifas Actualizadas - Abril 2026")

    # --- SELECCIÓN DE SERVICIO ---
    servicio = st.selectbox(
        "Seleccione el tipo de servicio:",
        ["Boda", "Quinceañera", "Sesión de Retrato / Book", "Evento Corporativo", "Publicidad / Producto"]
    )

    # --- DEFINICIÓN DE PRECIOS BASE (Nivelados) ---
    precios_base = {
        "Boda": 385000,
        "Quinceañera": 280000,
        "Sesión de Retrato / Book": 50000,
        "Evento Corporativo": 150000,
        "Publicidad / Producto": 120000
    }

    precio_final = precios_base[servicio]

    # --- SERVICIOS PREMIUM ---
    st.subheader("Servicios Adicionales")
    
    # El Drone ahora tiene un valor que refleja el mercado y el riesgo del equipo
    incluye_drone = st.checkbox("Cobertura Aérea 4K (Drone Potensic Atom 2)")
    if incluye_drone:
        precio_final += 85000  

    incluye_video = st.checkbox("Edición de Video High-End (CapCut/4K)")
    if incluye_video:
        precio_final += 45000

    # --- LOGÍSTICA ---
    st.subheader("Ubicación y Traslado")
    distancia = st.number_input("Distancia desde Albardón (km ida y vuelta):", min_value=0, value=0)
    costo_km = 1200  
    precio_final += (distancia * costo_km)

    # --- RESULTADO FINAL ---
    st.markdown("---")
    st.header(f"Total Presupuestado: ${precio_final:,.0f}")
    
    st.info("""
    **Detalles del Servicio:** Incluye cobertura profesional, edición avanzada en 
    Adobe Lightroom/Photoshop y entrega de archivos en alta resolución. 
    *Presupuesto sujeto a disponibilidad de fecha.*
    """)

if __name__ == "__main__":
    calcular_presupuesto()
