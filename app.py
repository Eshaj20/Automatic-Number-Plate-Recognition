# app.py
import streamlit as st
import easyocr
import numpy as np
import cv2
from PIL import Image
import io
import base64

# Background image URL
background_url = "https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?q=80&w=1966&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"  # Replace with your own

# Inject custom CSS
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{background_url}");
        background-attachment: fixed;
        background-size: cover;
    }}

    .main-container {{
        background-color: rgba(255, 255, 255, 0.85);
        padding: 2rem;
        border-radius: 1rem;
        box-shadow: 0px 0px 15px rgba(0,0,0,0.2);
        margin: 2rem auto;
        max-width: 800px;
    }}

    .css-1v3fvcr, .css-1wrcr25 {{  /* overrides for file uploader area */
        background-color: rgba(255, 255, 255, 0.7) !important;
        border-radius: 0.5rem;
    }}
    </style>
    """,
    unsafe_allow_html=True
)


st.title("🚘 Automatic Number Plate Recognition")
st.markdown("Upload an image or use your webcam. The app detects and reads the number plate using **EasyOCR**.")

threshold = st.slider("Confidence Threshold", 0.0, 1.0, 0.5, step=0.05)
source = st.radio("Image Source", ["Upload an Image", "Use Webcam"])

@st.cache_resource
def load_reader():
    return easyocr.Reader(['en'], gpu=False)

reader = load_reader()

def process_image(image_np):
    results = reader.readtext(image_np)
    output_img = image_np.copy()
    extracted_texts = []

    for (bbox, text, prob) in results:
        if prob >= threshold:
            (top_left, top_right, bottom_right, bottom_left) = bbox
            top_left = tuple(map(int, top_left))
            bottom_right = tuple(map(int, bottom_right))

            output_img = cv2.rectangle(output_img, top_left, bottom_right, (0, 255, 0), 2)
            output_img = cv2.putText(output_img, text, top_left, cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
            extracted_texts.append((text, prob))

    return output_img, extracted_texts

if source == "Upload an Image":
    uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image_bytes = uploaded_file.read()
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        image_np = np.array(image)

        st.image(image_np, caption="Original Image", use_column_width=True)

        with st.spinner("Processing..."):
            result_img, texts = process_image(image_np)

        st.image(result_img, caption="Detected Number Plate", use_column_width=True)

        if texts:
            st.subheader("🔍 Detected Text:")
            for text, prob in texts:
                st.write(f"**{text}** (Confidence: {prob:.2f})")
        else:
            st.warning("No text detected above the threshold.")
else:
    st.info("📷 Click below to capture from webcam (works in local Streamlit only)")
    camera_input = st.camera_input("Take a photo")

    if camera_input is not None:
        image = Image.open(camera_input).convert("RGB")
        image_np = np.array(image)

        st.image(image_np, caption="Captured Image", use_column_width=True)

        with st.spinner("Processing..."):
            result_img, texts = process_image(image_np)

        st.image(result_img, caption="Detected Number Plate", use_column_width=True)

        if texts:
            st.subheader("🔍 Detected Text:")
            for text, prob in texts:
                st.write(f"**{text}** (Confidence: {prob:.2f})")
        else:
            st.warning("No text detected above the threshold.")

st.markdown('</div>', unsafe_allow_html=True)



