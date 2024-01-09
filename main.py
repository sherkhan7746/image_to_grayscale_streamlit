import streamlit as st
from PIL import Image

with st.expander("Start Camera"):
    camera_image = st.camera_input("camera")

if camera_image:
    img = Image.open(camera_image)

    grayscale_image = img.convert("L")

    st.image(grayscale_image)