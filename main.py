import streamlit as st

st.set_page_config(page_title="Adam Conroy | Portfolio", page_icon="🎨", layout="wide")

# --- HIDE SIDEBAR ---
st.markdown("""
    <style>
        [data-testid="stSidebar"] {visibility: hidden;}
        [data-testid="stSidebarNav"] {display: none;}
        [data-testid="stToolbar"] {display: none;}
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- BLUE THEME STYLING ---
st.markdown("""
<style>
body {
    background-color: #B3E5FC; /* Fresh light blue */
    color: black;
    text-align: center;
    font-family: 'Segoe UI', sans-serif;
}
[data-testid="stAppViewContainer"] {
    background-color: #B3E5FC;
    color: black;
}
h1, h2, h3, h4, h5, h6, p, li, div, span {
    color: black !important;
    text-align: center !important;
}
.button-container {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 35px;
    margin-top: 50px;
}
.glow-button {
    background: linear-gradient(180deg, #2196F3, #1976D2);
    border: none;
    border-radius: 40px;
    padding: 18px 45px;
    color: white;
    font-size: 1.3rem;
    font-weight: 700;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 5px 20px rgba(25, 118, 210, 0.4);
    transition: all 0.3s ease-in-out;
    cursor: pointer;
}
.glow-button:hover {
    background: linear-gradient(180deg, #1976D2, #0D47A1);
    box-shadow: 0 0 25px rgba(25, 118, 210, 0.9);
    transform: scale(1.08);
}
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<h1>🎨 Adam Conroy | Creative Coder & Artist Portfolio</h1>", unsafe_allow_html=True)
st.markdown("""
<h3>Welcome to my interactive portfolio built with code and creativity — 
showcasing my coding skills along with my artwork.</h3>
<p>Explore my <b>coding projects</b>, <b>artwork</b>, and learn more <b>about me</b>.</p>
<p>This portfolio represents my passion for blending technology and design.</p>
""", unsafe_allow_html=True)

# --- NAVIGATION BUTTONS ---
col1, col2, col3, col4 = st.columns(4, gap="large")

with col1:
    st.markdown('<button class="glow-button">🏠 Main</button>', unsafe_allow_html=True)

with col2:
    if st.button("💻 Code", use_container_width=True):
        st.switch_page("pages/1_Coding.py")

with col3:
    if st.button("🎨 Art", use_container_width=True):
        st.switch_page("pages/2_Art.py")

with col4:
    if st.button("🙋 About Me", use_container_width=True):
        st.switch_page("pages/3_About_Me.py")
