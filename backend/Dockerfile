# pull official base image
FROM python:3.11.4-slim-buster

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
RUN apt-get update -y
RUN apt-get install pkg-config -y
RUN apt-get install -y python3-dev build-essential
RUN apt-get install -y default-libmysqlclient-dev

COPY ./requirements.txt .
RUN pip install -r requirements.txt

# add app
COPY . .

# start app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
