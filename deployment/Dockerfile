# RUNNING DOCKER -> CD TO THE REPOSITORY ROOT & EXECUTE BELOW COMMAND
# WINDOWS docker build -t django_ec2 -f .\deployment\dockerfile .
    # docker run -p 8000:8000 django_ec2
# LINUX - docker build -t django_ec2 -f ./deployment/dockerfile .

# INFO - WHY NOT TO USE ALPINE
## https://pythonspeed.com/articles/alpine-docker-python/



# BASE IMAGE
FROM python:3.7

# AUTHOR/ MAINTAINER
MAINTAINER raunak-r

# COPY THE MAIN CODE FOLDER INSIDE THE CONTAINER
ADD . /app

# SET THE DEFAULT DIRECTORY FOR CMD TO EXECUTE COMMANDS
WORKDIR /app

# INSTALL BACKEND DEPENDENCIES
RUN pip install -r ./backend/requirements.txt

# RUN THE DJANGO APP
EXPOSE 8000
RUN python ./backend/manage.py migrate
CMD [ "python", "./backend/manage.py", "runserver", "0.0.0.0:8000" ]
