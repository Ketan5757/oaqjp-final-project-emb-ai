"""Flask app for emotion detection."""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """Render the home page with the input form."""
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    """
    Process the input text, run emotion detection, and return a formatted response.
    If input is blank or invalid, return an error message.
    """
    text = request.form['text']
    result = emotion_detector(text)

    if result.get('dominant_emotion') is None:
        return "Invalid text! Please try again!"

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response_text

if __name__ == '__main__':
    app.run(debug=True)
