import streamlit as st

# -------------------------------------------------
# Page config
# -------------------------------------------------
st.set_page_config(
    page_title="For You ❤️",
    layout="centered"
)

# -------------------------------------------------
# Pastel Cute Styling (clean + stable)
# -------------------------------------------------
st.markdown("""
<style>

/* background */
.stApp {
    background: linear-gradient(135deg,#fff5f9,#ffe6f0,#ffd6e8);
}

/* hide top padding */
.block-container {
    padding-top: 3rem;
    padding-bottom: 3rem;
}

/* center card */
.card {
    max-width: 380px;
    margin: auto;
    background: white;
    padding: 35px 25px;
    border-radius: 22px;
    text-align: center;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
}

/* question text */
.qtext {
    font-size: 21px;
    font-weight: 600;
    color: #ff4d8d;
    margin-bottom: 25px;
    line-height: 1.4;
}

/* buttons */
.stButton > button {
    width: 100%;
    border-radius: 14px;
    padding: 12px 0;
    font-size: 15px;
    font-weight: 600;
    border: none;
    margin: 6px 0;
    background: #ff7aa8;
    color: white;
}

/* soft secondary */
.soft button {
    background: #ffd6e8 !important;
    color: #444 !important;
}

</style>
""", unsafe_allow_html=True)


# -------------------------------------------------
# Session State
# -------------------------------------------------
if "step" not in st.session_state:
    st.session_state.step = 0

if "dramatic" not in st.session_state:
    st.session_state.dramatic = False


def next_step():
    st.session_state.step += 1


# -------------------------------------------------
# Card start
# -------------------------------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)


# -------------------------------------------------
# FLOW
# -------------------------------------------------

# Step 0
if st.session_state.step == 0:
    st.markdown('<div class="qtext">Ready for a tiny quiz about us? 😄</div>', unsafe_allow_html=True)
    st.button("Start ❤️", on_click=next_step)


# Step 1
elif st.session_state.step == 1:
    st.markdown('<div class="qtext">Who’s your favorite person right now? 😏</div>', unsafe_allow_html=True)
    st.button("You", on_click=next_step)
    st.button("Only you", on_click=next_step)


# Step 2 (chocolate question added)
elif st.session_state.step == 2:
    st.markdown('<div class="qtext">Chocolate or me? 🍫😌</div>', unsafe_allow_html=True)
    st.button("You", on_click=next_step)
    st.button("Obviously you", on_click=next_step)


# Step 3
elif st.session_state.step == 3:
    st.markdown('<div class="qtext">Can I keep you forever? 🥺</div>', unsafe_allow_html=True)
    st.button("Yes", on_click=next_step)
    st.button("Definitely yes", on_click=next_step)


# Final
else:

    question = (
        "Will you be my Valentine or should I cry dramatically? 🥺"
        if st.session_state.dramatic
        else "Will you be my Valentine? 💖"
    )

    st.markdown(f'<div class="qtext">{question}</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("YES ❤️"):
            st.balloons()
            st.success("YAYYYY 🥰💞 You just made my day!")

    with col2:
        if st.button("NO ❌"):
            st.session_state.dramatic = True
            st.rerun()


st.markdown('</div>', unsafe_allow_html=True)
