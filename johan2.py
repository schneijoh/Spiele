import streamlit as st

st.set_page_config(page_title="ASCII Schwein", layout="centered")

st.title("🐷 ASCII-Schwein")

ascii_pig = r"""
        (\____/)
        ( o  o )
         >  ^  <
       /  _____  \
      /__/       \__\
        ||       ||
        ||       ||
       ^^ ^^     ^^ ^^
"""

st.code(ascii_pig)

st.write("Ein Schwein im ASCII-Design – läuft in Streamlit ✨")

if st.button("Neu laden"):
    st.rerun()


