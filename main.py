import streamlit as st

st.set_page_config(page_title="Adam Conroy | Portfolio", page_icon="🎨", layout="wide")

# --- HIDE SIDEBAR, TOOLBAR, FOOTER ---
st.markdown("""
    <style>
        [data-testid="stSidebar"] {visibility: hidden;}
        [data-testid="stSidebarNav"] {display: none;}
        [data-testid="stToolbar"] {display: none;}
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- MODERN BLUE STYLING ---
st.markdown("""
<style>
body {
    background-color: #B3E5FC;
    color: black;
    text-align: center;
    font-family: 'Segoe UI', sans-serif;
    margin: 0;
    padding: 0;
}
[data-testid="stAppViewContainer"] {
    background-color: #B3E5FC;
}
h1, h2, h3, h4, h5, h6, p, li, div, span {
    color: black !important;
    text-align: center !important;
}
.button-container {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 40px;
    flex-wrap: wrap;
    margin-top: 50px;
}
.glow-button {
    background: linear-gradient(180deg, #2196F3, #1976D2);
    border: none;
    border-radius: 50px;
    padding: 22px 55px;
    color: white;
    font-size: 1.3rem;
    font-weight: 700;
    text-decoration: none;
    box-shadow: 0 8px 20px rgba(25, 118, 210, 0.4);
    transition: all 0.3s ease-in-out;
    display: inline-block;
}
.glow-button:hover {
    background: linear-gradient(180deg, #1976D2, #0D47A1);
    box-shadow: 0 0 25px rgba(25,118,210,0.8);
    transform: scale(1.08);
}
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("""
<h1>🎨 Adam Conroy | Creative Coder & Artist Portfolio</h1>
<h3>Welcome to my interactive portfolio built with code and creativity — showcasing my coding skills along with my artwork.</h3>
<p>Explore my <b>coding projects</b>, <b>artwork</b>, and learn more <b>about me</b>.</p>
<p>This portfolio represents my passion for blending technology and design.</p>
""", unsafe_allow_html=True)

# --- CENTERED BUTTONS ---
st.markdown("""
<div class="button-container">
    <a href="/" target="_self" class="glow-button">🏠 Main</a>
    <a href="/1_Coding" target="_self" class="glow-button">💻 Code</a>
    <a href="/2_Art" target="_self" class="glow-button">🎨 Art</a>
    <a href="/3_About_Me" target="_self" class="glow-button">🙋 About Me</a>
</div>
""", unsafe_allow_html=True)
