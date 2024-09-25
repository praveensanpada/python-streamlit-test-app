import streamlit as st
from PIL import Image

# Set the title of the Streamlit application
st.title("AWS Face Recognition")

# File uploader widget
img_file = st.file_uploader("Upload Image", type=['png', 'jpg', 'jpeg'])

def load_image(img):
    # Function to load an image from file
    return Image.open(img)

if img_file is not None:
    # Display file details
    file_details = {}
    file_details['name'] = img_file.name
    file_details['type'] = img_file.type
    file_details['size'] = img_file.size
    st.write(file_details)

    # Save the uploaded image to the local filesystem
    with open('predict_image.jpg', 'wb') as f:
        f.write(img_file.getbuffer())
    
    # Display the uploaded image
    st.image(load_image(img_file), width=250)
