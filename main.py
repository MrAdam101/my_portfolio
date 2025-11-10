import streamlit as st

st.set_page_config(page_title="Adam Conroy | Portfolio", page_icon="🎨", layout="wide")

# --- STYLING ---
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
    text-decoration: none !important;
}

/* --- BUTTON CONTAINER --- */
.button-container {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 35px;
    margin-top: 60px;
}

/* --- BUTTON STYLE --- */
.image-button {
    background: linear-gradient(180deg, #56CCF2, #2F80ED);  /* light-blue glossy gradient */
    border: none;
    border-radius: 40px;
    padding: 18px 45px;
    color: white;
    font-size: 1.3rem;
    font-weight: 700;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 5px 20px rgba(0, 191, 255, 0.3);
    transition: all 0.3s ease-in-out;
}
.image-button:hover {
    background: linear-gradient(180deg, #2F80ED, #1B6FF0);
    box-shadow: 0 0 25px rgba(0,191,255,0.8);
    transform: scale(1.08);
}
.image-button h3 {
    margin: 0;
    font-size: 1.3rem;
    color: white;
    font-weight: 700;
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

# --- BUTTONS ---
st.markdown("""
<div class="button-container">

<a href="/" target="_self" class="image-button">
  <h3>🏠 Main</h3>
</a>

<a href="1_Coding" target="_self" class="image-button">
  <h3>💻 Code</h3>
</a>

<a href="2_Art" target="_self" class="image-button">
  <h3>🎨 Art</h3>
</a>

<a href="3_About_Me" target="_self" class="image-button">
  <h3>🙋 About Me</h3>
</a>

</div>
""", unsafe_allow_html=True)

st.divider()
st.info("💡 Hover over the buttons to see the glowing blue effect!")
