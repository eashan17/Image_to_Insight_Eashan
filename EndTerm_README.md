## Analysis of Memes Cloud Application  

This application was designed to demonstrate how artificial intelligence can be used to analyze the humor and emotions present in internet memes. Over a period of four weeks, a complete system was developed that generates a detailed report from a meme image by extracting the text it contains and identifying the emotions conveyed through that text.

The project follows a structured AI pipeline that converts raw image data into meaningful insights.

---

## Core Logic  

A linear processing pipeline was implemented as follows:

**Image Input**  
Users upload a meme image using the web interface.

**Image Standardization**  
The uploaded image is resized and converted to grayscale to ensure uniformity and efficient processing.

**Character Recognition**  
A deep learning-based OCR model converts pixel patterns into readable text.

**Emotional Scoring**  
A natural language processing model analyzes the extracted text to determine sentiment and objectivity.

**Web Interface**  
The final extracted text and emotional analysis are displayed through an interactive web application.

---

## Project Progress  

### Week 1: Image Foundations  

Images were studied as numerical matrices rather than visual objects. Basic preprocessing operations such as resizing and grayscale conversion were implemented to standardize input data.

---

### Week 2: Machine Vision Implementation  

EasyOCR was integrated to perform text recognition on meme images. A confidence filtering mechanism was applied to remove low-reliability OCR results and improve accuracy.

---

### Week 3: Meaning Extraction  

TextBlob was used to analyze the emotional tone of extracted text through:

- Polarity score for positive or negative sentiment  
- Subjectivity score for opinion versus factual content  

The limitation known as the "Sarcasm Gap" was also explored.

---

### Week 4: Software Engineering and Deployment  

All experimental scripts were refactored into a complete web application. Backend logic was separated from frontend components, and caching was added to improve performance and prevent repeated model loading.

---

## Project Files  

**app.py**  
Streamlit-based web interface for user interaction.

**meme_engine.py**  
Core analysis engine for OCR and sentiment processing.

**requirements.txt**  
List of required Python packages.

**README.md**  
Project documentation and overview.

