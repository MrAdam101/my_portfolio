import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="🎨 Art Gallery", page_icon="🎨", layout="wide")

# --- HIDE SIDEBAR ---
st.markdown("""
    <style>
        [data-testid="stSidebar"] {visibility: hidden;}
        [data-testid="stSidebarNav"] {display: none;}
        [data-testid="stToolbar"] {display: none;}
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- STYLING ---
st.markdown("""
<style>
body {background-color: #000; color: white; text-align: center; font-family: 'Segoe UI', sans-serif;}
[data-testid="stAppViewContainer"] {background-color: #000;}
h1, h2, h3, h4, h5, h6, p, li, div, span {color: white !important; text-align: center !important;}
.glow-button {
    background: linear-gradient(180deg, #56CCF2, #2F80ED);
    border: none;
    border-radius: 40px;
    padding: 15px 40px;
    color: white;
    font-size: 1.1rem;
    font-weight: 700;
    box-shadow: 0 5px 20px rgba(0, 191, 255, 0.3);
    transition: all 0.3s ease-in-out;
    cursor: pointer;
}
.glow-button:hover {
    background: linear-gradient(180deg, #2F80ED, #1B6FF0);
    box-shadow: 0 0 25px rgba(0,191,255,0.8);
    transform: scale(1.08);
}
</style>
""", unsafe_allow_html=True)

# --- CONTENT ---
st.title("🎨 My Art Portfolio")
st.write("""
A curated selection of my **digital artwork** and **AI-assisted illustrations**.
""")

image_folder = "images"
if os.path.exists(image_folder):
    images = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    for img in images:
        st.image(os.path.join(image_folder, img), use_container_width=True)
else:
    st.info("🖼️ Add artwork images to an 'images' folder to display them here.")

# --- BACK BUTTON ---
if st.button("🏠 Back to Main", key="back_main_art"):
    st.switch_page("main")
