# Use a base image
FROM python:3.9-slim

# Set a working directory
WORKDIR /app

# Copy the application to the Docker image
COPY . .

# Install any necessary dependencies (in this case, we don't have any external dependencies)
# RUN pip install --no-cache-dir -r requirements.txt

# The default command to run when the container starts
CMD ["python", "pipeline_game.py"]
