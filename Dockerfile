# Use official Python image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy all files to the container's /app folder
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables for Flask
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development

# Expose port 5000 for Flask
EXPOSE 5000

# Run Flask app
CMD ["flask", "run"]
