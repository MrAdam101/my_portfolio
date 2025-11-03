import streamlit as st

# --- Page Setup ---
st.set_page_config(
    page_title="Adam Conroy | Portfolio",
    page_icon="🌐",
    layout="centered"
)

# --- Custom Styling ---
st.markdown("""
    <style>
        .main-title {
            font-size: 48px;
            font-weight: bold;
            text-align: center;
            color: #2E86C1;
        }
        .subtitle {
            text-align: center;
            font-size: 22px;
            color: #555;
            margin-top: -10px;
        }
        .section {
            text-align: center;
            font-size: 18px;
            margin-top: 40px;
        }
        .stButton button {
            display: block;
            margin: 10px auto;
            border-radius: 10px;
            font-size: 18px;
            background-color: #2E86C1;
            color: white;
            padding: 0.6em 1.4em;
            transition: 0.3s;
        }
        .stButton button:hover {
            background-color: #1B4F72;
            color: #f1f1f1;
        }
    </style>
""", unsafe_allow_html=True)

# --- Main Content ---
st.markdown('<h1 class="main-title">Welcome to My Portfolio 🌟</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">A blend of Creativity 🎨 + Code 💻</p>', unsafe_allow_html=True)

st.markdown("""
<div class="section">
I'm <b>Adam Conroy</b> — a coder, artist, and creator living in South Korea 🇰🇷.<br>
I build creative digital tools and art that bridge imagination with technology.<br><br>
</div>
""", unsafe_allow_html=True)

# --- Navigation Buttons ---
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("💻 Coding"):
        st.switch_page("pages/1_Coding.py")

with col2:
    if st.button("🎨 Art"):
        st.switch_page("pages/2_Art.py")

with col3:
    if st.button("🙋‍♂️ About Me"):
        st.switch_page("pages/3_About_Me.py")

st.markdown("""
<div class="section">
✨ Use the sidebar or the buttons above to explore my coding projects, artwork, and story.<br>
Let's create something amazing together!
</div>
""", unsafe_allow_html=True)
