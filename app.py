import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.set_page_config(page_title="Lienzo Mágico", page_icon="✨")
st.title("🎀 Lienzo Mágico de Colores 🎀")

with st.sidebar:
    st.subheader("🌸 Opciones del Lienzo 🌸")
    
    drawing_mode = st.selectbox(
        "🧚‍♀️ Elige tu herramienta mágica:",
        ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
    )

    stroke_width = st.slider('✨ Grosor del pincel mágico ✨', 1, 30, 10)
    stroke_color = st.color_picker("🎨 Elige tu color favorito:", "#FF69B4")
    
    bg_base_color = st.color_picker("🌈 Color del fondo:", "#FFF0F5")
    bg_opacity = st.slider("🌫️ Transparencia del fondo (0 = invisible, 1 = opaco)", 0.0, 1.0, 1.0, 0.05)
    
    # Convertir color HEX a rgba con opacidad
    def hex_to_rgba(hex_color, alpha):
        hex_color = hex_color.lstrip('#')
        r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        return f"rgba({r}, {g}, {b}, {alpha})"
    
    bg_color = hex_to_rgba(bg_base_color, bg_opacity)

# Crear el componente de dibujo
canvas_result = st_canvas(
    fill_color="rgba(255, 192, 203, 0.4)",  # rosado pastel con transparencia
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=350,
    width=550,
    drawing_mode=drawing_mode,
    key="canvas_magico",
)
