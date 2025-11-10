import streamlit as st

st.set_page_config(page_title="💻 Coding Projects", page_icon="💻", layout="wide")

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
st.title("💻 My Coding Projects")
st.write("""
A showcase of my creative **Python** and **Streamlit** projects blending technology with art.
""")

st.markdown("### 🧠 Featured Projects")
st.write("- **QR Code Generator App** – Premium customizable QR codes with branding.")
st.write("- **Report Card Generator** – Auto-creates unique ESL student reports.")
st.write("- **Wedding Guest Manager** – Elegant dashboard with countdown and guest tracking.")
st.write("- **AI Art Dashboard** – Generate themed digital art through custom prompts.")

# --- BACK BUTTON ---
if st.button("🏠 Back to Main", key="back_main"):
    st.switch_page("main")
