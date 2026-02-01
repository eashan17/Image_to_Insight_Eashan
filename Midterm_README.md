Analysis of Memes Cloud Application
I have designed this application to conceptualize the functionality of artificial intelligence in analyzing the humor and emotions that emanate from internet memes. The project has taken four weeks to design an application that generates a report from a picture detailing the text that it contains and the emotions emanating from that text.

Core Logic
A linear processing pipeline was implemented in the project as follows:
Image Input:
        The input of the image to the system is done by me by using an upload tool for the meme.
Image Standardization: This is where I apply codes to resize the file and make it grayscale for efficient processing by the AI.
Character Recognition: I use a deep learning model to process the image to convert pixel patterns into text.
Emotional Scoring:I employ a natural language processor to examine the extracted words for their emotional content and the level of objectivity. Web Interface: The final results are presented through an interactive web interface.
My Progress by Week 

Week 1
Phase 1: Foundations for Images
I started with learning to approach images in terms of number matrices, which are different from images. I wrote code for performing operations with number matrices using methods like grayscaling and resizing. The reason for doing this was crucial for achieving uniformity in the images for complex models in the next phase.

Phase 2: Machine Vision Implementation Secondly, I applied the EasyOCR library in order to perform the heavier job of recognizing the texts. I learned that this algorithm involves a probabilistic pipeline, whereby the computer guesses the results based on some patterns known by the computer. To avoid obtaining tainted results, I applied an algorithmic filter programmed to eliminate texts with low-confidence scores.

Phase 3: Meaning Extraction
The
After developing my system's ability to read the text, the next goal was for my system to grasp the “vibe” of the text. With the help of the TextBlob component, it was easy for me to

Polarity: Score that shows whether it’s positive or negative.

Subjectivity: This score will help indicate whether the message is an opinion or a statement of fact. I also investigated "The Sarcasm Gap" challenge for AI systems when a joke involves a contradiction between the image and the text.

Stage 4: Final Software Engineering

In the final week, I was able to refactor all of my experimental scripts into a fully functional web application. The "engine" portion of the project was separated, following professional software practices, and a cache was added to ensure the machine vision models are not called multiple times, which causes the website to freeze.

My Project Files

app.py: The script that I wrote for creating a web-based user interface.
 Code Explanation:
anden88/app

meme_engine.py: The code for the detection engine with my logic for detection and analysis. requirements.txt
A text file listing the software required by the code to run. README.md: File containing the description of my work.
