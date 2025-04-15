# Use an official Python base image with Linux
FROM python:3.10-slim

# Create app directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your script
COPY pathway_pipeline.py .

# Run the script
CMD ["python", "pathway_pipeline.py"]