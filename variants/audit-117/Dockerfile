# Use official Python runtime as base image
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Copy requirements file (if it exists)
# Uncomment the next two lines if you have a requirements.txt
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Create a non-root user to run the application
RUN useradd -m -u 1000 appuser && \
    chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Run the application
CMD ["python", "app.py"]

# For students: This Dockerfile demonstrates:
# - Multi-stage builds (can be extended)
# - Security best practices (non-root user)
# - Environment variables
# - Layer caching optimization (COPY requirements before code)
