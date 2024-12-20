import streamlit as st
from PIL import Image
# started the camera

with st.expander("Upload Picture"):
    upload_image = st.file_uploader("Upload Image")

with st.expander("start camera"):
    camera_image = st.camera_input("Camera")
    #print(camera_image)

if camera_image:

    # create a pillow image instance
    img = Image.open(camera_image)

    #convert the pillow image to greyscale
    grey_img = img.convert("L")

    #Render the greyscale image on the webpage
    st.image(grey_img)
if upload_image:

    # create a pillow image instance
    img = Image.open(upload_image)

    #convert the pillow image to greyscale
    grey_img = img.convert("L")

    #Render the greyscale image on the webpage
    st.image(grey_img)