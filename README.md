# Flask Cloud-Native Application

## Overview
This project is a Flask-based REST API designed to showcase cloud-native development principles. The application is containerized using Docker, orchestrated with Kubernetes, and deployed on Google Cloud. Anaconda is used to create and manage the development environment.

## Features
- A simple REST API with a health check endpoint (`/health`).
- Containerized application for consistent deployment across environments.
- Deployment on Google Kubernetes Engine (GKE) for scalability.
- Integrated with Prometheus for monitoring and observability.

## Technologies Used
- **Flask**: A lightweight Python web framework for building the API.
- **Docker**: Used to create a container image of the application.
- **Kubernetes**: Manages the deployment and scaling of the Docker containers.
- **Google Cloud**: Hosts the application and provides cloud services.
- **Anaconda**: Manages the project’s Python environment and dependencies.

## App.py
- **Flask Initialization**: The Flask object is created to manage the web application.
- **Root Route (/)**: This route responds with a greeting message when accessed.
- **Health Check Route (/health)**: This route returns the health status of the API, allowing for monitoring.
- **App Execution**: The application runs on all interfaces (host='0.0.0.0') and listens on port 5000.

## Setup Instructions
Clone the Repository:
```python
git clone https://github.com/aleixbadia/flask-app.git
cd flask-app
```
Create and Activate Conda Environment:
```python
conda env create -f environment.yml
conda activate cloud_native_project
```
Install Required Packages:
```python
pip install -r requirements.txt
```

## Deployment Instructions
Build the Docker image:
```python
docker build -t gcr.io/YOUR_PROJECT_ID/flask-app:v1 .
```
Push the Docker image to Google Container Registry:
```python
docker push gcr.io/YOUR_PROJECT_ID/flask-app:v1
```
Apply the Kubernetes deployment:
```python
kubectl apply -f service.yaml
```

## Testing the Application
After deployment, you can test the application by accessing the external IP provided by the LoadBalancer. The health check endpoint can be accessed at http://EXTERNAL_IP/health.

## Observability
- Prometheus: Integrate with Prometheus for monitoring the application metrics.
- Logging: Ensure logs are properly configured to capture application behavior.

## Future Improvements
- Implement a Front-end to display data from the API calls.
- Enhance the API with more complex routes and functionalities.
- Connect the app to a database.
- Implement authentication and authorization mechanisms.
- Implement automatic image generation to automatise the deployment process further.
