import streamlit as st
st.title("Mi primera app")
image = Image.open('perro.webp')
st.image(image, caption='perro')
