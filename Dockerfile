FROM python:3.10

ENV PYTHONUNBUFFERED=1
WORKDIR /code

RUN apt-get update 

# Install pipenv
RUN pip install --upgrade pip 
RUN pip install pipenv

# Install application dependencies
COPY Pipfile Pipfile.lock /code/
# We use the --system flag so packages are installed into the system python
# and not into a virtualenv. Docker containers don't need virtual environments. 
RUN pipenv install --system --dev

# Copy the application files into the image
COPY . /code/

# Expose port 8000 on the container
EXPOSE 8000