# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy code
COPY . .

# Expose the port Flask runs on
ENV PORT=8080

# Start app with Gunicorn
CMD ["gunicorn", "-b", ":8080", "main:app"]
