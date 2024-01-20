# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Set the Docker image version as an argument and environment variable
ARG DOCKER_IMAGE_VERSION=latest
ENV DOCKER_IMAGE_VERSION=${DOCKER_IMAGE_VERSION}

# Make port available to the world outside this container
EXPOSE 5001

# Run app.py when the container launches
CMD ["python", "app.py"]
