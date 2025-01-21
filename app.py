import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np
import time

# Load all models at once
MODELS = {
    "Custom CNN (85% Accuracy)": 'my_cnn.keras',
    "MobileNetV1 (95% Accuracy)": 'MobileNetV1_finetuned_model.keras',
    "MobileNetV2 (92% Accuracy)": 'MobileNetV2_finetuned_model.keras'
}

# Define image size based on model input shape
IMAGE_SIZE = (224, 224)

# Set background styling
# st.markdown(
#     f"""
#     <style>
#     .stApp {{
#         background: url("https://i.redd.it/a86zrhe7c4zd1.png");
#         background-size: cover;
#         backdrop-filter: blur(25px);
#     }}
#     .stFileUploader {{
#         background-color: rgba(0, 0, 0, 0.6) !important;
#         border-radius: 10px;
#     }}
#     </style>
#     """,
#     unsafe_allow_html=True
# )

def preprocess_image(image):
    """Preprocess the uploaded image for model prediction."""
    if image.mode == 'RGBA':
        image = image.convert('RGB')
    image = image.resize(IMAGE_SIZE)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = image / 255.0
    return image

def classify_image(image_data, model):
    """Classify the uploaded image using the selected model."""
    processed_image = preprocess_image(image_data)
    prediction = model.predict(processed_image)
    class_label = int(np.round(prediction[0][0]))
    confidence = prediction[0][0]
    return class_label, confidence

# Title and description
#background: linear-gradient(90deg, #1c293b, #2a3e54);
st.markdown(
    """
    <div style="
        text-align: center; 
        font-size: 46px; 
        color: white; 
        padding: 8px 5px; 
        border-radius: 30px;
        font-weight: bold;
        -webkit-text-stroke: 1px black; /* Adds a black border around the text */
        text-stroke: 1px black;
    ">
        FauxFinder: Find the Real Art
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center; font-size: 24px;'>Upload an image, and the model will classify it as either Fake or Real Art.</p>",
    unsafe_allow_html=True)

# Model selection dropdown
selected_model_name = st.selectbox(
    "Select a Model for Classification:",
    list(MODELS.keys())
)

# Load the selected model
model = load_model(MODELS[selected_model_name])

# Model Details Expander
with st.expander("\u2699\ufe0f Model Details"):
    st.write("""
      The following models are available for classification:
      - **Custom CNN**: Achieved 85% test accuracy with a lightweight custom design.
      - **MobileNetV1**: Fine-tuned pre-trained model with 95% test accuracy, ideal for high accuracy.
      - **MobileNetV2**: Fine-tuned pre-trained model with 92% test accuracy, balancing efficiency and performance.
    """)

# Image upload and display
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"], accept_multiple_files=False)

if uploaded_file:
    st.markdown("<h3 style='text-align: center; font-size: 24px;'>Processing...</h3>", unsafe_allow_html=True)

    # Load and preprocess the uploaded image
    image = Image.open(uploaded_file)

    # Progress bar to simulate transition effect
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress_bar.progress(i + 1)

    st.success("Image uploaded successfully")

    # Make prediction
    class_label, confidence = classify_image(image, model)

    # Display results
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(image, caption=f"Uploaded Image - {uploaded_file.name}", use_container_width=True)

    with col2:
        if class_label == 0:
            st.markdown(
                """
                <div style="
                    text-align: center; 
                    font-size: 28px; 
                    color: white; 
                    background: linear-gradient(90deg, #ff4d4d, #ff9999); 
                    padding: 15px 10px; 
                    border-radius: 10px;
                    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2); 
                    font-weight: bold;
                ">
                    Fake (AI-Generated) Art
                </div>
                """,
                unsafe_allow_html=True
            )
            st.markdown(
                f"""
                <div style="
                    text-align: center; 
                    font-size: 20px; 
                    color: #4caf50; 
                    background-color: rgba(0, 0, 0, 0.7); 
                    margin-top: 10px; 
                    padding: 10px 15px; 
                    border-radius: 10px; 
                    font-weight: bold; 
                    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5); 
                    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.3);
                ">
                    Confidence Level: {confidence * 100:.2f}%
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                """
                <div style="
                    text-align: center; 
                    font-size: 28px; 
                    color: white; 
                    background: linear-gradient(90deg, #1e90ff, #3cb371); 
                    padding: 15px 10px; 
                    border-radius: 10px;
                    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2); 
                    font-weight: bold;
                ">
                    Real Art
                </div>
                """,
                unsafe_allow_html=True
            )
            st.markdown(
                f"""
                <div style="
                    text-align: center; 
                    font-size: 20px; 
                    color: #4caf50; 
                    background-color: rgba(0, 0, 0, 0.7); 
                    margin-top: 10px; 
                    padding: 10px 15px; 
                    border-radius: 10px; 
                    font-weight: bold; 
                    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5); 
                    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.3);
                ">
                    Confidence Level: {confidence * 100:.2f}%
                </div>
                """,
                unsafe_allow_html=True
            )

    # Custom Clear All Responses button
    st.markdown(
        """
        <div style="display: flex; justify-content: center; margin-top: 20px;">
            <form action="/" method="get">
                <button 
                    style="
                        font-size: 15px; 
                        padding: 12px 20px; 
                        color: white; 
                        background-color: #1968b3; 
                        border: none; 
                        border-radius: 8px; 
                        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); 
                        cursor: pointer;
                        transition: background-color 0.3s ease, transform 0.2s ease;"
                    type="submit"
                >
                    Clear Results and Upload New Images
                </button>
            </form>
        </div>
        """, unsafe_allow_html=True
    )

# Copyright Footer
st.markdown(
    """
    <hr>
    <div style='text-align: center;'>
        <p style='font-size: 1.2em; font-family: "Arial", sans-serif;'>
            © 2025 All rights reserved by 
            <a href='https://github.com/Kaleemullah-Younas' target='_blank'>
                <img src='https://img.icons8.com/?size=100&id=LoL4bFzqmAa0&format=png&color=000000' height='25' style='vertical-align: middle;'>
            </a>
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
