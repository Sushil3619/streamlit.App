import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf

# Load pretrained Keras/TensorFlow model (assumes model file 'plant_disease_model.h5' is in the same folder)
model = tf.keras.models.load_model('plant_disease_model.h5')

# Dictionary to map model output indices to disease names
disease_dict = {
    0: "Apple Scab",
    1: "Apple Black Rot",
    2: "Apple Cedar Rust",
    3: "Apple Healthy",
    4: "Corn Cercospora Leaf Spot",
    5: "Corn Common Rust",
    6: "Corn Healthy",
    # Add more classes based on your model
}

def preprocess_image(image):
    image = image.resize((128, 128))  # Resize to model input size
    image = np.array(image)
    image = image / 255.0  # normalize
    image = np.expand_dims(image, axis=0)  # batch dimension
    return image

def main():
    st.title("Agriculture Sector - Plant Disease Analysis")
    st.write("Upload a plant leaf image to predict the disease or confirm it is healthy.")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert('RGB')
        st.image(image, caption='Uploaded Leaf Image', use_column_width=True)

        if st.button("Predict Disease"):
            processed_image = preprocess_image(image)
            prediction = model.predict(processed_image)
            predicted_class = np.argmax(prediction, axis=1)[0]
            confidence = np.max(prediction)

            disease_name = disease_dict.get(predicted_class, "Unknown Disease")

            st.success(f"Prediction: {disease_name}")
            st.info(f"Confidence: {confidence:.2f}")

if __name__ == "__main__":
    main()
