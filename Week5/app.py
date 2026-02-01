import streamlit as st
from meme_engine import MemeAnalyzer
from PIL import Image
import numpy as np

st.set_page_config(page_title="Refactored Meme Analyzer", layout="wide")

@st.cache_resource
def load_system():
    return MemeAnalyzer()

st.title("🤖 Meme Sentiment & Insight Dashboard")
st.markdown("---")

try:
    analyzer = load_system()
    uploaded_file = st.file_uploader("Upload Meme", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        image = Image.open(uploaded_file)
   
        col1, col2 = st.columns([1, 1])

        with col1:
            st.subheader("🖼️ Uploaded Image")
            st.image(image, use_container_width=True)
        
        with col2:
            st.subheader("📊 Pipeline Analysis")
            if st.button("Run Full Analysis"):
                with st.spinner("Processing OCR & Sentiment..."):
                    extracted_text = analyzer.extract_text(image)
                    data = analyzer.analyze_sentiment(extracted_text)

                    if data['cleaned_text'] == "":
                        st.warning("⚠️ No clear text detected. Try a higher resolution image.")
                    else:
                        st.success(f"**Extracted:** {data['cleaned_text']}")
                    
                    m_col1, m_col2 = st.columns(2)
                    m_col1.metric("Polarity", data['polarity'], help="Negative (-1) to Positive (+1)")
                    m_col2.metric("Subjectivity", data['subjectivity'], help="Fact (0) to Opinion (1)")
                    
                    st.markdown("---")
                    st.header(f"**Meme Purpose:** {data['purpose']}")
                    
except Exception as e:
    st.error(f"System Error: {e}")