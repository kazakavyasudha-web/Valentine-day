import streamlit as st

# ---------------------------------
# Page Config
# ---------------------------------
st.set_page_config(page_title="For You ❤️", layout="centered")

# ---------------------------------
# Pink Cute Styling
# ---------------------------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg,#ffd6e8,#ffc2dc,#ff9ecb);
}

/* center everything */
.main {
    display:flex;
    align-items:center;
    justify-content:center;
    height:100vh;
}

/* cute card */
.card {
    background:white;
    padding:40px 25px;
    border-radius:25px;
    width:90%;
    max-width:380px;
    text-align:center;
    box-shadow:0 15px 40px rgba(0,0,0,0.15);
}

/* question text */
.question {
    font-size:22px;
    font-weight:600;
    margin-bottom:25px;
    color:#ff4d8d;
}

/* buttons */
.stButton>button {
    width:100%;
    border-radius:14px;
    padding:12px 0;
    font-size:16px;
    font-weight:600;
    background:#ff4d8d;
    color:white;
    border:none;
    margin:6px 0;
}

/* lighter pink for secondary */
.secondary button {
    background:#ffc2dc !important;
    color:#333 !important;
}

</style>
""", unsafe_allow_html=True)


# ---------------------------------
# Session State
# ---------------------------------
if "step" not in st.session_state:
    st.session_state.step = 0

if "dramatic" not in st.session_state:
    st.session_state.dramatic = False


def next_step():
    st.session_state.step += 1


# ---------------------------------
# Center wrapper
# ---------------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)


# ---------------------------------
# Steps Flow
# ---------------------------------

# Intro
if st.session_state.step == 0:
    st.markdown('<div class="question">Ready for a tiny quiz about us? 😄</div>', unsafe_allow_html=True)
    st.button("Start ❤️", on_click=next_step)


# Question 1 (your custom)
elif st.session_state.step == 1:
    st.markdown('<div class="question">Who’s your favorite person right now? 😏</div>', unsafe_allow_html=True)
    st.button("You", on_click=next_step)
    st.button("Only you", on_click=next_step)


# Question 2 (your custom)
elif st.session_state.step == 2:
    st.markdown('<div class="question">Can I keep you forever? 🥺</div>', unsafe_allow_html=True)
    st.button("Yes", on_click=next_step)
    st.button("Definitely yes", on_click=next_step)


# Final proposal
else:

    if st.session_state.dramatic:
        question_text = "Will you be my Valentine or should I cry dramatically? 🥺"
    else:
        question_text = "Will you be my Valentine? 💖"

    st.markdown(f'<div class="question">{question_text}</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    # YES
    with col1:
        if st.button("YES ❤️"):
            st.balloons()
            st.success("YAYYYY 🥰💞 You just made my day!")

    # NO
    with col2:
        if st.button("NO ❌"):
            st.session_state.dramatic = True
            st.rerun()


st.markdown('</div>', unsafe_allow_html=True)
