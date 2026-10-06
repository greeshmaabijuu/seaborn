import streamlit as st
import pandas as pd

st.title("My First Streamlit Application")

st.header("Welcome to my app")
st.subheader("This is a simple Streamlit application.")
st.write("Feel free to explore the different features of this app")
st.text("This is a text element.")

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
})

st.table(df)

agree = st.checkbox("I agree")

if agree:
    st.write("Great!")
    
    import streamlit as st

enable = st.checkbox("Enable camera")
picture = st.camera_input("Take a picture", disabled=not enable)

if picture:
    st.image(picture)
    import streamlit as st

picture = st.camera_input("Scan QR code", resolution="720p")

if picture:
    st.image(picture)