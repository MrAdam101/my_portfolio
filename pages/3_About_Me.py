import streamlit as st

st.set_page_config(page_title="🙋 About Me", page_icon="🙋", layout="wide")

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
st.title("🙋 About Me")
st.write("""
Hi, I'm **Adam Conroy**, a creative English teacher, developer, and digital artist from **Seoul, South Korea**.

I combine **AI**, **coding**, and **art** to build tools and visuals that inspire and innovate.  
Whether I’m generating designs, creating web apps, or coding automation tools,  
I’m driven by curiosity, creativity, and purpose.
""")

st.markdown("### 📫 Connect With Me")
st.write("""
- **GitHub:** [github.com/adamconroy](https://github.com/adamconroy)
- **YouTube:** [SuperTrainerAC](https://www.youtube.com/@supertrainerac)
- **Email:** adamconroy@gmail.com
""")

# --- BACK BUTTON ---
if st.button("🏠 Back to Main", key="back_main_about"):
    st.switch_page("main")
