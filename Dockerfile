# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Set environment variables (if any)
ENV GOOGLE_APPLICATION_CREDENTIALS=/app/keyfile.json

# Copy the Google Cloud credentials into the container
COPY keyfile.json /app/keyfile.json

# Command to run your script
CMD ["python", "src/etl.py"]
