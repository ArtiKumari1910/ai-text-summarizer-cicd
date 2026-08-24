# AI Text Summarizer

An AI-powered text summarization API built with FastAPI and Hugging Face Transformers. The application is containerized using Docker and integrated with a Jenkins CI/CD pipeline for automated build, DockerHub image publishing, and deployment.

## Features

- AI-based text summarization
- FastAPI REST API
- Health check endpoint
- Hugging Face Transformers model
- Docker containerization
- Jenkins CI/CD pipeline
- Automated Docker image build
- Automated DockerHub image push
- Automated Docker container deployment

## Technologies Used

- Python
- FastAPI
- Hugging Face Transformers
- PyTorch
- Docker
- Jenkins
- GitHub
- DockerHub
- Linux / WSL

## Project Structure

```text
ai-devops-project/
|
|-- app/
|   |-- main.py
|
|-- .gitignore
|-- Dockerfile
|-- Jenkinsfile
|-- requirements.txt
|-- README.md
```

## API Endpoints

### Home

GET /

### Health Check

GET /health

### Summarize Text

POST /summarize