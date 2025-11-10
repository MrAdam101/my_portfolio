import streamlit as st
from PIL import Image

st.set_page_config(page_title="Adam Conroy | Portfolio", page_icon="🎨", layout="wide")

# --- DARK THEME STYLING ---
st.markdown("""
    <style>
    body {
        background-color: #000000;
        color: white;
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
    }
    a {
        color: #00BFFF !important;
        text-decoration: none;
    }
    a:hover {
        color: #1E90FF !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.title("🎨 Adam Conroy | Creative Coder & Artist")
st.subheader("Welcome to my interactive portfolio built with Streamlit!")
st.write(
    """
    Explore my **coding projects**, **artwork**, and learn more **about me** using the sidebar.  
    This portfolio showcases my passion for blending creativity and technology.
    """
)

# --- FEATURED SECTIONS ---
col1, col2 = st.columns(2, gap="large")

with col1:
    st.header("💻 Coding Projects")
    st.write(
        """
        Dive into my latest **Python** and **Streamlit** creations — 
        from automation tools to AI-powered web apps.
        """
    )
    st.page_link("pages/1_Coding.py", label="See My Code", icon="🧠")

with col2:
    st.header("🎨 Artwork")
    st.write(
        """
        A showcase of my **digital art**, **MidJourney illustrations**, 
        and other creative designs made with AI and hand-crafted detail.
        """
    )
    st.page_link("pages/2_Art.py", label="View My Art Gallery", icon="🖼️")

st.divider()
st.info("💡 Tip: Use the sidebar to navigate between pages!")

