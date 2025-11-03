import streamlit as st

# --- Page Setup ---
st.set_page_config(
    page_title="Adam Conroy | Portfolio",
    page_icon="🌐",
    layout="centered"
)

# --- NAVIGATION BAR FUNCTION ---
def top_navbar():
    st.markdown("""
        <style>
            .nav-buttons {
                display: flex;
                justify-content: center;
                gap: 1rem;
                margin-bottom: 2rem;
            }
            .stButton button {
                background-color: #2E86C1;
                color: white;
                border-radius: 8px;
                font-size: 16px;
                padding: 0.5em 1em;
                border: none;
                transition: 0.3s;
            }
            .stButton button:hover {
                background-color: #1B4F72;
                color: #f1f1f1;
                transform: scale(1.05);
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="nav-buttons">', unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("🏠 Home"):
            st.switch_page("main.py")
    with col2:
        if st.button("💻 Coding"):
            st.switch_page("pages/1_Coding.py")
    with col3:
        if st.button("🎨 Art"):
            st.switch_page("pages/2_Art.py")
    with col4:
        if st.button("🙋‍♂️ About Me"):
            st.switch_page("pages/3_About_Me.py")
    st.markdown('</div>', unsafe_allow_html=True)


# --- NAVIGATION BAR ---
top_navbar()

# --- MAIN CONTENT ---
st.markdown("""
<h1 style='text-align:center; color:#2E86C1;'>Welcome to My Portfolio 🌟</h1>
<p style='text-align:center; font-size:20px; color:#555;'>A blend of Creativity 🎨 + Code 💻</p>
""", unsafe_allow_html=True)

st.markdown("""
<div style='text-align:center; font-size:18px; color:#333; margin-top:30px;'>
I'm <b>Adam Conroy</b> — a coder, artist, and creator living in South Korea 🇰🇷.<br>
I build creative digital tools and art that bridge imagination with technology.<br><br>
✨ Explore my projects, art, and story using the buttons above or the sidebar.<br>
Let's create something amazing together!
</div>
""", unsafe_allow_html=True)
