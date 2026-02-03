import streamlit as st

# -------------------------------------------------
# Page config
# -------------------------------------------------
st.set_page_config(page_title="For You ❤️", layout="centered")


# -------------------------------------------------
# Pastel romantic styling
# -------------------------------------------------
st.markdown("""
<style>

/* soft pastel background */
.stApp {
    background: linear-gradient(135deg,#fff6fa,#ffeaf3,#ffdbe9);
}

/* center layout */
.block-container {
    max-width: 420px;
    margin: auto;
    padding-top: 12vh;
    text-align: center;
}

/* question text */
.question {
    font-size: 24px;
    font-weight: 600;
    color: #ff4d8d;
    line-height: 1.5;
    margin-bottom: 30px;
}

/* minimal clean buttons (no boxes look) */
.stButton > button {
    background: transparent;
    color: #ff4d8d;
    border: none;
    font-size: 18px;
    padding: 10px 0;
    margin: 6px 0;
    font-weight: 600;
}

.stButton > button:hover {
    transform: scale(1.05);
}

/* floating hearts animation */
.hearts {
    position: fixed;
    bottom: 0;
    width: 100%;
    text-align: center;
    font-size: 28px;
    animation: floatUp 3s ease-in infinite;
}

@keyframes floatUp {
    0% {transform: translateY(0); opacity:1;}
    100% {transform: translateY(-600px); opacity:0;}
}

</style>
""", unsafe_allow_html=True)


# -------------------------------------------------
# Session state
# -------------------------------------------------
if "step" not in st.session_state:
    st.session_state.step = 0

if "dramatic" not in st.session_state:
    st.session_state.dramatic = False

if "celebrate" not in st.session_state:
    st.session_state.celebrate = False


def next_step():
    st.session_state.step += 1


# -------------------------------------------------
# Flow
# -------------------------------------------------

# Step 0
if st.session_state.step == 0:
    st.markdown('<div class="question">Ready for something cute? 😄</div>', unsafe_allow_html=True)
    st.button("Start ❤️", on_click=next_step)


# Step 1 (NEW: miss me question)
elif st.session_state.step == 1:
    st.markdown('<div class="question">Will you miss me when I’m not around? 🥺</div>', unsafe_allow_html=True)
    st.button("Yes", on_click=next_step)
    st.button("Always", on_click=next_step)


# Step 2
elif st.session_state.step == 2:
    st.markdown('<div class="question">Who’s your favorite person right now? 😏</div>', unsafe_allow_html=True)
    st.button("You", on_click=next_step)
    st.button("Only you", on_click=next_step)


# Step 3
elif st.session_state.step == 3:
    st.markdown('<div class="question">Can I keep you forever? 🥺</div>', unsafe_allow_html=True)
    st.button("Yes", on_click=next_step)
    st.button("Definitely yes", on_click=next_step)


# Final Proposal
else:

    question = (
        "Will you be my Valentine or should I cry dramatically? 🥺"
        if st.session_state.dramatic
        else "Will you be my Valentine? 💖"
    )

    st.markdown(f'<div class="question">{question}</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("YES ❤️"):
            st.session_state.celebrate = True

    with col2:
        if st.button("NO"):
            st.session_state.dramatic = True
            st.rerun()


# -------------------------------------------------
# Heart celebration (custom red hearts)
# -------------------------------------------------
if st.session_state.celebrate:
    st.markdown("""
    <div class="hearts">❤️ ❤️ ❤️ ❤️ ❤️ ❤️ ❤️ ❤️ ❤️ ❤️</div>
    <div class="hearts" style="animation-delay:1s;">💖 💗 💓 💞 💕</div>
    """, unsafe_allow_html=True)

    st.success("Yayyyy 🥰 You just made my whole day!")
