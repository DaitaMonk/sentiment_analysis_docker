
# Load libraries needed
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_lottie import st_lottie
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import re
from scipy.special import softmax
import torch

# define app section
header = st.container()

# Define the Lottie animation URL
lottie_animation_url = "https://lottie.host/014d5a0c-6902-4502-b791-33f924c9f682/3d9JZRiBJd.json"

# define header
with header:
    header.title(
        "Determing The Sentiment Of Covid-19 Vaccine Tweets Using Roberta Base Model")

    # Display the Lottie animation using st_lottie
    st_lottie(lottie_animation_url, height=200)

    header.write(
        "On this page,you can determine the sentiment of Covid-19 vaccine tweets")


@st.cache_resource()  # Cache the model and tokenizer
def load_model_and_tokenizer(model_name):
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    return model, tokenizer


# Load model and tokenizer
model_name = "VINAL/Roberta-Sentiment-Classifier"
model, tokenizer = load_model_and_tokenizer(model_name)

# Define text preprocessing function


def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()
    # Remove hashtags
    text = re.sub(r'#\w+', '', text)
    # Remove punctuations and  extra whitespaces
    text = re.sub("[^\w\s]", "", text)
    text = re.sub(r'\d+', '', text)
    # Remove numbers
    text = " ".join(word for word in text.split() if not word.isdigit())
    return text


# Enter input text
user_input = st.text_area("Please enter a covid-19 sentence here:")


# Define the sentiment labels
sentiment_labels = {0: "Negative", 1: "Neutral", 2: "Positive"}


def analyze_sentiment(input_text):
    preprocessed_text = preprocess_text(input_text)
    inputs = tokenizer(preprocessed_text, return_tensors="pt")
    outputs = model(**inputs)

    # Get the predicted class and associated confidence scores
    predicted_class = outputs.logits.argmax().item()
    sentiment = sentiment_labels.get(predicted_class, "Unknown")

    # Extract confidence scores (probability distribution)
    confidence_scores = outputs.logits.softmax(dim=1).tolist()[0]

    return sentiment, confidence_scores


if st.button("Analyze Sentiment"):
    if user_input:
        sentiment, confidence_scores = analyze_sentiment(user_input)

        # Create a list of (sentiment label, confidence score) pairs
        label_score_pairs = zip(sentiment_labels.values(), confidence_scores)

        # Sort the pairs in descending order of confidence scores
        sorted_label_score_pairs = sorted(
            label_score_pairs, key=lambda x: x[1], reverse=True)

        st.write("Your Sentiment is:", sentiment)

        # Create an expander for displaying the confidence scores
        with st.expander("Confidence Scores", True):
            # Display sorted sentiment labels and confidence scores
            for label, score in sorted_label_score_pairs:
                st.write(f"{label}: {score:.4f}")

st.write("""Example of sentences to input:
         
    - The New Vaccine is bad \n
    - Getting my vaccines !\n
    - Covid-19 is spreading fast
    
         """)
