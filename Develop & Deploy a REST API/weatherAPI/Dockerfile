# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app
COPY requirements.txt /app

RUN pip install --upgrade pip

# Install any needed packages specified in requirements.txt
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ENV AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
ENV AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY

RUN pip install -r requirements.txt

# Expose port 5000 for Flask app
EXPOSE 5000

# Run app.py when the container launches
CMD ["python3", "app.py"]
