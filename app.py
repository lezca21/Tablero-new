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
    bg_color = '#FFF0F5'  # rosadito suave

# Crear el componente de dibujo
canvas_result = st_canvas(
    fill_color="rgba(255, 192, 203, 0.4)",  # rosado pastel con transparencia
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=550,
    width=850,
    drawing_mode=drawing_mode,
    key="canvas_magico",
)
