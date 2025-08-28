import streamlit as st
from PIL import Image
st.title("Mi primera app")
image = Image.open('perro.webp')
st.image(image, caption='perro')
