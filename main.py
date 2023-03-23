import streamlit as st
from src.utils import *
import json

#read config file
with open('config.json') as f:
    config = json.load(f)

API_URL = config['API_URL']

st.title('Image Classifier')
st.write('Upload an image to classify it')
uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file is not None:
    show_image(uploaded_file)
    if submit_button():
        st.write("Classifying...")
        response = get_prediction(uploaded_file, API_URL)
        st.write("Classified!")
        st.write(response)






