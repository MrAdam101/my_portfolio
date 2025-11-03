import streamlit as st

st.set_page_config(page_title="Coding Projects", page_icon="💻", layout="centered")

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
            st.switch_page("../main")
    with col2:
        if st.button("💻 Coding"):
            st.experimental_rerun()
    with col3:
        if st.button("🎨 Art"):
            st.switch_page("pages/2_Art")
    with col4:
        if st.button("🙋‍♂️ About Me"):
            st.switch_page("pages/3_About_Me")

    st.markdown('</div>', unsafe_allow_html=True)

# --- NAVIGATION BAR ---
top_navbar()

st.title("💻 My Coding Projects")

st.write("""
Here are some of the coding skills and projects I’ve worked on:
""")

st.subheader("🧠 Skills")
skills = ["Python 🐍", "JavaScript ⚡", "HTML & CSS 🌐", "Streamlit 🧩", "AI Tools 🤖"]
st.write(", ".join(skills))

st.subheader("🚀 Projects")
st.markdown("""
- **QR Code Generator App** – Built with Streamlit and Python  
- **Wedding Guest Manager** – Dynamic guest list app  
- **Report Card Generator** – Automates English student reports  
- **Art Gallery App** – Displays my digital illustrations
""")
