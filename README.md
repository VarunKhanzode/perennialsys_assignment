# Employee Search API

## Features
- Dynamic columns per organization
- Search and filtering
- Custom rate limiting

## Quick Start

## Prerequisites

- Python 3.9+

---

## Running Locally

# Clone the repo and navigate to the directory:

- git clone https://github.com/VarunKhanzode/perennialsys_assignment.git
- cd perennialsys_assignment

# Create and activate a virtual environment:

- python3 -m venv env
- source env/bin/activate

# Install dependencies:

- pip install -r requirements.txt

# Run the application:

- uvicorn main:app --reload

# Load sample data :

curl -X POST http://localhost:8000/load-sample-data

# Visit API docs:

# Swagger UI: http://localhost:8000/docs

# ReDoc: http://localhost:8000/redoc

