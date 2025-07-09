import streamlit as st
from pathlib import Path
import urllib.parse
import base64

# Configuración de la página
st.set_page_config(
    page_title="Plant-Based Dumplings",
    page_icon="🥟",
    layout="centered"
)

# Ruta base
BASE_DIR = Path.cwd()

# Función para convertir imagen a base64
def img_to_base64(img_path):
    with open(img_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Logo principal (imagen 5), centrado
grid_logo = st.columns([1, 3, 1])
grid_logo[1].image(
    str(BASE_DIR / "5.png"),
    caption="Plant-Based Dumplings",
    use_container_width=True
)

# WhatsApp número desde secrets.toml
whatsapp_number = st.secrets.get("WHATSAPP_NUMBER", None)

# Mensaje para WhatsApp
message = "¡Hola! Quiero más información sobre sus dumplings plant-based."

# Mostrar logo oficial de WhatsApp como botón justo debajo del logo principal
whatsapp_logo_path = BASE_DIR / "whatsapp_logo.png"

if whatsapp_number and whatsapp_logo_path.exists():
    whatsapp_url = f"https://api.whatsapp.com/send?phone={whatsapp_number}&text={urllib.parse.quote(message)}"
    b64_img = img_to_base64(whatsapp_logo_path)
    grid_logo[1].markdown(
        f'''
        <div style="text-align: center; margin-top: 10px;">
            <a href="{whatsapp_url}" target="_blank" style="display: inline-block;">
                <img src="data:image/png;base64,{b64_img}" alt="WhatsApp" width="48" height="48" style="cursor:pointer;">
            </a>
        </div>
        ''',
        unsafe_allow_html=True
    )
else:
    st.warning("Número de WhatsApp o logo no encontrado. Asegurate de tener 'whatsapp_logo.png' y el número en secrets.toml")

# Historia y descripción
st.markdown("""
### 🥟 ¿Qué son los dumplings?
Los dumplings son pequeños paquetes de masa rellenos, originarios de Asia. En culturas como la china, se preparan al vapor, a la plancha o hervidos y suelen compartirse en reuniones familiares. Simbolizan abundancia y buena fortuna.

### 🌿 Nuestra versión plant-based
Nuestros dumplings están hechos con ingredientes 100% vegetales, sin ajo ni cebolla.

- **Masa**: Harina de trigo candeal, espinaca y zanahoria.
- **Relleno**: Espinaca, zanahoria, jengibre, aceite de sésamo y condimentos taiwaneses.

Una receta equilibrada, sabrosa y pensada para todos los paladares.
""")

# Botón para descargar la receta
receta_path = BASE_DIR / "recetas.pdf"

if receta_path.exists():
    with open(receta_path, "rb") as file:
        st.download_button(
            label="📄 Descargar receta completa",
            data=file,
            file_name="recetas-dumplings.pdf",
            mime="application/pdf"
        )
else:
    st.warning("Archivo de receta no encontrado. Asegurate de tener 'recetas.pdf' en la misma carpeta.")

# Instrucción para ver productos
st.write("**Deslizá o usá el cursor para ver nuestros productos:**")

# Lista de imágenes de producto
product_images = ["1.png", "2.png", "4.png"]

# Slider para seleccionar imagen
i = st.slider("Seleccioná el producto", 1, len(product_images), 1)
selected_img = product_images[i - 1]

# Mostrar imagen seleccionada
st.image(
    str(BASE_DIR / selected_img),
    use_container_width=True
)
