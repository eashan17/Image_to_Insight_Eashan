import easyocr
from textblob import TextBlob
import re
from PIL import Image, ImageOps, ImageEnhance
import numpy as np

class MemeAnalyzer:
    def __init__(self):
        
        self.reader = easyocr.Reader(['en'], gpu=False)

    def extract_text(self, image_input):
       
        if isinstance(image_input, np.ndarray):
            img = Image.fromarray(image_input)
        else:
            img = image_input

        img = ImageOps.grayscale(img)
        img = ImageEnhance.Contrast(img).enhance(2.0)
        
       
        processed_img = np.array(img)
        
        
        results = self.reader.readtext(processed_img)
        valid_text = [text for (bbox, text, prob) in results if prob > 0.3]
        
        return " ".join(valid_text)

    def analyze_sentiment(self, text):
        
        processed = re.sub(r'([a-z])(and|then|over|because|the|with|for|is|are)([a-z])', r'\1 \2 \3', text.lower())
        clean_text = re.sub(r'[^a-zA-Z\s]', '', processed)
        
        
        blob = TextBlob(clean_text)
        
        return {
            "raw_text": text,
            "cleaned_text": clean_text,
            "polarity": round(blob.sentiment.polarity, 2),
            "subjectivity": round(blob.sentiment.subjectivity, 2)
        }