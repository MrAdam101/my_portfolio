import streamlit as st

st.set_page_config(page_title="Adam Conroy | Portfolio", page_icon="🎨", layout="wide")

# --- HIDE STREAMLIT DEFAULT SIDEBAR AND MENU ---
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
body {
    background-color: #000000;
    color: white;
    text-align: center;
    font-family: 'Segoe UI', sans-serif;
}
[data-testid="stAppViewContainer"] {
    background-color: #000000;
}
h1, h2, h3, h4, h5, h6, p, li, div, span {
    color: white !important;
    text-align: center !important;
}
.button-container {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 35px;
    margin-top: 60px;
}
.glow-button {
    background: linear-gradient(180deg, #56CCF2, #2F80ED);
    border: none;
    border-radius: 40px;
    padding: 18px 45px;
    color: white;
    font-size: 1.3rem;
    font-weight: 700;
    display: inline-flex;
    align-items: center;
    justify-content: center;
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

# --- HEADER ---
st.title("🎨 Adam Conroy | Creative Coder & Artist")
st.subheader("Welcome to my interactive portfolio built with Streamlit!")
st.write(
    """
    Explore my **coding projects**, **artwork**, and learn more **about me** using the buttons below.  
    This portfolio showcases my passion for blending creativity and technology.
    """
)

# --- NAVIGATION BUTTONS ---
col1, col2, col3, col4 = st.columns(4, gap="large")

with col1:
    st.button("🏠 Main", use_container_width=True)

with col2:
    if st.button("💻 Code", use_container_width=True):
        st.switch_page("1_Coding")

with col3:
    if st.button("🎨 Art", use_container_width=True):
        st.switch_page("2_Art")

with col4:
    if st.button("🙋 About Me", use_container_width=True):
        st.switch_page("3_About_Me")
