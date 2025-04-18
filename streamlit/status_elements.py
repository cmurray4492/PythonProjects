import streamlit as st
import time

# progress
st.header('st.progress')
st.caption('Display a progress bar')


def progress_bar():
    for pct_complete in range(1, 101):
        time.sleep(0.1)
        my_bar.progress(pct_complete)


# spinner
with st.spinner("wait for it!"):
    my_bar = st.progress(0)
    progress_bar()


# info status message
st.subheader("st.info()")
st.info("This is an information message")

st.subheader("st.success()")
st.success("This is a success message")

st.subheader("st.warning()")
st.warning("This is a warning message")

st.subheader("st.error()")
st.error("This is an error message")

time.sleep(2)
st.balloons()
