import streamlit as st

st.set_page_config(page_title="Adam Conroy | Portfolio", page_icon="🎨", layout="wide")

# --- DARK THEME STYLING ---
st.markdown("""
<style>
body {
    background-color: #000000;
    color: white;
    text-align: center;
}
[data-testid="stAppViewContainer"] {
    background-color: #000000;
    color: white;
}
[data-testid="stHeader"] {
    background: none;
}
[data-testid="stSidebar"] {
    background-color: #111111;
}
h1, h2, h3, h4, h5, h6, p, li, div, span {
    color: white !important;
    text-align: center !important;
}
a {
    color: #00BFFF !important;
    text-decoration: none;
}
a:hover {
    color: #1E90FF !important;
}
.button-container {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 40px;
    margin-top: 60px;
}
.image-button {
    background-color: #111111;
    border: 2px solid #00BFFF;
    border-radius: 20px;
    padding: 20px;
    width: 220px;
    transition: 0.3s;
    text-align: center;
}
.image-button:hover {
    transform: scale(1.05);
    background-color: #1a1a1a;
    border-color: #1E90FF;
}
.image-button img {
    width: 150px;
    height: 150px;
    object-fit: contain;
    border-radius: 15px;
}
.image-button h3 {
    margin-top: 10px;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.title("🎨 Adam Conroy | Creative Coder & Artist")
st.subheader("Welcome to my interactive portfolio built with Streamlit!")
st.write(
    """
    Explore my **coding projects**, **artwork**, and learn more **about me** using the image buttons below.  
    This portfolio showcases my passion for blending creativity and technology.
    """
)

# --- IMAGE BUTTONS ---
st.markdown(
"""<div class="button-container">
<div class="image-button">
  <a href="/" target="_self">
    <img src="images/main.png" alt="Main Button">
    <h3>🏠 Main</h3>
  </a>
</div>
<div class="image-button">
  <a href="1_Coding" target="_self">
    <img src="images/code.png" alt="Code Button">
    <h3>💻 Code</h3>
  </a>
</div>
<div class="image-button">
  <a href="2_Art" target="_self">
    <img src="images/art.png" alt="Art Button">
    <h3>🎨 Art</h3>
  </a>
</div>
<div class="image-button">
  <a href="3_About_Me" target="_self">
    <img src="images/about.png" alt="About Button">
    <h3>🙋 About</h3>
  </a>
</div>
</div>""",
unsafe_allow_html=True
)

st.divider()
st.info("💡 Click an image above to explore different sections of my portfolio!")
