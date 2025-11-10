import streamlit as st

st.set_page_config(page_title="Adam Conroy | Portfolio", page_icon="🎨", layout="wide")

# --- DARK THEME STYLING ---
st.markdown("""
<style>
body {
    background-color: #000000;
    color: white;
    text-align: center;
    font-family: 'Segoe UI', sans-serif;
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
    text-decoration: none !important;
}
a:hover {
    color: #1E90FF !important;
}
.button-container {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 30px;
    margin-top: 60px;
}
.image-button {
    background-color: #111111;
    border: 3px solid #00BFFF;
    border-radius: 25px;
    width: 150px;
    height: 150px;
    display: flex;
    justify-content: center;
    align-items: center;
    transition: 0.3s;
    box-shadow: 0 0 10px rgba(0,191,255,0.2);
}
.image-button:hover {
    transform: scale(1.1);
    border-color: #FF4500;
    box-shadow: 0 0 25px #FF4500;
    background-color: #1a1a1a;
}
.image-button h3 {
    margin: 0;
    font-size: 1.3rem;
    font-weight: 700;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.title("🎨 Adam Conroy | Creative Coder & Artist")
st.subheader("Welcome to my interactive portfolio built with Streamlit!")
st.write(
    """
    Explore my **coding projects**, **artwork**, and learn more **about me** using the buttons below.  
    This portfolio showcases my passion for blending creativity and technology.
    """
)

# --- SMALL EMOJI BUTTONS ---
st.markdown(
"""<div class="button-container">

<div class="image-button">
  <a href="/" target="_self">
    <h3>🏠 Main</h3>
  </a>
</div>

<div class="image-button">
  <a href="1_Coding" target="_self">
    <h3>💻 Code</h3>
  </a>
</div>

<div class="image-button">
  <a href="2_Art" target="_self">
    <h3>🎨 Art</h3>
  </a>
</div>

<div class="image-button">
  <a href="3_About_Me" target="_self">
    <h3>🙋 About Me</h3>
  </a>
</div>

</div>""",
unsafe_allow_html=True
)

st.divider()
st.info("💡 Hover over any button to see the glowing border effect!")

