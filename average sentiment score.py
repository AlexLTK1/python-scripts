import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import os
import re

def clean_text(text):
    """Cleans text by removing punctuation, digits, and extra whitespace."""
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = re.sub(r'\d+', '', text)  # Remove digits
    text = re.sub(r'\s+', ' ', text)  # Remove extra whitespace
    text = text.lower()  # Convert to lowercase
    return text.strip()

def read_documents(folder_path):
    """Reads all text documents in a folder and returns a list of their contents."""
    documents = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r') as file:
                documents.append(file.read())
    return documents

def calculate_sentiment_scores(documents):
    """Calculates the average sentiment score for each document in a list of documents."""
    sia = SentimentIntensityAnalyzer()
    scores = []
    for document in documents:
        cleaned_document = clean_text(document)
        score = sia.polarity_scores(cleaned_document)['compound']
        scores.append(score)
    return scores

def calculate_average_score(scores):
    """Calculates the average score for a list of scores."""
    return sum(scores) / len(scores)

if __name__ == '__main__':
    folder_path = 'path/to/folder'
    documents = read_documents(folder_path)
    scores = calculate_sentiment_scores(documents)
    average_score = calculate_average_score(scores)
    print(f'The average sentiment score for the documents is {average_score:.2f}')
