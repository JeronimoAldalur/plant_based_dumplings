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

# Lista de imágenes de producto (sin la 3 que sacaste)
product_images = ["1.png", "2.png", "4.png"]

# Selector interactivo (slider) para navegar
i = st.slider("Seleccioná el producto", 1, len(product_images), 1)
selected_img = product_images[i - 1]

# Mostrar imagen seleccionada
st.image(
    str(IMAGE_DIR / selected_img),
    use_container_width=True
)

# Número de WhatsApp seguro desde secrets.toml
whatsapp_number = st.secrets["WHATSAPP_NUMBER"]

# Mensaje que se enviará por WhatsApp (url encode para espacios y símbolos)
import urllib.parse
message = "¡Hola! Quiero más información sobre sus dumplings plant-based."
encoded_message = urllib.parse.quote(message)

url = f"https://api.whatsapp.com/send?phone={whatsapp_number}&text={encoded_message}"

# Botón para abrir WhatsApp
st.markdown(
    f"[👉 Pedir ahora por WhatsApp 👈]({url})",
    unsafe_allow_html=True
)
