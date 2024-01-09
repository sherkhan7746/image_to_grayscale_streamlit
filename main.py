import streamlit as st
from PIL import Image
uploaded_image = st.file_uploader("Upload Image")
with st.expander("Start Camera"):
    camera_image = st.camera_input("camera")

if uploaded_image:
    img = Image.open(uploaded_image)

    grayscale_image = img.convert("L")

    st.image(grayscale_image)
if camera_image:
    img = Image.open(camera_image)

    grayscale_image = img.convert("L")

    st.image(grayscale_image)