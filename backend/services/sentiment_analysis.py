import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import spacy

nlp = spacy.load('en_core_web_sm')

class SentimentAnalyzer:
    def __init__(self):
        self.sia = SentimentIntensityAnalyzer()

    def analyze_sentiment(self, text):
        doc = nlp(text)
        sentiment_scores = self.sia.polarity_scores(text)
        return sentiment_scores
