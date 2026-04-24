import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="DL Fotografía y Video", layout="wide")

# 2. TRUCO PARA QUITAR LA PROPAGANDA (CSS)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_style, unsafe_allow_html=True)

# 3. Encabezado con tu Logo
# Aquí usamos el logo que me pasaste
st.image("tu_logo.png", width=200) 

# 4. Título y mensaje de equipos profesionales
st.title("Capturando tus momentos más importantes")
st.subheader("Fotografía y Video con estándares de alta calidad")

col1, col2 = st.columns(2)

with col1:
    # Aquí pondríamos la foto tuya editando (foto3.jpg)
    st.image("foto3.jpg", caption="Post-producción con equipos profesionales")

with col2:
    st.write("""
    En **DL Fotografía y Video** no solo capturamos imágenes; creamos recuerdos duraderos. 
    Utilizamos tecnología de vanguardia, desde cámaras **Nikon** de alta resolución 
    hasta tomas aéreas con drone **Potensic Atom 2** para una perspectiva cinematográfica.
    """)

# 5. Tu Calculadora de Presupuestos (Tu lógica de Python va aquí abajo)
st.divider()
st.header("Calculá tu presupuesto")
# ... (Aquí pegas el código de la calculadora que ya tenías)
