import streamlit as st

# Inject CSS for better visibility
st.markdown("""
    <style>
    .big-label {
        font-size: 22px !important;
        color: #222222 !important; /* dark grey, easy to read */
        font-weight: 600 !important;
    }
    .score-label {
        font-size: 20px !important;
        color: #ff4b4b !important; /* bright red for visibility */
        font-weight: 700 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🎮 Word Fun Game")
st.write("Reverse words, check palindromes, and score points!")

# User input
user_input = st.text_input("Enter a word:")

# Score tracker
if "score" not in st.session_state:
    st.session_state.score = 0

# Logic
if user_input:
    reversed_str = user_input[::-1]
    st.markdown(f"<p class='big-label'>🔄 Reversed Word: {reversed_str}</p>", unsafe_allow_html=True)

    if user_input.lower() == reversed_str.lower():
        st.success("🎉 It's a palindrome!")
        st.session_state.score += 10
    else:
        st.warning("❌ Not a palindrome!")

    st.markdown(f"<p class='score-label'>🏆 Score: {st.session_state.score}</p>", unsafe_allow_html=True)
