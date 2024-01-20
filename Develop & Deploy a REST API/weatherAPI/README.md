# Weather Flask API

This is a Flask application that provides weather information using the OpenWeather API. The application includes a health status check endpoint and an endpoint to get weather information for a specified city.

## Prerequisites

Before running the application, make sure you have the following prerequisites installed:

- Python 3.x
- Virtual Env
- Docker (for containerization)
- AWS CLI (for accessing AWS Secrets Manager)

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/weather-flask-app.git
    cd weather-flask-app
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask application:

    ```bash
    python app.py
    ```

    The application should be running at `http://localhost:5000/health` & `http://localhost:5000/api/weather`.

## Configuration

The application retrieves OpenWeather API key from AWS Secrets Manager. Make sure you have configured the necessary AWS credentials on your machine.

## Usage

### Health Check

Check the health status of the application:

```bash
curl http://localhost:5000/health
```

### Weather API

Get weather information from below url:

```bash
curl http://localhost:5000/api/weather
```

## CI/CD Pipeline

The CI/CD pipeline automatically builds and pushes Docker images to Docker Hub on each push to the `main` branch. The versioning is handled dynamically, and each image is tagged with an incremented version number.

### GitHub Actions Workflow

The CI/CD workflow is defined in `.github/workflows/docker-build.yml`. It includes the following steps:

1. **Checkout Code**: Checks out the source code from the repository.
2. **Get Previous Version**: Retrieves the previous Docker image version from Docker Hub.
3. **Login to Docker Hub**: Authenticates with Docker Hub using Docker Hub credentials.
4. **Build, Tag, and Push Image**: Builds the Docker image, tags it with the incremented version, and pushes it to Docker Hub.
