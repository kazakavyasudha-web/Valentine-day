import streamlit as st
import random

st.set_page_config(page_title="For You ❤️", layout="centered")

# --- Cute background ---
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg,#ff9ecb,#ffc3e6);
}
.big {
    font-size:28px;
    text-align:center;
    font-weight:bold;
}
button {
    border-radius: 12px !important;
}
</style>
""", unsafe_allow_html=True)


if "step" not in st.session_state:
    st.session_state.step = 0


def next_step():
    st.session_state.step += 1


# --- Steps ---
if st.session_state.step == 0:
    st.markdown('<p class="big">Ready for a few questions? 😄</p>', unsafe_allow_html=True)
    st.button("Start ❤️", on_click=next_step)


elif st.session_state.step == 1:
    st.markdown('<p class="big">Do you miss me sometimes? 🥺</p>', unsafe_allow_html=True)
    st.button("Yes", on_click=next_step)
    st.button("Always", on_click=next_step)


elif st.session_state.step == 2:
    st.markdown('<p class="big">Chocolate or me? 😏</p>', unsafe_allow_html=True)
    st.button("You", on_click=next_step)
    st.button("Obviously you", on_click=next_step)


else:
    st.markdown('<p class="big">Will you be my Valentine? 💖</p>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("YES ❤️"):
            st.balloons()
            st.success("YAYYYY 🥰 You just made my day!")

    with col2:
        # NO button prank
        if st.button("NO ❌"):
            st.warning("Wrong answer 😈 Try again")
