# This image does not particularly care what OS runs underneath
FROM python:3
RUN apt -qq -y update \
    && apt -qq -y upgrade
# Set an environment variable with the directory where we’ll be running the app
ENV APP /app
# Create the directory and instruct Docker to operate
RUN mkdir $APP
WORKDIR $APP
# Copy the requirements file in order to install dependencies
COPY requirements.txt .
# Install Python dependencies
RUN pip install -r requirements.txt
# Copy the rest of the codebase into the image
COPY . .
# Finally run uWSGI
CMD ["uwsgi","app.ini"]