# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY "Develop & Deploy a REST API/weatherAPI/requirements.txt" /app
COPY "Develop & Deploy a REST API/weatherAPI/app.py" /app

RUN ls -la /app

# Display the current directory contents for debugging
RUN ls -la /app

# Install any needed packages specified in requirements.txt
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ENV AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
ENV AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port 5000 for Flask app
EXPOSE 5000

# Run app.py when the container launches
CMD ["python3", "app.py"]
