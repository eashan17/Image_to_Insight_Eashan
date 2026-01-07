import streamlit as st
from meme_engine import MemeAnalyzer
from PIL import Image
import numpy as np


st.set_page_config(page_title="Final Group Submission", layout="centered")

@st.cache_resource
def load_system():
    return MemeAnalyzer()

st.title("Meme Sentiment Analyzer")

try:
    analyzer = load_system()
    uploaded_file = st.file_uploader("Upload Meme", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Current Meme", use_container_width=True)
        
        if st.button("Run Pipeline"):
            with st.spinner("Applying Image Enhancement & OCR..."):
                
                extracted_text = analyzer.extract_text(image)
                data = analyzer.analyze_sentiment(extracted_text)
                
                st.markdown("---")
                st.subheader("Final Analysis")
                
                if data['cleaned_text'].strip() == "":
                    st.warning("Detection Note: Text too blurry for high-confidence extraction.")
                else:
                    st.write(f"**Extracted Text:** {data['cleaned_text']}")
                    
                col_a, col_b = st.columns(2)
                col_a.metric("Polarity", data['polarity'])
                col_b.metric("Subjectivity", data['subjectivity'])
except Exception as e:
    st.error(f"System Error: {e}")