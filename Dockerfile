# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables to prevent Python from writing pyc files to disk and buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Flask is running on
EXPOSE 5000

# Ensure that the cards.json file is created and is writable
RUN touch /app/cards.json && chmod 666 /app/cards.json

# Set the default command to run the Flask application
CMD ["python", "app.py"]

# Keep the image size small by removing the build dependencies
RUN apt-get purge -y --auto-remove \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
