import streamlit as st
from pathlib import Path
import urllib.parse

# Configuración de la página
st.set_page_config(
    page_title="Plant-Based Dumplings",
    page_icon="🥟",
    layout="centered"
)

# Ruta de imágenes (carpeta actual)
IMAGE_DIR = Path.cwd()

# Logo principal (imagen 5) al inicio, centrado
grid_logo = st.columns([1, 3, 1])
grid_logo[1].image(
    str(IMAGE_DIR / "5.png"),
    caption="Plant-Based Dumplings",
    use_container_width=True
)

# Instrucciones
st.write("**Deslizá o usá el cursor para ver nuestros productos:**")

# Lista de imágenes de producto (sin la 3)
product_images = ["1.png", "2.png", "4.png"]

# Selector interactivo (slider) para navegar
i = st.slider("Seleccioná el producto", 1, len(product_images), 1)
selected_img = product_images[i - 1]

# Mostrar imagen seleccionada sin texto extra
st.image(
    str(IMAGE_DIR / selected_img),
    use_container_width=True
)

# Número de WhatsApp seguro desde secrets.toml
whatsapp_number = st.secrets.get("WHATSAPP_NUMBER", None)

if not whatsapp_number:
    st.error("Número de WhatsApp no configurado en secrets.toml")
else:
    # Mensaje para WhatsApp (url encode)
    message = "¡Hola! Quiero más información sobre sus dumplings plant-based."
    encoded_message = urllib.parse.quote(message)
    url = f"https://api.whatsapp.com/send?phone={whatsapp_number}&text={encoded_message}"

    # Botón para abrir WhatsApp
    if st.button("👉 Pedir ahora por WhatsApp 👈"):
        st.markdown(f"[Abrir WhatsApp]({url})", unsafe_allow_html=True)
