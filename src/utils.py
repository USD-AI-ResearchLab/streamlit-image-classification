import requests
from PIL import Image
import streamlit as st

def upload_image():
    """Uploads an image and returns the image as a PIL object"""

    uploaded_file = st.file_uploader("Choose an image...", type="jpg")
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        return image
    return None

def show_image(image):
    """Shows an image using streamlit"""
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    return None

def submit_button():
    """Creates a submit button"""
    return st.button("Classify")

def get_prediction(image, api_url):
    """Sends an image to the API and returns the prediction"""
    response = requests.post(api_url, files={"file": image})
    return f"The prediction is: {response.text}"


