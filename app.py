import streamlit as st
import random
import time
from streamlit_extras.let_it_rain import rain

# ----------------- PAGE SETUP -----------------
st.set_page_config(page_title="String Game 🎮", page_icon="🌸", layout="centered")

# Custom CSS for Aesthetic Background + Fonts
st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #fbc2eb 0%, #a6c1ee 100%);
            font-family: 'Comic Sans MS', cursive, sans-serif;
            color: #4a148c;
        }
        .stTextInput input {
            border-radius: 15px;
            border: 2px solid #ff80ab;
            padding: 10px;
            font-size: 18px;
        }
        .result-card {
            background-color: #fff0f6;
            border-radius: 15px;
            padding: 15px;
            text-align: center;
            margin-top: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# ----------------- APP TITLE -----------------
st.markdown("<h1 style='text-align:center;'>🌸 Word Arena 🎮</h1>", unsafe_allow_html=True)
st.write("Welcome, player! Enter a word and let’s see what happens ✨")

# ----------------- SCORE INIT -----------------
if "score" not in st.session_state:
    st.session_state.score = 0

# ----------------- USER INPUT -----------------
user_input = st.text_input("✨ Type your word here:")

if st.button("Play 🎲"):
    if user_input:
        # Reverse the string
        reversed_str = user_input[::-1]

        # Check palindrome
        is_palindrome = user_input.lower() == reversed_str.lower()

        # Result Card
        st.markdown(
            f"<div class='result-card'>"
            f"<h3>🔄 Reversed Word:</h3>"
            f"<p style='font-size:22px; color:#ff1493;'><b>{reversed_str}</b></p>"
            f"</div>", unsafe_allow_html=True
        )

        # Game Scoring
        gained = random.randint(5, 15)
        if is_palindrome:
            st.success(f"💖 Woohoo! '{user_input}' is a Palindrome! +20 points 🎉")
            st.session_state.score += 20
            rain(emoji="✨", font_size=54, falling_speed=5, animation_length=3)
        else:
            st.error(f"🙈 Nope, '{user_input}' is not a Palindrome. But you still get +{gained} points ✨")
            st.session_state.score += gained

        # Update Scoreboard
        st.markdown(
            f"<div class='result-card'>"
            f"<h2>🏆 Your Score: {st.session_state.score}</h2>"
            f"</div>", unsafe_allow_html=True
        )

        # Animation
        st.balloons()
    else:
        st.warning("⚠️ Please type a word first!")
