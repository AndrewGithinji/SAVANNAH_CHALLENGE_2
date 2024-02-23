# Use the official Python image as the base image
FROM python:3.11

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /SAVANNAH_CHALLENGE_2

# Copy the requirements file into the container
COPY requirements.txt /SAVANNAH_CHALLENGE_2/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the project files into the container
COPY . /SAVANNAH_CHALLENGE_2/

# Apply Django migrations
RUN python manage.py makemigrations
RUN python manage.py migrate

# Create a superuser (if applicable)
RUN python manage.py createsuperuser --noinput

# Expose the port that the app will run on
EXPOSE 8000

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
