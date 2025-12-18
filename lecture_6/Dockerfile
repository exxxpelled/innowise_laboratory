# Use Python 3.13.7 slim version as base image
FROM python:3.13.7-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements file to working directory
COPY requirements.txt .

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application files to working directory
COPY . .

# Expose port 8000 for FastAPI application
EXPOSE 8000

# Run FastAPI server
# app.main:app = from app.main import app
# 0.0.0.0 = accessible from outside container
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]