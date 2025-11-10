import streamlit as st

st.set_page_config(page_title="🙋 About Me", page_icon="🙋", layout="wide")

st.title("🙋 About Me")
st.write("""
Hello! I'm **Adam Conroy**, a creative English teacher, developer,
and digital artist based in **Seoul, South Korea**.

I’m passionate about combining **AI, code, and art** to create tools and visuals that inspire.
Whether it’s building Streamlit apps, generating designs, or coding automation —
I love exploring how creativity and logic meet.
""")

st.markdown("### 📫 Connect With Me")
st.write("""
- **GitHub:** [github.com/adamconroy](https://github.com/adamconroy)
- **YouTube:** [SuperTrainerAC](https://www.youtube.com/@supertrainerac)
- **Email:** adamconroy@gmail.com
""")

if st.button("🏠 Back to Main"):
    st.switch_page("main.py")
