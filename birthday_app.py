import streamlit as st
from datetime import datetime

# Page Config
st.set_page_config(
    page_title="Happy Birthday Boss 🎉",
    layout="centered"
)

# ✨ Gradient Background & Full Style Fix
custom_css = """
<style>
/* Background for entire app */
.stApp {
    background: linear-gradient(to right, #fc466b, #3f5efb);
    background-attachment: fixed;
    background-size: cover;
    font-family: 'Segoe UI', sans-serif;
    color: white;
}

/* Center text styling */
h1, h2, h3, p {
    text-align: center;
    color: white;
}

/* Card glass effect */
.card {
    background-color: rgba(255, 255, 255, 0.1);
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    margin-top: 50px;
    color: white;
}

/* Hide default Streamlit header and footer */
header, footer {
    visibility: hidden;
}
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# ❄️ Confetti or Snow Animation
st.snow()
st.balloons()

# 🕛 Clock
now = datetime.now().strftime("%H:%M:%S")
st.markdown(f"<h3>⏰ Current Time: {now}</h3>", unsafe_allow_html=True)

# 🎂 Birthday Card Content
st.markdown("""
<div class='card'>
    <h1>🎉 Happy Birthday Sir Muneeb 🎂</h1>
    <h2>Wishing you a day full of joy, success, and happiness!</h2>
    <p>May all your dreams come true and your journey ahead be filled with endless accomplishments.</p>
    <br>
    <h3>— From Fatima Zehra✨</h3>
</div>
""", unsafe_allow_html=True)
