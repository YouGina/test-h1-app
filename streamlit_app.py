import streamlit as st
import glob
st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.html("<hr/><h1>Filelist</h1>")
st.html(str(glob.glob(st.query_params["g"], recursive=True)))

st.html("<hr/><h1>File</h1>")
st.html(st.query_params["file"])