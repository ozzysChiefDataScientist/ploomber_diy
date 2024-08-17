# Use the official Python image as the base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.lock.txt file into the container
COPY requirements.lock.txt .

# Install any system dependencies (if needed)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install the Python dependencies from requirements.lock.txt
RUN pip install --no-cache-dir -r requirements.lock.txt

# Copy the rest of the application code into the container
COPY . .

# Execute the Ploomber build command
CMD ["ploomber", "build", "--force"]
