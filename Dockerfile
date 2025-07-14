# Use a lightweight official Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy your Python script into the container
COPY fetch_sensor_data.py .

# Install Python dependencies
RUN pip install requests

# Set the default command to run your script
CMD ["python", "fetch_sensor_data.py"]
