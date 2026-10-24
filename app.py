import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

st.set_page_config(page_title="ChestScan AI - Prototype", page_icon="🩺")

@st.cache_resource
def load_model():
    return tf.keras.models.load_model("chestscan_mobilenet_finetuned.keras")

model = load_model()
class_names = ['NORMAL', 'PNEUMONIA']

st.title("🩺 ChestScan AI - Analyse de Radiographies")

uploaded_file = st.file_uploader("Importer une radiographie thoracique (JPEG, PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption='Radiographie importée', use_container_width=True)
    
    if st.button("Lancer l'analyse"):
        with st.spinner("Analyse en cours par l'intelligence artificielle..."):
            img_resized = image.resize((224, 224))
            img_array = tf.keras.utils.img_to_array(img_resized)
            img_array = np.expand_dims(img_array, axis=0)
            img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)
            
            score = model.predict(img_array)[0][0]
            pred_idx = 1 if score >= 0.5 else 0
            result_class = class_names[pred_idx]
            
            st.subheader("Résultats :")
            if result_class == 'PNEUMONIA':
                st.error(f"**PNEUMONIE DÉTECTÉE** (Confiance : {score*100:.2f}%)")
            else:
                st.success(f"**NORMAL** (Confiance : {(1-score)*100:.2f}%)")