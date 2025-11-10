import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="🎨 Art Portfolio", page_icon="🎨", layout="wide")

st.title("🎨 My Art Portfolio")
st.write("""
A curated selection of my **digital artwork** — combining AI-assisted generation,
illustration, and design elements inspired by modern creativity.
""")

image_folder = "images"
if os.path.exists(image_folder):
    images = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    for img in images:
        st.image(os.path.join(image_folder, img), use_container_width=True)
else:
    st.info("🖼️ Add some images to the `images` folder to showcase your artwork here.")

if st.button("🏠 Back to Main"):
    st.switch_page("main.py")
