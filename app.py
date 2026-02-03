import streamlit as st

# ----------------------------------------
# Page config
# ----------------------------------------
st.set_page_config(page_title="For You ❤️", layout="centered")

# ----------------------------------------
# Soft pastel styling (SAFE CSS only)
# ----------------------------------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg,#fff6fa,#ffeaf3,#ffdbe9);
}

/* center everything nicely */
.block-container {
    max-width: 420px;
    padding-top: 8vh;
    padding-bottom: 8vh;
    margin: auto;
}

/* question text */
.question {
    text-align: center;
    font-size: 22px;
    font-weight: 600;
    color: #ff4d8d;
    margin-bottom: 25px;
    line-height: 1.5;
    word-wrap: break-word;
}

/* buttons */
.stButton > button {
    width: 100%;
    border-radius: 14px;
    padding: 12px 0;
    font-size: 15px;
    font-weight: 600;
    margin: 6px 0;
    background-color: #ff7aa8;
    color: white;
    border: none;
}

/* softer secondary buttons */
.secondary button {
    background-color: #ffd6e8 !important;
    color: #444 !important;
}

</style>
""", unsafe_allow_html=True)


# ----------------------------------------
# Session state
# ----------------------------------------
if "step" not in st.session_state:
    st.session_state.step = 0

if "dramatic" not in st.session_state:
    st.session_state.dramatic = False


def next_step():
    st.session_state.step += 1


# ----------------------------------------
# Card container (stable layout)
# ----------------------------------------
with st.container():

    # STEP 0
    if st.session_state.step == 0:
        st.markdown('<div class="question">Ready for a tiny quiz about us? 😄</div>', unsafe_allow_html=True)
        st.button("Start ❤️", on_click=next_step)


    # STEP 1
    elif st.session_state.step == 1:
        st.markdown('<div class="question">Who’s your favorite person right now? 😏</div>', unsafe_allow_html=True)
        st.button("You", on_click=next_step)
        st.button("Only you", on_click=next_step)


    # STEP 2 (Chocolate question)
    elif st.session_state.step == 2:
        st.markdown('<div class="question">Chocolate or me? 🍫😌</div>', unsafe_allow_html=True)
        st.button("You", on_click=next_step)
        st.button("Obviously you", on_click=next_step)


    # STEP 3
    elif st.session_state.step == 3:
        st.markdown('<div class="question">Can I keep you forever? 🥺</div>', unsafe_allow_html=True)
        st.button("Yes", on_click=next_step)
        st.button("Definitely yes", on_click=next_step)


    # FINAL
    else:

        question_text = (
            "Will you be my Valentine or should I cry dramatically? 🥺"
            if st.session_state.dramatic
            else "Will you be my Valentine? 💖"
        )

        st.markdown(f'<div class="question">{question_text}</div>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            if st.button("YES ❤️"):
                st.balloons()
                st.success("YAYYYY 🥰💞 You just made my day!")

        with col2:
            if st.button("NO ❌"):
                st.session_state.dramatic = True
                st.rerun()
