import streamlit as st

# Page setup
st.set_page_config(page_title="Word Arena 🎮", page_icon="🕹️", layout="centered")

# Pixel art style with custom CSS
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

    body {
        background-color: #fdf6e3;
        color: #222;
        font-family: 'Press Start 2P', cursive;
    }
    .title {
        text-align: center;
        font-size: 28px;
        color: #ff006e;
        margin-bottom: 20px;
    }
    .result {
        font-size: 16px;
        padding: 15px;
        margin-top: 15px;
        border: 4px solid #ffbe0b;
        border-radius: 8px;
        background-color: #fbf8cc;
        color: #3a0ca3;
        text-align: center;
    }
    .stButton button {
        background-color: #ff006e !important;
        color: white !important;
        font-size: 14px !important;
        border-radius: 6px !important;
        padding: 8px 14px;
        font-family: 'Press Start 2P', cursive !important;
    }
    .option-label {
        color: #8338ec;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title
st.markdown("<div class='title'>🕹️ Word Arena 🎮</div>", unsafe_allow_html=True)

# Input
user_input = st.text_input("👉 Enter your string here:")

# Operation selection
operation = st.radio(
    "Choose your operation:",
    ["Reverse String", "Palindrome Check", "Toggle Case", "Find Length"],
    horizontal=False,
)

# Button
if st.button("Play! 🚀"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter something first!")
    else:
        if operation == "Reverse String":
            reversed_str = user_input[::-1]
            st.markdown(
                f"<div class='result'>🔄 Reversed: <b>{reversed_str}</b></div>",
                unsafe_allow_html=True,
            )

        elif operation == "Palindrome Check":
            reversed_str = user_input[::-1]
            if user_input.lower() == reversed_str.lower():
                st.markdown(
                    f"<div class='result'>🎉 Woohoo! <b>{user_input}</b> is a Palindrome! </div>",
                    unsafe_allow_html=True,
                )
                st.snow()
                st.balloons()
            else:
                st.markdown(
                    f"<div class='result'>😢 Nope! <b>{user_input}</b> is not a Palindrome.</div>",
                    unsafe_allow_html=True,
                )

        elif operation == "Toggle Case":
            toggled = "".join(
                [ch.lower() if ch.isupper() else ch.upper() for ch in user_input]
            )
            st.markdown(
                f"<div class='result'>🔡 Toggle Case: <b>{toggled}</b></div>",
                unsafe_allow_html=True,
            )

        elif operation == "Find Length":
            length = len(user_input)
            st.markdown(
                f"<div class='result'>📏 Length of String: <b>{length}</b></div>",
                unsafe_allow_html=True,
            )

# Footer
st.markdown("<br><center>👾 Built with love in pixel style 🎨</center>", unsafe_allow_html=True)
