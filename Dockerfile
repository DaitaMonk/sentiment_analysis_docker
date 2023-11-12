# Use the official Python 3.9 image as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt ./

# Install the Python dependencies from the requirements file
RUN pip install -r requirements.txt

# Create a writable directory for the user
RUN mkdir /.cache
RUN chmod -R 777 /.cache

# Copy your Streamlit app file into the container
COPY ./app.py .


#Copy the dataset folder
COPY Datasets/ Datasets/


# Copy all Python files from the pages folder, including those with emojis
COPY pages/ pages/


#Copy team logo and photos

# Copy the 'Team logo/' folder and its contents into the '/app/Teamlogo/' directory
COPY ["Team logo/", "/app/Team logo/"]

# Copy the 'Team photos/' folder and its contents into the '/app/Teamphotos/' directory
COPY ["Team photos/", "/app/Team photos/"]

# Expose port 8501, which is the default port for Streamlit apps
EXPOSE 8501

# Define the command to run your Streamlit app
CMD ["streamlit", "run", "app.py"]
