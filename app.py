
import streamlit as st

st.set_page_config(
    page_title="Hackathon App",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Hackathon App")

st.write("My Python frontend is working!")

name = st.text_input("Enter your name")

if st.button("Submit"):
    if name:
        st.success(f"Welcome, {name}!")
    else:
        st.warning("Please enter your name.")