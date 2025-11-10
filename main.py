import streamlit as st
from PIL import Image

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
    .box-container {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 30px;
        margin-top: 50px;
    }
    .box {
        background-color: #111111;
        border: 2px solid #00BFFF;
        border-radius: 15px;
        padding: 30px 40px;
        width: 250px;
        text-align: center;
        transition: 0.3s;
    }
    .box:hover {
        transform: scale(1.05);
        background-color: #1a1a1a;
        border-color: #1E90FF;
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

# --- CENTERED BOXES ---
st.markdown("""
<div class="box-container">

    <div class="box">
        <a href="/" target="_self">
            <h3>🏠 Main</h3>
            <p>Return to the main landing page.</p>
        </a>
    </div>

    <div class="box">
        <a href="/1_Coding" target="_self">
            <h3>💻 Code</h3>
            <p>Explore my coding projects and apps.</p>
        </a>
    </div>

    <div class="box">
        <a href="/2_Art" target="_self">
            <h3>🎨 Artwork</h3>
            <p>View my digital and AI artwork gallery.</p>
        </a>
    </div>

    <div class="box">
        <a href="/3_About_Me" target="_self">
            <h3>🙋 About Me</h3>
            <p>Learn more about who I am and what I do.</p>
        </a>
    </div>

</div>
""", unsafe_allow_html=True)

st.divider()
st.info("💡 Tip: Use the sidebar or the boxes above to navigate between pages!")


  
