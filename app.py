import streamlit as st
from PIL import Image
import json
from streamlit_lottie import st_lottie
from streamlit_timeline import timeline

import time
import os

# ----- Setup -----
st.set_page_config(page_title="Shenbaga Ganeshan | AI Portfolio", layout="centered", page_icon="🧠")



# Load Assets
profile_img = Image.open("assets/profile.jpg")
with open("assets/lottie_ai.json") as f:
    lottie_ai = json.load(f)

# Dark Theme Styling
st.markdown("""
    <style>
    .gradient-text {
        font-size: 40px;
        font-weight: bold;
        background: linear-gradient(to right, #30CFD0, #330867);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)


# ----- Header -----
st.markdown('<h1 class="gradient-text">Shenbaga Ganeshan S</h1>', unsafe_allow_html=True)
st.image(profile_img, width=150, caption="AI & Data Science Student", use_container_width=True)

st.markdown("📫 [ganeshanshenbaga@gmail.com](mailto:ganeshanshenbaga@gmail.com) | [LinkedIn](https://linkedin.com/in/shenbaga-ganeshan-250a41256)")

# ----- Lottie Animation -----
st_lottie(lottie_ai, height=300, key="ai")

# ----- About Me -----
st.subheader("👨‍💼 About Me")
st.write("""
I'm an **AI student** with hands-on internship experience at **Ramco Cements**, where I built real-time cement bag counting and forecasting systems.  
I specialize in building AI pipelines using Python, ML, Computer Vision, and Prompt Engineering.
""")
with open("assets/ganesh_resume.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(
    label="📄 Download My Resume",
    data=PDFbyte,
    file_name="ganesh_resume.pdf",
    mime='application/octet-stream'
)


# ----- Skills -----
st.subheader("💻 Skills")
st.write("""
- Python 🐍  
- Java (Basic) ☕  
- SQL 🗃️  
- Prompt Engineering 🧠  
- OpenCV, YOLOv8  
- Streamlit, Flask
""")

# ----- Projects Carousel -----
st.subheader("🚀 Featured Projects")
project = st.radio("Select a Project", ["Cement Bag Counter", "Cement Forecasting"], horizontal=True)

if project == "Cement Bag Counter":
    st.markdown("""
    **Real-time Detection & Counting**  
    🔹 Used YOLOv8 + BoT-SORT  
    🔹 Live RTSP camera feed integration  
    🔹 Deployed for truck-wise cement tracking
    """)
elif project == "Cement Forecasting":
    st.markdown("""
    **Forecast Cement Flow Using AI**  
    🔹 Used synthetic data + regression models  
    🔹 Predicts daily truck count from patterns  
    🔹 Helps optimize truck loading schedules
    """)

# ----- Blog Section -----
st.subheader("📝 My AI Insights")
st.markdown("""
**🔍 Why Real-Time Vision Matters**  
In industries like cement and manufacturing, real-time object detection improves speed, safety, and accountability.

**📊 Forecasting = Power**  
Prediction isn’t just numbers — it's insight. With ML, we turn raw loading data into cost-saving intelligence.

**🎯 Prompting is Programming**  
Prompt engineering is the new coding skill — it lets you shape AI like never before!
""")

# ----- Footer -----
st.markdown("---")
st.markdown("Made with ❤️ by Shenbaga Ganeshan | © 2025")
st.subheader("📬 Contact Me")
st.markdown("""
<form action="https://formsubmit.co/shenbagaganeshan8@gmail.com" method="POST">
     <input type="text" name="name" placeholder="Your Name" required><br>
     <input type="email" name="email" placeholder="Your Email" required><br>
     <textarea name="message" placeholder="Your Message Here" rows="4" required></textarea><br>
     <button type="submit">Send Message</button>
</form>
""", unsafe_allow_html=True)


import sys

st.markdown("### 🔚 Want to close the app?")
if st.button("❌ Exit App Now"):
    st.markdown("## 👋 The app has been shut down. Please close this window.")
    st.markdown("Thanks for visiting!")
    time.sleep(2)
    os._exit(0)  # Kill backend

