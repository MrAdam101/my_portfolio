import streamlit as st

st.set_page_config(page_title="💻 Coding Projects", page_icon="💻", layout="wide")

st.title("💻 My Coding Projects")
st.write("""
Here you'll find a collection of my Python, Streamlit, and creative coding projects —
tools and apps built to blend **AI, automation, and art** together.
""")

st.markdown("### 🧠 Featured Projects")
st.write("- **QR Code Generator App** – Create premium-style QR codes with logos and SVG exports.")
st.write("- **Report Card Generator** – Automatically generates ESL student reports.")
st.write("- **Wedding Guest List App** – Organize and categorize events with countdown timers.")
st.write("- **AI Art Dashboard** – Generates themed digital art directly from prompts.")

if st.button("🏠 Back to Main"):
    st.switch_page("main.py")
