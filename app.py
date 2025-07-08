import streamlit as st
from pathlib import Path

# Configuración de la página
st.set_page_config(
    page_title="Plant-Based Dumplings",
    page_icon="🥟",
    layout="centered"
)

# Ruta de imágenes
IMAGE_DIR = Path(__file__).parent

# Logo principal (imagen 5) al inicio, centrado
grid_logo = st.columns([1, 3, 1])
grid_logo[1].image(
    str(IMAGE_DIR / "5.png"),
    caption="Plant-Based Dumplings",
    use_container_width=True
)

# Instrucciones
st.write("**Deslizá o usá el cursor para ver nuestros productos:**")

# Lista de imágenes de producto
product_images = ["1.png", "2.png", "4.png"]

# Selector interactivo (slider) para navegar
i = st.slider("Seleccioná el producto", 1, len(product_images), 1)
selected_img = product_images[i-1]

# Mostrar imagen seleccionada
st.image(
    str(IMAGE_DIR / selected_img),
    use_container_width=True
)

# Botón de contacto WhatsApp para todos los productos
whatsapp_number = st.secrets.get("WHATSAPP_NUMBER", "5491124618125")
message = "¡Hola! Quiero más información sobre sus dumplings plant-based."
url = f"https://api.whatsapp.com/send?phone={whatsapp_number}&text={message}"

st.markdown(
    f"[👉 Pedir ahora por WhatsApp 👈]({url})",
    unsafe_allow_html=True
)
