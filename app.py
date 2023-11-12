# Import libraries
import streamlit as st
from streamlit_lottie import st_lottie

# Set page configuration
st.set_page_config(
    page_title="Welcome To Amissah's Sentiment App",
    page_icon="😃",
    layout="wide"
)

# Title and Lottie animation
st.markdown("# 👋 Welcome To Team Cape Cod's Sales Sentiment Analysis App")

lottie_animation_url = "https://lottie.host/543b1c58-ed15-49db-a83a-2aec9909b945/gJQjDHOswZ.json"
st_lottie(lottie_animation_url, height=200)

# Add CSS for animation
st.write("""
    <style>
        @keyframes slide-in {
            0% {
                transform: translateX(-100%);
            }
            100% {
                transform: translateX(0);
            }
        }
        .slide-in-animation {
            animation: slide-in 1.5s ease;
        }
    </style>
""", unsafe_allow_html=True)

# Text with animation
st.markdown('<div class="slide-in-animation">In this application, you can utilize the Roberta base model to categorize sentiments related to Covid-19. The primary goal of this challenge is to create a machine learning model capable of determining whether a Twitter post, particularly those related to vaccinations, conveys a positive, neutral, or negative sentiment.</div>', unsafe_allow_html=True)

# Variable definition
html_content = """
<div class="slide-in-animation">
    <h3>Variable Definition:</h3>
    <p><strong>safe_tweet:</strong> Text contained in the tweet with sensitive information removed</p>
    <p><strong>label:</strong> Sentiment of the tweet (-1 for negative, 0 for neutral, 1 for positive)</p>
    <p><strong>agreement:</strong> The tweets were labeled by three people, and agreement indicates the percentage of reviewers that agreed on the label. This column can be used for training but is not shared for the test set.</p>
</div>
"""

st.markdown(html_content, unsafe_allow_html=True)

# Add a sidebar
st.sidebar.success("Select a page above.")

# Create a Streamlit container for the subheader
subheader_container = st.container()

# Define the subheader content
subheader_content = """
<div class="slide-in-animation">
<h3>Things You Can Do On This App:</h3>
<ul>
  <li>Predict Sentiments</li>
  <li>Explore the data</li>
  <li>Get to know more about the team behind this app</li>
</ul>
</div>
"""

# Apply CSS animation using HTML/CSS
subheader_container.markdown(subheader_content, unsafe_allow_html=True)

# Add CSS for animation
st.write("""
<style>
    @keyframes slide-in {
        0% {
            transform: translateX(-100%);
        }
        100% {
            transform: translateX(0);
        }
    }
    .slide-in-animation {
        animation: slide-in 1.5s ease;
    }
</style>
""", unsafe_allow_html=True)
