import streamlit as st

# Set page config with a bright theme
st.set_page_config(page_title="Word Arena 🎮", page_icon="✨", layout="centered")

# Custom CSS for brighter, aesthetic look
st.markdown(
    """
    <style>
    body {
        background-color: #fff8f0;
        color: #333333;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    .title {
        text-align: center;
        font-size: 36px;
        color: #ff4081;
    }
    .result {
        font-size: 24px;
        padding: 10px;
        border-radius: 12px;
        margin-top: 10px;
        background-color: #ffe0f0;
        color: #4a148c;
        text-align: center;
    }
    .stButton button {
        background-color: #ff80ab !important;
        color: white !important;
        font-size: 18px !important;
        border-radius: 10px !important;
        padding: 8px 16px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title
st.markdown("<h1 class='title'>✨ Word Arena ✨</h1>", unsafe_allow_html=True)

# Input box
user_input = st.text_input("👉 Enter a word or phrase:")

# User selects operation
operation = st.radio(
    "🔧 Choose an operation:",
    ["Reverse the string", "Check if palindrome"],
    horizontal=True,
)

if st.button("Go! 🚀"):
    if user_input.strip() == "":
        st.warning("Please enter something first 💡")
    else:
        if operation == "Reverse the string":
            reversed_str = user_input[::-1]
            st.markdown(
                f"<div class='result'>🔄 Reversed: <b>{reversed_str}</b></div>",
                unsafe_allow_html=True,
            )

        elif operation == "Check if palindrome":
            reversed_str = user_input[::-1]
            if user_input.lower() == reversed_str.lower():
                st.markdown(
                    f"<div class='result'>🎉 Yes! <b>{user_input}</b> is a Palindrome </div>",
                    unsafe_allow_html=True,
                )
                st.balloons()
                st.snow()
            else:
                st.markdown(
                    f"<div class='result'>😔 Nope! <b>{user_input}</b> is not a Palindrome</div>",
                    unsafe_allow_html=True,
                )

# Footer
st.markdown("<br><br><center>Made with using Streamlit</center>", unsafe_allow_html=True)
