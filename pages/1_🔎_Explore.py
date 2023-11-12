# Load libraries
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
import plotly
from collections import Counter


# Define functions
def load_data(path):
    dataset = pd.read_csv(path)
    return dataset


# Load the dataset
data_path = "Datasets/clean_data.csv"
load_df = load_data(data_path)

load_df.dropna(inplace=True)
load_df = load_df.drop("Unnamed: 0", axis=1)

# Define section
data = st.container()

# Set up the data section that users will interact with
with data:
    data.title("On this page,you can explore and see visuals from the dataset")
    st.write("View the Dataset below")

    # Button to preview the dataset
    if st.button("Preview the dataset"):
        data.write(load_df)

    # Button to view the chart
    st.write("Graph showing tweet length can be viewed below")
    if st.button("View Chart"):

        # we add a column tweet_length to see length of tweet
        load_df["tweet_length"] = [len(i.split(" "))for i in load_df["tweets"]]

        # Get the value counts of tweet_length
        tweet_length_value_counts = load_df['tweet_length'].value_counts(
        ).reset_index()
        tweet_length_value_counts.columns = ['tweet_length', 'count']

        fig = px.scatter(data_frame=tweet_length_value_counts, x="tweet_length",
                         y="count", size="count", color="tweet_length", title="Length of Tweets")
        st.plotly_chart(fig)


# Adding visual of distribution graph
st.write("View the Distribution of Sentiment")
if st.button("Sentiment Graph"):

    # Create a plotly chart
    fig = px.bar(load_df, x=load_df['label'].value_counts(
    ).index, y=load_df['label'].value_counts().values,  title="Distribution of Sentiment")

    # Display the chart using st.plotly_chart()
    st.subheader("A plot of sentiment graph")
    st.plotly_chart(fig)


# Add graph for top 10 words
st.write("View the top 10 most important words in the dataset")
if st.button("Top 10 words"):

    # Count word frequencies
    word_counts = Counter(" ".join(load_df["tweets"]).split())

    # Get the most common words and their frequencies
    most_common_words = word_counts.most_common()

    # Print the top N most frequent words
    N = 10  # Change N to the desired number of top words

    # Create a list of dictionaries
    top_words_list = [{"Word": word, "Frequency": count}
                      for word, count in most_common_words[:N]]

    # Convert the list to a DataFrame
    top_words_df = pd.DataFrame(top_words_list)

    # create plotly chart
    fig = px.treemap(top_words_df, path=[
                     "Word"], values="Frequency", title=f"Top {N} Most Frequent Words")

    # Display the chart using st.plotly_chart()
    st.subheader("A plot of the top 10 most used words")
    st.plotly_chart(fig)
