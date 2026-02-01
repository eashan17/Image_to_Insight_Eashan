import easyocr
from textblob import TextBlob
import re
import numpy as np
from PIL import Image

class MemeAnalyzer:
    def __init__(self):
        self.reader = easyocr.Reader(['en'], gpu=False)

    def extract_text(self, image_input):
        if isinstance(image_input, Image.Image):
            image_data = np.array(image_input.convert('RGB'))
        else:
            image_data = image_input

        results = self.reader.readtext(image_data)
        filtered_text = [text for (bbox, text, prob) in results if prob > 0.4]
        return " ".join(filtered_text)

    def analyze_sentiment(self, text):
        clean_text = re.sub(r'[^a-zA-Z\s]', '', text.lower()).strip()
        
        if not clean_text:
            return {"cleaned_text": "", "polarity": 0.0, "subjectivity": 0.0, "purpose": "Unknown"}

        blob = TextBlob(clean_text)
        pol = round(blob.sentiment.polarity, 2)
        subj = round(blob.sentiment.subjectivity, 2)

        if pol > 0.2 and subj > 0.5:
            purpose = "🎉 Wholesome / Uplifting"
        elif pol < -0.2 and subj > 0.5:
            purpose = "😤 Relatable Frustration / Venting"
        elif subj < 0.3:
            purpose = "📰 Factual / Educational"
        else:
            purpose = "🎭 General Humor"

        return {
            "cleaned_text": clean_text,
            "polarity": pol,
            "subjectivity": subj,
            "purpose": purpose
        }