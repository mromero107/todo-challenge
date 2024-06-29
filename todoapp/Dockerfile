# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables for Python and Docker
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

# Set the working directory in the container
WORKDIR /code

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /code/
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the Django project code into the container
COPY . /code/

# Expose the port on which your Django app will run
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
